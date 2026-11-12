"""Differential observations against full scans; source bytes are the oracle."""
from copy import deepcopy
from dataclasses import asdict
from pathlib import Path
import os

import pytest

from code2llm.api import FAST_CONFIG, analyze, analyze_file, analyze_incremental
import code2llm.core.persistent_cache as persistent


def graph(result):
    return {'functions': {name: asdict(item) for name, item in sorted(result.functions.items())},
            'classes': {name: asdict(item) for name, item in sorted(result.classes.items())},
            'modules': {name: asdict(item) for name, item in sorted(result.modules.items())},
            'nodes': {name: asdict(item) for name, item in sorted(result.nodes.items())},
            'edges': sorted((item.source, item.target) for item in result.edges)}


@pytest.fixture
def project(tmp_path, monkeypatch):
    root = tmp_path / 'project'
    root.mkdir()
    (root / 'a.py').write_text('def entry():\n    return helper()\n\ndef helper():\n    return 1\n')
    (root / 'b.py').write_text('def other():\n    return 2\n')
    cfg = deepcopy(FAST_CONFIG)
    cfg.performance.parallel_enabled = False
    cfg.performance.cache_dir = str(tmp_path / 'legacy-file-cache')
    monkeypatch.setattr(persistent, '_DEFAULT_ROOT', str(tmp_path / 'legacy-persistent'))
    return root, cfg, tmp_path / 'private-cache'


def cold(root, cfg):
    selected = deepcopy(cfg)
    selected.performance.enable_cache = False
    selected.no_cache = True
    return analyze(str(root), selected)


def test_single_file_never_returns_sibling_symbols(project):
    root, cfg, _ = project
    result = analyze_file(str(root / 'a.py'), cfg)
    assert set(result.modules) == {'a'}
    assert set(result.functions) == {'a.entry', 'a.helper'}


def test_legacy_cache_detects_rewrite_preserving_mtime_and_size(project):
    root, cfg, _ = project
    analyze(str(root), cfg)
    path = root / 'a.py'
    before = path.stat()
    path.write_text(path.read_text().replace('helper', 'newfun'))
    os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns))
    assert graph(analyze(str(root), cfg)) == graph(cold(root, cfg))


def test_warm_api_reuses_file_analysis_but_relinks_graph(project, monkeypatch):
    root, cfg, cache = project
    first = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    from code2llm.core.file_analyzer import FileAnalyzer
    def unexpected_parse(*args):
        raise AssertionError('unchanged file was parsed again')
    monkeypatch.setattr(FileAnalyzer, 'analyze_file', unexpected_parse)
    second = analyze_incremental(str(root), cache_dir=str(cache), config=cfg, changed_files=[])
    assert second.identity == first.identity
    assert second.identity['snapshot_atomic'] is False
    assert second.incremental['analysis_candidates'] == 0
    assert second.incremental['cached_files'] == 2
    assert second.incremental['graph_relinked'] == 'full'
    assert graph(first.analysis) == graph(second.analysis)


@pytest.mark.parametrize('operation', ['edit', 'touch', 'rename', 'delete', 'same-metadata', 'same-bytes', 'config'])
def test_incremental_matches_full_scan_after_change(project, operation):
    root, cfg, cache = project
    first = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    a = root / 'a.py'
    if operation in {'edit', 'same-metadata'}:
        old = a.stat()
        a.write_text(a.read_text().replace('helper', 'newfun'))
        if operation == 'same-metadata':
            os.utime(a, ns=(old.st_atime_ns, old.st_mtime_ns))
    elif operation == 'touch':
        old = a.stat()
        os.utime(a, ns=(old.st_atime_ns, old.st_mtime_ns + 1000000))
    elif operation == 'rename':
        a.rename(root / 'renamed.py')
    elif operation == 'delete':
        a.unlink()
    elif operation == 'same-bytes':
        (root / 'copy.py').write_bytes(a.read_bytes())
    elif operation == 'config':
        cfg.filters.min_function_lines = 100
    candidate = analyze_incremental(str(root), cache_dir=str(cache), config=cfg, changed_files=['a.py'])
    assert graph(candidate.analysis) == graph(cold(root, cfg))
    for name in ('inventory_seconds', 'hashing_seconds', 'parsing_seconds', 'linking_seconds'):
        assert candidate.incremental[name] >= 0
    if operation == 'touch':
        assert candidate.identity == first.identity
        assert candidate.incremental['analysis_candidates'] == 0
    else:
        assert candidate.identity['snapshot_sha256'] != first.identity['snapshot_sha256']
    if operation in {'rename', 'delete'}:
        assert candidate.incremental['deleted_files'] == ['a.py']


def test_off_policy_never_reads_pickle(project, monkeypatch):
    root, cfg, cache = project
    import pickle
    def refuse(*args, **kwargs):
        raise AssertionError('off policy read a cached pickle')
    monkeypatch.setattr(pickle, 'load', refuse)
    monkeypatch.setattr(pickle, 'loads', refuse)
    result = analyze_incremental(str(root), cache_dir=str(cache), config=cfg, cache_policy='off')
    assert not cache.exists()
    assert graph(result.analysis) == graph(cold(root, cfg))


def test_drift_is_rejected_and_not_advertised_as_atomic(project, monkeypatch):
    root, cfg, cache = project
    from code2llm.core.analyzer import ProjectAnalyzer
    original = ProjectAnalyzer.analyze_project
    def mutate(self, path):
        result = original(self, path)
        (root / 'a.py').write_text('def changed_during_analysis():\n    return 1\n')
        return result
    monkeypatch.setattr(ProjectAnalyzer, 'analyze_project', mutate)
    with pytest.raises(RuntimeError, match='Source changed'):
        analyze_incremental(str(root), cache_dir=str(cache), config=cfg)


@pytest.mark.parametrize('fault', ['inside', 'public', 'hint', 'policy'])
def test_api_refuses_unsafe_cache_and_hint_scope(project, fault):
    root, cfg, cache = project
    args = dict(cache_dir=str(cache), config=cfg)
    if fault == 'inside':
        args['cache_dir'] = str(root / 'cache')
    elif fault == 'public':
        cache.mkdir(mode=0o755)
    elif fault == 'hint':
        args['changed_files'] = ['../outside.py']
    else:
        args['cache_policy'] = 'metadata-only'
    with pytest.raises(ValueError):
        analyze_incremental(str(root), **args)


def test_cycles_are_relinked_after_callee_edit_and_deletion(project):
    root, cfg, cache = project
    (root / 'a.py').write_text('def first():\n    return second()\n')
    (root / 'b.py').write_text('def second():\n    return first()\n')
    initial = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    assert graph(initial.analysis) == graph(cold(root, cfg))
    (root / 'b.py').write_text('def second():\n    return 1\n')
    edited = analyze_incremental(str(root), cache_dir=str(cache), config=cfg, changed_files=[])
    assert edited.incremental['changed_files'] == ['b.py']
    assert graph(edited.analysis) == graph(cold(root, cfg))
    (root / 'b.py').unlink()
    deleted = analyze_incremental(str(root), cache_dir=str(cache), config=cfg, changed_files=[])
    assert graph(deleted.analysis) == graph(cold(root, cfg))


def test_parallel_workers_receive_full_configuration(project):
    root, cfg, cache = project
    for index in range(31):
        (root / ('module' + str(index) + '.py')).write_text('def tiny():\n    return 1\n')
    cfg.filters.min_function_lines = 100
    sequential = cold(root, cfg)
    cfg.performance.parallel_enabled = True
    cfg.performance.parallel_workers = 2
    parallel = cold(root, cfg)
    assert not sequential.functions
    assert graph(parallel) == graph(sequential)


def test_off_and_cached_observations_share_snapshot_identity(project):
    root, cfg, cache = project
    cached = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    uncached = analyze_incremental(str(root), cache_dir=str(cache), config=cfg, cache_policy='off')
    assert cached.identity == uncached.identity


def test_export_cache_follows_the_analysis_namespace(project, tmp_path):
    from code2llm.cli_parser import create_parser
    from code2llm.cli_exports.orchestrator import _run_exports, _try_serve_from_cache
    root, cfg, cache = project
    cfg.persistent_cache_root = str(cache)
    args = create_parser().parse_args([str(root), '-f', 'projections', '-o', str(tmp_path / 'output')])
    output = tmp_path / 'output'
    output.mkdir()
    result = analyze(str(root), cfg)
    _run_exports(args, result, output, root)
    assert _try_serve_from_cache(args, ['projections'], output, root) is True
    (root / 'a.py').write_text('def replacement():\n    return 3\n')
    result = analyze(str(root), cfg)
    args._analysis_cache_context = result.stats['analysis_cache_context']
    assert _try_serve_from_cache(args, ['projections'], output, root) is False


def test_existing_cache_inventory_and_gc_include_configuration_namespaces(project):
    from code2llm.core.persistent_cache import PersistentCache, get_all_projects
    root, cfg, cache = project
    first = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    cfg.filters.min_function_lines = 100
    second = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    assert first.identity['config_sha256'] != second.identity['config_sha256']
    persistent_root = cache / 'persistent'
    projects = get_all_projects(str(persistent_root))
    assert len(projects) == 1
    assert len(projects[0]['analysis_namespaces']) == 2
    assert projects[0]['files_cached'] == 4
    parent = PersistentCache(str(root), cache_root=str(persistent_root), auto_cleanup=False)
    for namespace in parent._project_cache.glob('analysis-*'):
        (namespace / 'files/orphan.pkl').write_bytes(b'not a pickle; never loaded')
    assert parent.gc() == 2
    assert not list(parent._project_cache.glob('analysis-*/files/orphan.pkl'))
    current = analyze_incremental(str(root), cache_dir=str(cache), config=cfg)
    assert current.incremental['cached_files'] == 2
