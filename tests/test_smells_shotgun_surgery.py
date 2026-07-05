"""Tests for SmellDetector._detect_shotgun_surgery.

2026-07-06 incident: grouping mutations by variable *name* alone (ignoring
file) meant a generic local name like `args`/`data`/`client` -- conventionally
reused as an independent local in unrelated functions across unrelated
files -- falsely triggered "Shotgun Surgery" whenever 5+ unrelated functions
anywhere in the analyzed tree happened to share that name. Reproduced live:
40+ false-positive tickets in one monorepo, including `args` in a 40-line,
one-function CLI file reported as "spans 8 functions" (the other 7 were
unrelated `args` locals in unrelated files elsewhere in the tree).
"""

from __future__ import annotations

from code2llm.analysis.smells import SmellDetector
from code2llm.core.models import AnalysisResult, FunctionInfo, Mutation


def _function(name: str, file: str, line: int = 1) -> FunctionInfo:
    return FunctionInfo(name=name, qualified_name=f"{file}::{name}", file=file, line=line)


def _mutation(variable: str, file: str, scope: str, line: int = 1) -> Mutation:
    return Mutation(
        variable=variable, file=file, line=line, type="assign", scope=scope, context=""
    )


def test_same_name_across_unrelated_files_is_not_shotgun_surgery():
    """The core regression: `args` reused independently in 6 unrelated
    files/functions must NOT be flagged -- no single file has more than one
    mutating function."""
    result = AnalysisResult()
    for i in range(6):
        file = f"pkg{i}/cli.py"
        scope = f"pkg{i}.cli::main"
        result.functions[scope] = _function("main", file)
        result.mutations.append(_mutation("args", file, scope))

    smells = SmellDetector(result)._detect_shotgun_surgery()

    assert smells == []


def test_genuine_same_file_shotgun_surgery_still_detected():
    """5+ functions *within the same file* mutating the same variable is the
    real smell and must still be caught."""
    result = AnalysisResult()
    file = "core/session.py"
    for i in range(5):
        scope = f"core.session::step_{i}"
        result.functions[scope] = _function(f"step_{i}", file, line=10 * i)
        result.mutations.append(_mutation("state", file, scope))

    smells = SmellDetector(result)._detect_shotgun_surgery()

    assert len(smells) == 1
    assert smells[0].name == "Shotgun Surgery: state"
    assert set(smells[0].context["affected_functions"]) == {
        f"core.session::step_{i}" for i in range(5)
    }


def test_four_functions_in_one_file_below_threshold():
    result = AnalysisResult()
    file = "core/session.py"
    for i in range(4):
        scope = f"core.session::step_{i}"
        result.functions[scope] = _function(f"step_{i}", file)
        result.mutations.append(_mutation("state", file, scope))

    smells = SmellDetector(result)._detect_shotgun_surgery()

    assert smells == []


def test_same_variable_name_in_two_files_counts_separately_per_file():
    """5 mutators of 'data' in file A (real smell) plus unrelated mutators of
    'data' in file B must not combine into a bigger, less accurate count,
    and file B (below threshold) must not itself be flagged."""
    result = AnalysisResult()
    file_a = "a.py"
    for i in range(5):
        scope = f"a::fn_{i}"
        result.functions[scope] = _function(f"fn_{i}", file_a)
        result.mutations.append(_mutation("data", file_a, scope))

    file_b = "b.py"
    for i in range(3):
        scope = f"b::fn_{i}"
        result.functions[scope] = _function(f"fn_{i}", file_b)
        result.mutations.append(_mutation("data", file_b, scope))

    smells = SmellDetector(result)._detect_shotgun_surgery()

    assert len(smells) == 1
    assert smells[0].context["file"] == file_a
