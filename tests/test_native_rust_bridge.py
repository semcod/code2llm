"""Unit and contract tests for code2llm native Rust acceleration bridge."""

import pytest
import networkx as nx
from code2llm.analysis.native_bridge import (
    is_native_rust_available,
    get_native_version,
    native_extract_function_body,
    native_calculate_complexity,
    native_batch_complexity,
    native_extract_calls,
    native_batch_calls,
    native_betweenness_centrality,
    native_detect_god_functions,
    native_detect_data_clumps,
)
from code2llm.analysis.complexity import (
    calculate_complexity_regex,
    estimate_function_complexity,
    compute_cyclomatic_complexity,
)
from code2llm.core.models import FunctionInfo


def test_native_rust_available():
    """Verify code2llm-rust C-extension is detected and version is resolved."""
    assert is_native_rust_available() is True
    assert get_native_version() == "0.1.0"


def test_native_extract_function_body():
    """Test native function body extraction between braces."""
    code = "function test() {\n    let a = 1;\n    return a + 2;\n}\nfunction next() {}"
    body = native_extract_function_body(code, 1)
    assert body is not None
    assert "return a + 2;" in body
    assert "function next" not in body


def test_native_calculate_complexity():
    """Verify exact match of complexity calculation between native Rust and Python regex."""
    body = """
    function compute(a, b) {
        if (a > 0 && b > 0) {
            while (a < 10) {
                a++;
            }
        } else if (a < 0 || b < 0) {
            switch (b) {
                case 1: return a;
                default: break;
            }
        }
        return a + b;
    }
    """
    native_cc, native_rank = native_calculate_complexity(body, "c_family")
    py_cc = compute_cyclomatic_complexity(body, "c_family")

    assert native_cc == py_cc
    assert native_rank in ("A", "B", "C", "D")


def test_native_batch_complexity():
    """Verify batch complexity computation across multiple line starts."""
    content = "fn one() { if (x) {} }\nfn two() { while (y) { if (z) {} } }"
    res = native_batch_complexity(content, [1, 2], "rust")
    assert res is not None
    assert 1 in res
    assert 2 in res
    assert res[1][0] == 2
    assert res[2][0] == 3


def test_native_extract_calls():
    """Verify fast native call extraction."""
    body = "function run() { this.render(); service.fetchData(); log(); if (ok) { next(); } }"
    calls = native_extract_calls(body)
    assert calls is not None
    assert "render" in calls
    assert "fetchData" in calls
    assert "log" in calls
    assert "next" in calls
    assert "if" not in calls


def test_native_batch_calls():
    """Verify batch call extraction across multiple lines."""
    content = "function a() { foo(); }\nfunction b() { bar(); baz(); }"
    res = native_batch_calls(content, [1, 2])
    assert res is not None
    assert 1 in res
    assert "foo" in res[1]
    assert 2 in res
    assert "bar" in res[2]
    assert "baz" in res[2]


def test_native_betweenness_centrality_vs_networkx():
    """Verify Brandes algorithm matches NetworkX betweenness centrality."""
    nodes = ["A", "B", "C", "D", "E"]
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")]

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    nx_cb = nx.betweenness_centrality(G)
    rust_cb = native_betweenness_centrality(nodes, edges, normalized=True)

    assert rust_cb is not None
    for n in nodes:
        assert abs(rust_cb[n] - nx_cb[n]) < 1e-5


def test_native_detect_god_functions():
    """Verify native smell candidate detection."""
    fn_tuples = [
        ("app.normal", "app.py", 10, 2, 1, 3),
        ("app.god", "app.py", 50, 20, 10, 25),
    ]
    res = native_detect_god_functions(fn_tuples)
    assert res is not None
    assert len(res) == 1
    assert res[0][0] == "app.god"
    assert res[0][6] > 0.8  # high severity


def test_native_detect_data_clumps():
    """Verify native parameter clump detection."""
    func_params = [
        ("f1", ["req", "res", "ctx", "span"]),
        ("f2", ["req", "res", "ctx", "logger"]),
        ("f3", ["req", "res", "ctx"]),
    ]
    clumps = native_detect_data_clumps(func_params, min_size=3, min_occurrences=2)
    assert clumps is not None
    assert len(clumps) == 1
    params, funcs = clumps[0]
    assert set(params) == {"req", "res", "ctx"}
    assert len(funcs) == 3
