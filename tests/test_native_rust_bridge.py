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


def test_native_detect_circular_dependencies():
    """Verify Tarjan SCC cycle detection matches expectation without hanging."""
    from code2llm.analysis.native_bridge import native_detect_circular_dependencies

    nodes = ["mod_a", "mod_b", "mod_c", "leaf"]
    edges = [
        ("mod_a", "mod_b"),
        ("mod_b", "mod_c"),
        ("mod_c", "mod_a"),
        ("mod_c", "leaf"),
    ]
    cycles = native_detect_circular_dependencies(nodes, edges)
    assert cycles is not None
    assert len(cycles) == 1
    assert set(cycles[0]) == {"mod_a", "mod_b", "mod_c"}


def test_native_compute_reachability():
    """Verify fast graph reachability marks orphans as unreachable."""
    from code2llm.analysis.native_bridge import native_compute_reachability

    nodes = ["app.main", "app.init", "app.worker", "app.dead_func"]
    edges = [
        ("app.main", "app.init"),
        ("app.main", "app.worker"),
    ]
    entry_points = ["app.main"]

    reach = native_compute_reachability(nodes, edges, entry_points)
    assert reach is not None
    assert reach["app.main"] == "reachable"
    assert reach["app.init"] == "reachable"
    assert reach["app.worker"] == "reachable"
    assert reach["app.dead_func"] == "unreachable"


def test_native_compute_module_coupling():
    """Verify module coupling calculation."""
    from code2llm.analysis.native_bridge import native_compute_module_coupling

    func_modules = [
        ("api.router", "api"),
        ("services.user", "services"),
        ("db.client", "db"),
    ]
    calls = [
        ("api.router", "services.user"),
        ("services.user", "db.client"),
    ]

    res = native_compute_module_coupling(func_modules, calls)
    assert res is not None
    interactions, metrics = res
    assert interactions["api"] == ["services"]
    assert interactions["services"] == ["db"]
    assert interactions["db"] == []

    ca, ce, inst = metrics["services"]
    assert ca == 1  # called by api
    assert ce == 1  # calls db
    assert inst == 0.5


def test_native_walk_project_files(tmp_path):
    """Verify fast native repository file discovery respecting gitignore."""
    from code2llm.analysis.native_bridge import native_walk_project_files

    # Create dummy files
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("def main(): pass")
    (tmp_path / "src" / "helper.ts").write_text("export function help() {}")
    (tmp_path / "ignored").mkdir()
    (tmp_path / "ignored" / "temp.py").write_text("pass")
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "pkg.js").write_text("console.log(1)")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config.py").write_text("pass")

    # .gitignore
    (tmp_path / ".gitignore").write_text("ignored/\n")

    files = native_walk_project_files(
        root=str(tmp_path),
        extensions=[".py", ".ts"],
        filenames=[],
        filename_prefixes=[],
        skip_dirs=["node_modules", ".git"],
        respect_gitignore=True,
    )
    assert files is not None
    file_names = [f[0] for f in files]
    assert any("main.py" in f for f in file_names)
    assert any("helper.ts" in f for f in file_names)
    # ignored directory should be skipped by gitignore
    assert not any("temp.py" in f for f in file_names)
    # node_modules should be skipped by skip_dirs
    assert not any("pkg.js" in f for f in file_names)
    # .git should be skipped
    assert not any("config.py" in f for f in file_names)


def test_native_check_changed_files(tmp_path):
    """Verify fast native parallel cache validation."""
    from code2llm.analysis.native_bridge import native_check_changed_files
    import hashlib

    # Create test files
    f1 = tmp_path / "a.py"
    f1.write_text("print(1)")
    f2 = tmp_path / "b.py"
    f2.write_text("print(2)")

    stat1 = f1.stat()
    stat2 = f2.stat()

    h1 = hashlib.sha256(f"v0.1.0\0{f1}\0print(1)".encode()).hexdigest()[:16]
    h2 = hashlib.sha256(f"v0.1.0\0{f2}\0print(2)".encode()).hexdigest()[:16]

    manifest = {
        "a.py": (h1, stat1.st_mtime, stat1.st_size),
        # b.py has drifted mtime, triggering L2 check where hash mismatches
        "b.py": ("wronghash1234567", stat2.st_mtime + 10.0, stat2.st_size),
    }

    res = native_check_changed_files(
        project_dir=str(tmp_path),
        filepaths=[str(f1), str(f2)],
        manifest_entries=manifest,
        analyzer_version="0.1.0",
    )
    assert res is not None
    changed, cached, refreshed = res
    assert str(f1) in cached
    assert str(f2) in changed


def test_native_format_toon_header():
    """Verify native TOON header formatting."""
    from code2llm.analysis.native_bridge import native_format_toon_header

    lines = native_format_toon_header(
        nfiles=42,
        total_lines=1337,
        lang_label="Python",
        timestamp="2026-10-02 23:00",
        avg_cc=3.14,
        critical_cc=5,
        total_funcs=100,
        dups=2,
        cycles=1,
    )
    assert lines is not None
    assert len(lines) == 2
    assert "42f 1337L" in lines[0]
    assert "critical:5/100" in lines[1]


def test_native_resolve_call_graph():
    """Verify native call graph resolution and entry points finding."""
    from code2llm.analysis.native_bridge import native_resolve_call_graph

    func_calls = [
        ("app.cli.run", ["parse_args", "app.core.execute"]),
        ("app.cli.parse_args", []),
        ("app.core.execute", ["db.connect"]),
        ("db.connect", []),
    ]

    res = native_resolve_call_graph(func_calls)
    assert res is not None
    resolved_calls, called_by, entry_points = res

    # parse_args should be resolved to app.cli.parse_args
    assert resolved_calls["app.cli.run"] == ["app.cli.parse_args", "app.core.execute"]
    assert "app.cli.run" in called_by["app.cli.parse_args"]
    assert "app.cli.run" in called_by["app.core.execute"]
    assert "app.core.execute" in called_by["db.connect"]

    # Entry point is only app.cli.run
    assert entry_points == ["app.cli.run"]


def test_native_find_pipeline_paths():
    """Verify native pipeline path finding."""
    from code2llm.analysis.native_bridge import native_find_pipeline_paths

    nodes = ["step1", "step2", "step3", "step4", "unrelated"]
    edges = [("step1", "step2"), ("step2", "step3"), ("step3", "step4")]

    paths = native_find_pipeline_paths(nodes, edges, min_length=3, max_pipelines=5)
    assert paths is not None
    assert len(paths) >= 1
    assert paths[0] == ["step1", "step2", "step3", "step4"]


def test_native_calculate_call_metrics():
    """Verify native call metrics calculation."""
    from code2llm.analysis.native_bridge import native_calculate_call_metrics

    functions = [
        ("caller", ["callee"], [], 3.0),
        ("callee", [], [], 2.0),
    ]

    res = native_calculate_call_metrics(functions)
    assert res is not None
    metrics, called_by = res
    assert metrics["caller"] == (0, 1, 3.0)
    assert metrics["callee"] == (1, 0, 2.0)
    assert called_by["callee"] == ["caller"]




