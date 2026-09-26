"""Unit tests for the atomized complexity engine (code2llm.analysis.complexity)."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

from code2llm.analysis.complexity import (
    _find_rust_binary,
    _rust_batch_complexity,
    calculate_complexity_regex,
    calculate_python_complexity,
    compute_cc_rank,
    compute_cyclomatic_complexity,
    estimate_function_complexity,
    extract_function_body,
)


def test_extract_function_body_nested_braces() -> None:
    code = """
void outer() {
    if (true) {
        doSomething();
    }
}

void another() {
    return;
}
"""
    body = extract_function_body(code, 2)
    assert "void outer() {" in body
    assert "doSomething();" in body
    assert "void another()" not in body


def test_extract_function_body_out_of_bounds() -> None:
    assert extract_function_body("foo", 0) == ""
    assert extract_function_body("foo", 100) == ""


def test_compute_cc_rank() -> None:
    assert compute_cc_rank(1) == "A"
    assert compute_cc_rank(5) == "A"
    assert compute_cc_rank(6) == "B"
    assert compute_cc_rank(10) == "B"
    assert compute_cc_rank(11) == "C"
    assert compute_cc_rank(20) == "C"
    assert compute_cc_rank(21) == "D"
    assert compute_cc_rank(50) == "D"


def test_compute_cyclomatic_complexity_c_family() -> None:
    body = """
{
    if (a && b) {
        while (c) {
            val = x ? y : z;
        }
    } else if (d || e) {
        switch (k) {
            case 1: break;
        }
    }
}
"""
    # if (1) + && (1) + while (1) + ? : (1) + else if (1) + || (1) + switch (1) + case (1) = 8 + 1 = 9
    cc = compute_cyclomatic_complexity(body, lang="c_family")
    assert cc == 9


def test_compute_cyclomatic_complexity_go() -> None:
    body = """
{
    if err != nil {
        return err
    }
    for i := 0; i < 10; i++ {
        select {
        case <-ch:
            go worker()
            defer cleanup()
        }
    }
}
"""
    # if(1) + for(1) + select(1) + case(1) + go(1) + defer(1) = 6 + 1 = 7
    cc = compute_cyclomatic_complexity(body, lang="go")
    assert cc == 7


def test_compute_cyclomatic_complexity_rust() -> None:
    body = """
{
    if let Some(x) = opt {
        match x {
            1 => loop { break; },
            _ => while running { work()?; },
        }
    }
}
"""
    # if(1) + match(1) + loop(1) + while(1) + ?(1) = 5 + 1 = 6
    cc = compute_cyclomatic_complexity(body, lang="rust")
    assert cc == 6


def test_calculate_complexity_regex_populates_result() -> None:
    code = """
function testA() {
    if (x > 0 && y > 0) {
        return 1;
    }
    return 0;
}

function testB() {
    return 42;
}
"""
    func_a = MagicMock()
    func_a.line = 2
    func_b = MagicMock()
    func_b.line = 9

    result: dict[str, Any] = {
        "functions": {
            "testA": func_a,
            "testB": func_b,
        }
    }

    calculate_complexity_regex(code, result, lang="c_family")

    assert func_a.complexity["cyclomatic_complexity"] >= 3  # if + && + 1
    assert func_a.complexity["cc_rank"] == "A"
    assert func_b.complexity["cyclomatic_complexity"] == 1
    assert func_b.complexity["cc_rank"] == "A"


def test_rust_batch_complexity_consistency() -> None:
    rust_bin = _find_rust_binary()
    if not rust_bin:
        return

    code = """
void foo() {
    if (a && b) {
        doSomething();
    }
}

void bar() {
    return;
}
"""
    rust_res = _rust_batch_complexity(lines=[2, 8], lang="c_family", content=code)
    assert rust_res is not None
    assert 2 in rust_res
    assert 8 in rust_res

    py_cc_foo, py_rank_foo = estimate_function_complexity(code, 2, lang="c_family")
    py_cc_bar, py_rank_bar = estimate_function_complexity(code, 8, lang="c_family")

    assert rust_res[2] == (py_cc_foo, py_rank_foo)
    assert rust_res[8] == (py_cc_bar, py_rank_bar)


def test_calculate_python_complexity() -> None:
    py_code = """
def complex_fn(a, b):
    if a > 0:
        if b > 0:
            return a + b
    return 0

class MyService:
    def simple_method(self):
        return 1
"""
    func1 = MagicMock()
    func2 = MagicMock()
    cls1 = MagicMock()
    cls1.is_state_machine = False

    result: dict[str, Any] = {
        "module": MagicMock(name="mod"),
        "functions": {
            "mod.complex_fn": func1,
            "mod.MyService.simple_method": func2,
        },
        "classes": {
            "mod.MyService": cls1,
        },
    }
    result["module"].name = "mod"

    calculate_python_complexity(py_code, "test.py", result)

    assert func1.complexity["cyclomatic_complexity"] == 3
    assert func1.complexity["cc_rank"] == "A"
    assert func2.complexity["cyclomatic_complexity"] == 1
    assert func2.complexity["cc_rank"] == "A"
