"""Unit tests for code2flow exporters and validation."""
from code2graph import AnalysisResult, FunctionInfo
from code2flow import (
    export_flow_compact,
    export_calls,
    validate_mermaid_file,
    fix_mermaid_file,
)


def test_export_flow_compact(tmp_path):
    result = AnalysisResult()
    result.functions = {
        "app.main": FunctionInfo(name="main", qualified_name="app.main", file="app.py", line=1, calls=["app.worker"]),
        "app.worker": FunctionInfo(name="worker", qualified_name="app.worker", file="app.py", line=10, called_by=["app.main"]),
    }
    out_file = tmp_path / "compact_flow.mmd"
    export_flow_compact(result, str(out_file))

    assert out_file.exists()
    content = out_file.read_text()
    assert "graph TD" in content or "flowchart" in content or "subgraph" in content


def test_export_calls(tmp_path):
    result = AnalysisResult()
    result.functions = {
        "app.main": FunctionInfo(name="main", qualified_name="app.main", file="app.py", line=1, calls=["app.worker"]),
        "app.worker": FunctionInfo(name="worker", qualified_name="app.worker", file="app.py", line=10, called_by=["app.main"]),
    }
    out_file = tmp_path / "calls.mmd"
    export_calls(result, str(out_file))

    assert out_file.exists()
    content = out_file.read_text()
    assert "flowchart" in content or "graph" in content


def test_validate_and_fix_mermaid(tmp_path):
    mmd_file = tmp_path / "test.mmd"
    mmd_file.write_text("graph TD\n    A -->|bad_label(| B\n")
    errors = validate_mermaid_file(str(mmd_file))
    assert isinstance(errors, list)

    fixed = fix_mermaid_file(str(mmd_file))
    assert fixed is True
    assert "bad_label" in mmd_file.read_text()
