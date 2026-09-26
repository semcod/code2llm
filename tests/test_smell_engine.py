"""Unit tests for the atomized smell_engine functions."""

from __future__ import annotations

from code2llm.analysis.smell_engine import (
    detect_all_smells,
    detect_bottlenecks,
    detect_circular_dependencies,
    detect_feature_envy,
    detect_god_functions,
    detect_god_modules,
    index_mutations_by_scope,
)
from code2llm.core.models import (
    AnalysisResult,
    FunctionInfo,
    ModuleInfo,
    Mutation,
)


def _func(
    name: str,
    file: str,
    args: list[str] | None = None,
    line: int = 1,
    centrality: float = 0.0,
    cc: int = 1,
) -> FunctionInfo:
    return FunctionInfo(
        name=name,
        qualified_name=f"{file}::{name}",
        file=file,
        line=line,
        args=args or [],
        centrality=centrality,
        complexity={"cyclomatic_complexity": cc, "cc": cc},
    )


def _mut(variable: str, file: str, scope: str, line: int = 1) -> Mutation:
    return Mutation(
        variable=variable,
        file=file,
        line=line,
        type="assign",
        scope=scope,
        context="",
    )


def test_index_mutations_by_scope():
    muts = [
        _mut("x", "a.py", "foo"),
        _mut("y", "a.py", "foo"),
        _mut("z", "b.py", "bar"),
    ]
    indexed = index_mutations_by_scope(muts)
    assert len(indexed["foo"]) == 2
    assert len(indexed["bar"]) == 1
    assert indexed["baz"] == []


def test_detect_god_functions():
    funcs = {
        "mod.large": _func("large", "mod.py", cc=15),
        "mod.normal": _func("normal", "mod.py", cc=3),
    }
    metrics = {
        "mod.large": {"fan_out": 12},
        "mod.normal": {"fan_out": 2},
    }
    mutations_by_scope = {
        "mod.large": [_mut(f"v{i}", "mod.py", "mod.large") for i in range(7)],
        "mod.normal": [],
    }

    smells = detect_god_functions(funcs, metrics, mutations_by_scope)
    assert len(smells) == 1
    assert smells[0].type == "god_function"
    assert smells[0].name == "God Function: large"
    assert smells[0].context["fan_out"] == 12
    assert smells[0].context["mutations"] == 7
    assert smells[0].context["complexity"] == 15
    assert smells[0].severity <= 1.0


def test_detect_god_modules():
    mods = {
        "huge_mod": ModuleInfo(
            name="huge_mod",
            file="huge.py",
            functions=[f"f_{i}" for i in range(45)],
            classes=[f"C_{i}" for i in range(12)],
        ),
        "small_mod": ModuleInfo(
            name="small_mod",
            file="small.py",
            functions=["f1", "f2"],
            classes=["C1"],
        ),
    }

    smells = detect_god_modules(mods)
    assert len(smells) == 1
    assert smells[0].name == "God Module: huge_mod"
    assert smells[0].context["functions"] == 45
    assert smells[0].context["classes"] == 12


def test_detect_feature_envy():
    funcs = {
        "pkg.worker": _func("worker", "pkg/worker.py"),
    }
    mutations_by_scope = {
        "pkg.worker": [
            _mut("other1.state", "pkg/worker.py", "pkg.worker"),
            _mut("other2.data", "pkg/worker.py", "pkg.worker"),
            _mut("other3.client", "pkg/worker.py", "pkg.worker"),
        ]
    }

    smells = detect_feature_envy(funcs, mutations_by_scope)
    assert len(smells) == 1
    assert smells[0].type == "feature_envy"
    assert smells[0].name == "Feature Envy: worker"
    assert len(smells[0].context["foreign_mutations"]) == 3


def test_detect_bottlenecks():
    funcs = {
        "core.router": _func("router", "core/router.py", centrality=0.25),
        "core.leaf": _func("leaf", "core/router.py", centrality=0.02),
    }

    smells = detect_bottlenecks(funcs)
    assert len(smells) == 1
    assert smells[0].type == "bottleneck"
    assert smells[0].name == "Structural Bottleneck: router"
    assert smells[0].context["centrality"] == 0.25


def test_detect_circular_dependencies():
    funcs = {
        "a.f": _func("f", "a.py"),
        "b.g": _func("g", "b.py"),
    }
    cycles = [["a.f", "b.g", "a.f"]]

    smells = detect_circular_dependencies(cycles, funcs)
    assert len(smells) == 1
    assert smells[0].type == "circular_dependency"
    assert smells[0].name == "Circular Dependency: a.f -> b.g -> a.f"
    assert smells[0].file == "a.py"


def test_detect_all_smells_orchestration():
    result = AnalysisResult()
    result.functions["core.f"] = _func("f", "core.py", centrality=0.3)
    result.metrics["project"] = {
        "circular_dependencies": [["core.f", "core.g"]]
    }
    result.functions["core.g"] = _func("g", "core.py")

    smells = detect_all_smells(result)
    assert len(smells) >= 2
    assert result.smells == smells
