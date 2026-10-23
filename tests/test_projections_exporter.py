"""Contract tests for the bounded intent-retrieval projection (PLF-035 / #25).

The projection is a reuse contract consumed by external indexers
(semcod/search): determinism, provenance, bounds and version stamping
are load-bearing, not incidental.
"""
from pathlib import Path
from types import SimpleNamespace

import pytest

from code2llm import __version__
from code2llm.exporters.projections_exporter import (
    FIELD_LIMIT,
    MAX_RECORDS,
    PROJECTION_SCHEMA,
    ProjectionsExporter,
    build_projection,
)


def _fake_result(modules=(), classes=(), functions=(), stats=None, path="proj", mode="standard"):
    def mod(name, file):
        return SimpleNamespace(name=name, file=file)

    def cls(name, file, line):
        return SimpleNamespace(name=name, qualified_name=f"mod.{name}", file=file, line=line)

    def fn(name, file, line):
        return SimpleNamespace(name=name, qualified_name=f"mod.{name}", file=file, line=line)

    return SimpleNamespace(
        modules=[mod(*m) for m in modules],
        classes=[cls(*c) for c in classes],
        functions=[fn(*f) for f in functions],
        stats=stats or {"files": 3, "lines": 100},
        project_path=path,
        analysis_mode=mode,
    )


def test_schema_and_producer_version_are_pinned():
    doc = build_projection(_fake_result())
    assert doc["schema"] == PROJECTION_SCHEMA
    assert doc["producer"] == {"tool": "code2llm", "version": __version__}


def test_records_carry_source_and_symbol_provenance():
    doc = build_projection(
        _fake_result(
            modules=[("core", "pkg/core/__init__.py")],
            classes=[("Engine", "pkg/core/engine.py", 12)],
            functions=[("run", "pkg/core/engine.py", 40)],
        )
    )
    by_kind = {r["kind"]: r for r in doc["records"]}
    assert by_kind["module"] == {
        "kind": "module",
        "symbol": "core",
        "file": "pkg/core/__init__.py",
        "digest": by_kind["module"]["digest"],
    }
    assert by_kind["class"]["symbol"] == "mod.Engine"
    assert by_kind["class"]["file"] == "pkg/core/engine.py"
    assert by_kind["class"]["line"] == 12
    assert by_kind["function"]["line"] == 40
    assert all(r["digest"].startswith("sha256:") for r in doc["records"])


def test_deterministic_bytes_and_digest():
    result = _fake_result(
        classes=[("B", "b.py", 2), ("A", "a.py", 1)],
        functions=[("z", "a.py", 9), ("a", "b.py", 1)],
    )
    first = build_projection(result)
    second = build_projection(result)
    assert first == second
    assert first["digest"] == second["digest"]
    # Record order is canonical: (file, line, kind, symbol).
    order = [(r["file"], r.get("line", 0), r["kind"], r["symbol"]) for r in first["records"]]
    assert order == sorted(order)
    # generated_at never leaks into the digest.
    stamped = build_projection(result, generated_at="2026-10-23T00:00:00Z")
    assert stamped["digest"] == first["digest"]


def test_bounds_cap_records_and_flag_truncation():
    functions = [(f"f{i}", "m.py", i + 1) for i in range(MAX_RECORDS + 5)]
    doc = build_projection(_fake_result(functions=functions))
    assert len(doc["records"]) == MAX_RECORDS
    assert doc["stats"]["truncated"] is True
    assert doc["stats"]["symbols"] == MAX_RECORDS
    small = build_projection(_fake_result(functions=functions[:4]))
    assert small["stats"]["truncated"] is False


def test_long_fields_are_truncated():
    long_name = "x" * (FIELD_LIMIT + 50)
    doc = build_projection(_fake_result(functions=[(long_name, long_name + ".py", 1)]))
    record = doc["records"][0]
    assert len(record["symbol"]) == FIELD_LIMIT
    assert len(record["file"]) == FIELD_LIMIT


def test_exporter_writes_canonical_json(tmp_path: Path):
    result = _fake_result(classes=[("E", "e.py", 3)])
    exporter = ProjectionsExporter()
    out = tmp_path / "projections.json"
    path = exporter.export(result, str(out))
    assert path == out and out.exists()
    body = out.read_text(encoding="utf-8")
    again = exporter.export(result, str(tmp_path / "again.json"))
    assert again.read_text(encoding="utf-8") == body
    assert body.endswith("\n")


def test_registry_lists_projections():
    from code2llm.exporters import EXPORT_REGISTRY, get_exporter

    assert "projections" in EXPORT_REGISTRY
    assert get_exporter("projections") is ProjectionsExporter


def test_cli_help_mentions_projections(capsys):
    from code2llm.cli_parser import create_parser

    with pytest.raises(SystemExit) as exc:
        create_parser().parse_args(["--help"])
    assert exc.value.code == 0
    assert "projections" in (capsys.readouterr().out or "")
