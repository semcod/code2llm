"""Regression test: export cache must not clobber foreign artifacts.

The export-level cache used to snapshot the ENTIRE output directory via
``_copy_to_cache`` — including foreign-tool artifacts that merely live there
(redup → duplication.toon.yaml, vallm → validation.toon.yaml) — and restore
that snapshot on every cache hit via ``_copy_cached_export``, silently
reverting newer external exports (PLF-211: fresh 2026-09-20 redup export
reverted to a stale 2026-06-16 copy on every run).

Both directions are now restricted to code2llm-owned artifact names, so:
  - foreign files never enter the cache, and
  - legacy cache entries that already contain foreign snapshots cannot
    overwrite live foreign exports in the output directory.
"""

import os
import time
from pathlib import Path

from code2llm.cli_exports.orchestrator import (
    _copy_cached_export,
    _copy_to_cache,
)
from code2llm.cli_exports.orchestrator_constants import is_cacheable_export_name

FOREIGN = "# redup/duplication | 0 groups | 17f 3213L | 2026-09-20\nfresh\n"
FOREIGN_STALE = "# redup/duplication | 2 groups | 19f 2883L | 2026-06-16\nstale\n"


def test_copy_to_cache_skips_foreign_files(tmp_path: Path) -> None:
    output_dir = tmp_path / "out"
    cache_dir = tmp_path / "cache"
    output_dir.mkdir(parents=True)

    (output_dir / "analysis.toon.yaml").write_text("x: 1\n", encoding="utf-8")
    (output_dir / "prompt.txt").write_text("prompt\n", encoding="utf-8")
    (output_dir / "duplication.toon.yaml").write_text(FOREIGN, encoding="utf-8")
    (output_dir / "validation.toon.yaml").write_text("foreign\n", encoding="utf-8")
    (output_dir / "mermaid.export").write_text("foreign\n", encoding="utf-8")

    _copy_to_cache(output_dir, cache_dir, verbose=False)

    assert (cache_dir / "analysis.toon.yaml").exists()
    assert (cache_dir / "prompt.txt").exists()
    assert not (cache_dir / "duplication.toon.yaml").exists()
    assert not (cache_dir / "validation.toon.yaml").exists()
    assert not (cache_dir / "mermaid.export").exists()


def test_copy_cached_export_never_overwrites_foreign_file(tmp_path: Path) -> None:
    """Legacy cache entry carries a stale foreign snapshot — must be inert."""
    cache_dir = tmp_path / "cache"
    output_dir = tmp_path / "out"

    # Simulate a pre-fix cache entry: owned exports + foreign snapshot.
    cache_dir.mkdir(parents=True)
    (cache_dir / "analysis.toon.yaml").write_text("cached\n", encoding="utf-8")
    (cache_dir / "duplication.toon.yaml").write_text(FOREIGN_STALE, encoding="utf-8")

    # Live output dir with a newer foreign export.
    output_dir.mkdir(parents=True)
    foreign_path = output_dir / "duplication.toon.yaml"
    foreign_path.write_text(FOREIGN, encoding="utf-8")
    stale_mtime = time.time() - 60 * 60 * 24 * 90  # 90 days ago
    os.utime(foreign_path, (stale_mtime, stale_mtime))

    _copy_cached_export(cache_dir, output_dir, verbose=False)

    assert foreign_path.read_text(encoding="utf-8") == FOREIGN, (
        "cache restore reverted the foreign redup export to its stale snapshot"
    )
    # Owned artifact is still restored normally.
    assert (output_dir / "analysis.toon.yaml").read_text(encoding="utf-8") == "cached\n"
    # The foreign file was not even touched (mtime preserved).
    assert foreign_path.stat().st_mtime == stale_mtime


def test_roundtrip_preserves_owned_and_foreign_artifacts(tmp_path: Path) -> None:
    """End-to-end: save → mutate foreign file → restore leaves it alone."""
    output_dir = tmp_path / "out"
    cache_dir = tmp_path / "cache"
    output_dir.mkdir(parents=True)

    (output_dir / "map.toon.yaml").write_text("map v1\n", encoding="utf-8")
    (output_dir / "duplication.toon.yaml").write_text(FOREIGN, encoding="utf-8")

    _copy_to_cache(output_dir, cache_dir, verbose=False)

    # Foreign tool writes a newer export; owned file changes owner-side too.
    (output_dir / "duplication.toon.yaml").write_text(
        "# redup/duplication | 1 group | 18f 3300L | 2026-09-21\nnewer\n",
        encoding="utf-8",
    )
    (output_dir / "map.toon.yaml").unlink()

    _copy_cached_export(cache_dir, output_dir, verbose=False)

    assert (output_dir / "map.toon.yaml").read_text(encoding="utf-8") == "map v1\n"
    assert "2026-09-21" in (output_dir / "duplication.toon.yaml").read_text(
        encoding="utf-8"
    )


def test_cacheable_names_cover_code2llm_outputs() -> None:
    owned = [
        "analysis.toon.yaml",
        "analysis.toon",
        "analysis.yaml",
        "analysis.json",
        "map.toon.yaml",
        "flow.toon.yaml",
        "evolution.toon.yaml",
        "planfile-tickets.yaml",
        "context.md",
        "README.md",
        "project.yaml",
        "project.toon.yaml",
        "project.toon",
        "project_part2.toon",
        "prompt.txt",
        "index.html",
        "flow.mmd",
        "compact_flow.mmd",
        "calls.yaml",
        "calls.toon.yaml",
        "flow.png",
        "data_structures.yaml",
        "prompts",
        "separated",
        "split",
    ]
    for name in owned:
        assert is_cacheable_export_name(name), f"{name} should be cacheable"

    foreign = [
        "duplication.toon.yaml",
        "validation.toon.yaml",
        "mermaid.export",
        "foreign_report.yaml",
        "notes.md",
    ]
    for name in foreign:
        assert not is_cacheable_export_name(name), f"{name} must not be cacheable"
