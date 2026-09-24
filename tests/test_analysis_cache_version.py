"""Upgrading the analyzer must not reuse previous parser metrics or exports."""

import hashlib
import json
import os
import pickle

import pytest

from code2llm.core import file_cache, persistent_cache


@pytest.mark.parametrize("persistent", [False, True])
def test_distinct_source_paths_keep_their_own_cached_module_identity(tmp_path, persistent):
    first = tmp_path / "a" / "index.js"
    second = tmp_path / "b" / "index.js"
    for source in (first, second):
        source.parent.mkdir()
        source.write_text("const f=()=>true;")
        os.utime(source, ns=(1_700_000_000_000_000_000, 1_700_000_000_000_000_000))
    if persistent:
        cache = persistent_cache.PersistentCache(
            str(tmp_path), str(tmp_path / "cache"), auto_cleanup=False
        )
        get, put = cache.get_file_result, cache.put_file_result
    else:
        cache = file_cache.FileCache(str(tmp_path / "cache"))
        get, put = cache.get_fast, cache.put_fast
    put(str(first), {"module": "a.index"})
    assert get(str(second)) is None
    put(str(second), {"module": "b.index"})
    assert get(str(first)) == {"module": "a.index"}
    assert get(str(second)) == {"module": "b.index"}
    assert file_cache.make_cache_key(str(first), first.read_text()) != file_cache.make_cache_key(
        str(second), second.read_text()
    )


@pytest.mark.parametrize("fast", [False, True])
def test_file_cache_rejects_legacy_and_previous_version(tmp_path, monkeypatch, fast):
    source = tmp_path / "fixture.js"
    source.write_text("let pending=null; const pick=()=>true;")
    cache_dir = tmp_path / "cache"
    current = file_cache.FileCache(str(cache_dir))
    stat = source.stat()
    legacy = cache_dir / f"fixture_{stat.st_mtime_ns}_{stat.st_size}.pkl"
    legacy.write_bytes(pickle.dumps({"wrong": "pending"}))

    def get(cache):
        return cache.get_fast(str(source)) if fast else cache.get(str(source), source.read_text())

    def put(cache, value):
        if fast:
            cache.put_fast(str(source), value)
        else:
            cache.put(str(source), source.read_text(), value)

    assert get(current) is None
    put(current, {"old_version": True})
    assert get(current) == {"old_version": True}
    old_key = file_cache.make_cache_key(str(source), source.read_text())
    monkeypatch.setattr(file_cache, "__version__", "future-analyzer")
    upgraded = file_cache.FileCache(str(cache_dir))
    assert get(upgraded) is None
    assert file_cache.make_cache_key(str(source), source.read_text()) != old_key
    put(upgraded, {"correct": "pick"})
    assert get(upgraded) == {"correct": "pick"}


def test_persistent_cache_rejects_legacy_results_and_exports(tmp_path):
    source = tmp_path / "fixture.js"
    source.write_text("let pending=null; const pick=()=>true;")
    root = tmp_path / "cache"
    cache = persistent_cache.PersistentCache(str(tmp_path), str(root), auto_cleanup=False)
    legacy_hash = hashlib.sha256(source.read_bytes()).hexdigest()[:16]
    (cache._files_dir / f"{legacy_hash}.pkl").write_bytes(pickle.dumps({"wrong": "pending"}))
    stat = source.stat()
    files = {source.name: {"hash": legacy_hash, "mtime": stat.st_mtime, "size": stat.st_size}}
    cache._manifest_path.write_text(
        json.dumps({"version": persistent_cache.VERSION, "files": files})
    )
    manifest_hash = hashlib.md5(json.dumps(files, sort_keys=True).encode()).hexdigest()[:12]
    config_hash = hashlib.md5(b"{}").hexdigest()[:8]
    legacy_export = cache._exports_dir / f"{manifest_hash}_{config_hash}"
    legacy_export.mkdir()
    cache.mark_export_complete(legacy_export)

    upgraded = persistent_cache.PersistentCache(str(tmp_path), str(root), auto_cleanup=False)
    assert upgraded.get_changed_files([str(source)]) == ([str(source)], [])
    assert upgraded.get_file_result(str(source)) is None
    assert upgraded.get_export_cache_dir({}) is None
    upgraded.put_file_result(str(source), {"correct": "pick"})
    # Repopulating the manifest must still not resurrect a legacy export.
    assert upgraded.get_export_cache_dir({}) is None
    assert upgraded.get_file_result(str(source)) == {"correct": "pick"}


def test_persistent_cache_version_upgrade_keeps_current_cache_hits(tmp_path, monkeypatch):
    source = tmp_path / "fixture.js"
    source.write_text("const pick=()=>true;")
    root = tmp_path / "cache"

    def open_cache():
        return persistent_cache.PersistentCache(str(tmp_path), str(root), auto_cleanup=False)

    previous = open_cache()
    previous.put_file_result(str(source), {"old_version": True})
    previous.mark_export_complete(previous.create_export_cache_dir({}))
    previous.save()
    monkeypatch.setattr(persistent_cache, "__version__", "future-analyzer")
    current = open_cache()
    assert current.get_changed_files([str(source)]) == ([str(source)], [])
    assert current.get_file_result(str(source)) is None
    current.put_file_result(str(source), {"correct": "pick"})
    assert current.get_export_cache_dir({}) is None
    export = current.create_export_cache_dir({})
    current.mark_export_complete(export)
    current.save()
    reopened = open_cache()
    assert reopened.get_changed_files([str(source)]) == ([], [str(source)])
    assert reopened.get_file_result(str(source)) == {"correct": "pick"}
    assert reopened.get_export_cache_dir({}) == export
