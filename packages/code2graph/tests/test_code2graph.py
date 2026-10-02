"""Tests for code2graph data models and queries."""

from code2graph import (
    AnalysisResult,
    FunctionInfo,
    ClassInfo,
    ModuleInfo,
    FlowNode,
    FlowEdge,
    GraphQuery,
)


def test_models_serialization():
    result = AnalysisResult(project_path="/tmp/test")
    fn = FunctionInfo(
        name="test_func",
        qualified_name="pkg.mod.test_func",
        file="pkg/mod.py",
        line=10,
        calls=["pkg.mod.helper"],
    )
    result.functions[fn.qualified_name] = fn

    d = result.to_dict(compact=True)
    assert d["project_path"] == "/tmp/test"
    assert "pkg.mod.test_func" in d["functions"]
    assert d["functions"]["pkg.mod.test_func"]["name"] == "test_func"


def test_graph_query():
    result = AnalysisResult()
    f1 = FunctionInfo(name="main", qualified_name="app.main", file="app.py", line=1, calls=["app.worker"])
    f2 = FunctionInfo(name="worker", qualified_name="app.worker", file="app.py", line=10, called_by=["app.main"])
    result.functions["app.main"] = f1
    result.functions["app.worker"] = f2

    query = GraphQuery(result)
    assert query.get_callees("app.main") == ["app.worker"]
    assert query.get_callers("app.worker") == ["app.main"]
    assert query.get_entry_points() == ["app.main"]
    assert query.find_reachable(["app.main"]) == {"app.main", "app.worker"}
