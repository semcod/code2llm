"""End-to-end tests for cache invalidation across the full analyze→export pipeline.

These pin the contract that the user cares about:
  - Modifying a file triggers re-analysis of that file and a fresh export.
  - Deleting a file shrinks the manifest and invalidates the export cache.
  - Running twice with no changes is a full cache hit.
"""

from pathlib import Path

import pytest

from code2llm.core.analyzer import ProjectAnalyzer
from code2llm.core.config import Config, analysis_config_digest
from code2llm.core.persistent_cache import PersistentCache


@pytest.fixture()
def project(tmp_path, monkeypatch):
    """A tiny python project with its own PersistentCache root."""
    (tmp_path / "project").mkdir()
    (tmp_path / "project" / "a.py").write_text("def foo():\n    return 1\n")
    (tmp_path / "project" / "b.py").write_text("def bar():\n    return 2\n")
    # Redirect ~/.code2llm so tests don't touch real user cache.
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setenv("HOME", str(fake_home))
    # persistent_cache._DEFAULT_ROOT is captured at import time, so we
    # have to reach into PersistentCache and override its root explicitly
    # via a subclass-free patch.
    return tmp_path / "project", fake_home / ".code2llm"


def _analysis_config(project_dir: Path, root: Path):
    cfg = Config(output_dir=str(project_dir.parent / "out"), persistent_cache_root=str(root))
    cfg.performance.parallel_enabled = False
    cfg.performance.cache_dir = str(root / "file-cache")
    return cfg


def _cache_for(project_dir: Path, root: Path) -> PersistentCache:
    return PersistentCache(str(project_dir), cache_root=str(root),
                           analysis_identity=analysis_config_digest(_analysis_config(project_dir, root)))


def _run_full_analysis(project_dir: Path, cache_root: Path):
    """Use the explicit cache configuration instead of replacing its constructor."""
    return ProjectAnalyzer(_analysis_config(project_dir, cache_root), project_dir).analyze_project(str(project_dir))


def test_first_run_populates_manifest(project):
    project_dir, cache_root = project
    _run_full_analysis(project_dir, cache_root)
    pc = _cache_for(project_dir, cache_root)
    assert "a.py" in pc._manifest["files"], (
        "after first run the manifest must contain per-file entries "
        "(regression for analyze_file not tagging 'file' key)"
    )
    assert "b.py" in pc._manifest["files"]


def test_run_hash_changes_when_file_modified(project):
    project_dir, cache_root = project
    _run_full_analysis(project_dir, cache_root)
    pc1 = _cache_for(project_dir, cache_root)
    h1 = pc1._compute_run_hash({"fmt": "toon"})

    # Modify a.py
    (project_dir / "a.py").write_text("def foo():\n    return 42\n")
    _run_full_analysis(project_dir, cache_root)

    pc2 = _cache_for(project_dir, cache_root)
    h2 = pc2._compute_run_hash({"fmt": "toon"})
    assert h1 != h2, "modifying a file must change the export-cache run hash"


def test_run_hash_changes_when_file_deleted(project):
    project_dir, cache_root = project
    _run_full_analysis(project_dir, cache_root)
    pc1 = _cache_for(project_dir, cache_root)
    h1 = pc1._compute_run_hash({"fmt": "toon"})

    # Delete b.py
    (project_dir / "b.py").unlink()
    _run_full_analysis(project_dir, cache_root)

    pc2 = _cache_for(project_dir, cache_root)
    assert "b.py" not in pc2._manifest["files"], (
        "deleted files must be pruned from manifest"
    )
    h2 = pc2._compute_run_hash({"fmt": "toon"})
    assert h1 != h2, "deleting a file must change the export-cache run hash"


def test_run_hash_stable_when_nothing_changes(project):
    project_dir, cache_root = project
    _run_full_analysis(project_dir, cache_root)
    pc1 = _cache_for(project_dir, cache_root)
    h1 = pc1._compute_run_hash({"fmt": "toon"})

    _run_full_analysis(project_dir, cache_root)

    pc2 = _cache_for(project_dir, cache_root)
    h2 = pc2._compute_run_hash({"fmt": "toon"})
    assert h1 == h2, (
        "identical project state must yield identical run hash (full cache hit)"
    )
