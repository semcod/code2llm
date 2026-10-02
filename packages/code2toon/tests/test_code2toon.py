"""Tests for code2toon parser, validator, and diff engine."""
import pytest
from code2toon import (
    parse_toon_content,
    validate_toon,
    diff_toon,
    ToonDocument,
    ToonHeader,
    FunctionEntry,
    is_toon_file,
)


SAMPLE_TOON = """# myproject | 2026-10-03
# CC̄=3.5 | critical: 2 | dups: 1 | cycles: 0

HEALTH[2]:
  🔴 God function in core.py:42
  🟡 High coupling in api.py:10

FUNCTIONS[2]:
  12.0 core.heavy_calc
  2.0  core.helper

CLASSES[2]:
  CoreConfig
  HelperService

HOTSPOTS[1]:
  # 5 calls from core.heavy_calc
"""


def test_is_toon_file(tmp_path):
    toon_file = tmp_path / "analysis.toon"
    toon_file.write_text(SAMPLE_TOON)
    assert is_toon_file(toon_file)
    assert is_toon_file(str(toon_file))

    py_file = tmp_path / "sample.py"
    py_file.write_text("print('hello')")
    assert not is_toon_file(py_file)


def test_parse_toon_content():
    data = parse_toon_content(SAMPLE_TOON)
    assert data["meta"]["project"] == "myproject"
    assert data["stats"]["critical"] == "2"
    assert data["stats"]["duplicates"] == "1"
    assert len(data["health"]) == 2
    assert len(data["functions"]) == 2
    assert data["functions"][0]["name"] == "core.heavy_calc"
    assert data["functions"][0]["cc"] == 12.0
    assert len(data["classes"]) == 2
    assert len(data["hotspots"]) == 1


def test_validate_toon():
    data = parse_toon_content(SAMPLE_TOON)
    valid, errors = validate_toon(data)
    assert valid
    assert len(errors) == 0

    invalid_data = {"meta": {}}
    valid, errors = validate_toon(invalid_data)
    assert not valid
    assert len(errors) > 0


def test_diff_toon():
    doc1 = ToonDocument(
        header=ToonHeader(project="myproject", mean_cc=3.5),
        functions=[FunctionEntry(name="foo", cc=4.0), FunctionEntry(name="bar", cc=2.0)],
        classes=["FooClass"],
        health=["🔴 Old Issue"],
    )
    doc2 = ToonDocument(
        header=ToonHeader(project="myproject", mean_cc=2.5),
        functions=[FunctionEntry(name="foo", cc=2.0), FunctionEntry(name="baz", cc=1.0)],
        classes=["FooClass", "BazClass"],
        health=["🟡 New Issue"],
    )

    diff = diff_toon(doc1, doc2)
    assert diff.has_drift
    assert diff.cc_delta == -1.0
    assert diff.added_functions == ["baz"]
    assert diff.removed_functions == ["bar"]
    assert diff.added_classes == ["BazClass"]
    assert diff.added_health_issues == ["🟡 New Issue"]
    assert diff.resolved_health_issues == ["🔴 Old Issue"]
