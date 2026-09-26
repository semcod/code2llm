"""Unit tests for the atomized call graph engine (code2llm.analysis.call_graph_engine)."""

from __future__ import annotations

import ast
from typing import Any
from unittest.mock import MagicMock

from code2llm.analysis.call_graph_engine import (
    CallGraphExtractor,
    _rust_batch_calls,
    calculate_call_metrics,
    extract_calls_regex,
)
from code2llm.analysis.complexity import _find_rust_binary
from code2llm.core.config import Config


def test_calculate_call_metrics() -> None:
    caller = MagicMock()
    caller.calls = ["mod.callee"]
    caller.called_by = []
    caller.complexity = 3

    callee = MagicMock()
    callee.calls = []
    callee.called_by = []
    callee.complexity = 2

    functions = {
        "mod.caller": caller,
        "mod.callee": callee,
    }
    metrics: dict[str, dict[str, Any]] = {}

    res = calculate_call_metrics(functions, metrics)

    assert "mod.caller" in callee.called_by
    assert res["mod.caller"]["fan_out"] == 1
    assert res["mod.caller"]["fan_in"] == 0
    assert res["mod.callee"]["fan_out"] == 0
    assert res["mod.callee"]["fan_in"] == 1


def test_extract_calls_regex_resolves_known_and_external() -> None:
    code = """
function caller() {
    helper();
    externalLib();
    if (x > 0) {
        return done();
    }
}

function helper() {
    return 1;
}
"""
    f_caller = MagicMock()
    f_caller.line = 2
    f_caller.calls = []

    f_helper = MagicMock()
    f_helper.line = 10
    f_helper.calls = []

    result: dict[str, Any] = {
        "functions": {
            "app.caller": f_caller,
            "app.helper": f_helper,
        }
    }

    extract_calls_regex(code, "app", result)

    assert "app.helper" in f_caller.calls
    assert "app.externalLib" in f_caller.calls
    assert "app.done" in f_caller.calls
    assert "if" not in f_caller.calls
    assert "return" not in f_caller.calls


def test_call_graph_extractor_ast() -> None:
    py_code = """
import os

def helper():
    return 42

class Worker:
    def process(self):
        val = helper()
        self.save(val)

    def save(self, data):
        pass
"""
    tree = ast.parse(py_code)
    cfg = Config()
    extractor = CallGraphExtractor(cfg)

    # Pre-populate dummy functions in result to receive calls
    extractor.extract(tree, "mod", "test.py")

    assert "Worker" in extractor.result.classes
    assert extractor.result.classes["Worker"]["methods"] == ["process", "save"]


def test_rust_batch_calls_matches_expected() -> None:
    rust_bin = _find_rust_binary()
    if not rust_bin:
        return

    code = """
void foo() {
    this.bar();
    baz();
    if (true) {
        done();
    }
}
"""
    res = _rust_batch_calls(lines=[2], content=code)
    assert res is not None
    assert 2 in res
    calls = res[2]
    assert "bar" in calls
    assert "baz" in calls
    assert "done" in calls
    assert "if" not in calls
