"""Pure, decoupled code smell and hotspot detection algorithms.

Provides atomic functions for detecting:
- God Functions
- God Modules
- Feature Envy
- Data Clumps
- Shotgun Surgery
- Structural Bottlenecks
- Circular Dependencies
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Mapping, Sequence, Set, Tuple

from code2llm.core.models import (
    AnalysisResult,
    CodeSmell,
    FunctionInfo,
    ModuleInfo,
    Mutation,
)


def index_mutations_by_scope(
    mutations: Sequence[Mutation],
) -> Dict[str, List[Mutation]]:
    """Index mutations by their scope to avoid O(n*m) lookup scans."""
    mutations_by_scope: Dict[str, List[Mutation]] = defaultdict(list)
    for m in mutations:
        mutations_by_scope[m.scope].append(m)
    return mutations_by_scope


def detect_god_functions(
    functions: Mapping[str, FunctionInfo],
    metrics: Mapping[str, dict] | None = None,
    mutations_by_scope: Mapping[str, Sequence[Mutation]] | None = None,
) -> List[CodeSmell]:
    """Detect high fan-out, overly complex, or mutation-heavy functions."""
    if metrics is None:
        metrics = {}
    if mutations_by_scope is None:
        mutations_by_scope = {}

    smells: List[CodeSmell] = []
    for func_name, func_info in functions.items():
        fn_metrics = metrics.get(func_name, {})
        fan_out = fn_metrics.get("fan_out", 0)
        mutation_count = len(mutations_by_scope.get(func_name, []))

        # Use cyclomatic complexity (mapped to 'cc' in FunctionInfo.complexity)
        complexity = func_info.complexity.get("cyclomatic_complexity", 1)

        if fan_out > 10 or mutation_count > 6 or complexity > 12:
            severity = (
                (fan_out / 20) * 0.3
                + (mutation_count / 15) * 0.3
                + (complexity / 30) * 0.4
            )
            severity = min(1.0, severity)

            smells.append(
                CodeSmell(
                    name=f"God Function: {func_info.name}",
                    type="god_function",
                    file=func_info.file,
                    line=func_info.line,
                    severity=severity,
                    description=(
                        f"Function '{func_info.name}' is oversized:"
                        f" CC={complexity}, fan-out={fan_out},"
                        f" mutations={mutation_count}."
                    ),
                    context={
                        "fan_out": fan_out,
                        "mutations": mutation_count,
                        "complexity": complexity,
                        "function": func_name,
                    },
                )
            )
    return smells


def detect_god_modules(modules: Mapping[str, ModuleInfo]) -> List[CodeSmell]:
    """Detect oversized modules/packages (>40 functions or >10 classes)."""
    smells: List[CodeSmell] = []
    for mod_name, mod in modules.items():
        f_count = len(mod.functions)
        c_count = len(mod.classes)

        if f_count > 40 or c_count > 10:
            severity = (f_count / 100) * 0.5 + (c_count / 25) * 0.5
            severity = min(1.0, severity)

            smells.append(
                CodeSmell(
                    name=f"God Module: {mod_name}",
                    type="god_function",  # Map to extract_method
                    file=mod.file,
                    line=1,
                    severity=severity,
                    description=(
                        f"Module '{mod_name}' is too large"
                        f" ({f_count} functions, {c_count} classes)."
                        " Consider splitting into sub-modules."
                    ),
                    context={"functions": f_count, "classes": c_count},
                )
            )
    return smells


def detect_feature_envy(
    functions: Mapping[str, FunctionInfo],
    mutations_by_scope: Mapping[str, Sequence[Mutation]] | None = None,
) -> List[CodeSmell]:
    """Detect functions that mutate multiple variables in other modules."""
    if mutations_by_scope is None:
        mutations_by_scope = {}

    smells: List[CodeSmell] = []
    for func_name, func_info in functions.items():
        mut_mod = func_name.split(".")[0]
        foreign_mutations: List[str] = []

        for mutation in mutations_by_scope.get(func_name, []):
            if "." in mutation.variable:
                origin_mod = mutation.variable.split(".")[0]
                if origin_mod != mut_mod:
                    foreign_mutations.append(mutation.variable)

        if len(set(foreign_mutations)) >= 3:
            smells.append(
                CodeSmell(
                    name=f"Feature Envy: {func_info.name}",
                    type="feature_envy",
                    file=func_info.file,
                    line=func_info.line,
                    severity=0.7,
                    description=(
                        f"Function '{func_info.name}' mutates multiple"
                        f" variables in other modules:"
                        f" {', '.join(set(foreign_mutations))}."
                    ),
                    context={
                        "foreign_mutations": list(set(foreign_mutations)),
                    },
                )
            )
    return smells


def detect_data_clumps(
    functions: Mapping[str, FunctionInfo],
) -> List[CodeSmell]:
    """Detect 3+ variables frequently passed together within same file."""
    smells: List[CodeSmell] = []
    arg_sets: Dict[Tuple[str, frozenset], List[str]] = {}

    for func_name, func_info in functions.items():
        if len(func_info.args) >= 3:
            key = (func_info.file, frozenset(func_info.args))
            if key not in arg_sets:
                arg_sets[key] = []
            arg_sets[key].append(func_name)

    for (file, args), funcs in arg_sets.items():
        if len(funcs) >= 2:
            for func_name in funcs:
                func_info = functions[func_name]
                smells.append(
                    CodeSmell(
                        name=f"Data Clump: {', '.join(args)}",
                        type="data_clump",
                        file=func_info.file,
                        line=func_info.line,
                        severity=0.6,
                        description=(
                            f"Arguments ({', '.join(args)}) are used together"
                            f" in multiple functions: {', '.join(funcs)}."
                        ),
                        context={
                            "clump": list(args),
                            "related_functions": funcs,
                        },
                    )
                )
    return smells


def detect_shotgun_surgery(
    mutations: Sequence[Mutation],
    functions: Mapping[str, FunctionInfo],
) -> List[CodeSmell]:
    """Detect variables whose mutation spans 5+ functions in same file."""
    smells: List[CodeSmell] = []
    var_mutators: Dict[Tuple[str, str], Set[str]] = {}

    for mutation in mutations:
        key = (mutation.file, mutation.variable)
        if key not in var_mutators:
            var_mutators[key] = set()
        var_mutators[key].add(mutation.scope)

    for (file, var), funcs in var_mutators.items():
        if len(funcs) >= 5:
            # Find a representative function to report the smell
            func_name = list(funcs)[0]
            func_info = functions.get(func_name)
            if not func_info:
                continue

            smells.append(
                CodeSmell(
                    name=f"Shotgun Surgery: {var}",
                    type="shotgun_surgery",
                    file=func_info.file,
                    line=func_info.line,
                    severity=0.8,
                    description=(
                        f"Mutation of variable '{var}' spans"
                        f" {len(funcs)} functions in {file}."
                        " Changing this logic requires work in many places."
                    ),
                    context={
                        "variable": var,
                        "file": file,
                        "affected_functions": list(funcs),
                    },
                )
            )
    return smells


def detect_bottlenecks(
    functions: Mapping[str, FunctionInfo],
) -> List[CodeSmell]:
    """Detect functions with high Betweenness Centrality (>0.1)."""
    smells: List[CodeSmell] = []
    for func_name, func_info in functions.items():
        if func_info.centrality > 0.1:  # Heuristic threshold
            smells.append(
                CodeSmell(
                    name=f"Structural Bottleneck: {func_info.name}",
                    type="bottleneck",
                    file=func_info.file,
                    line=func_info.line,
                    severity=min(1.0, func_info.centrality * 5),
                    description=(
                        f"Function '{func_info.name}' is a structural"
                        f" bottleneck"
                        f" (centrality={round(func_info.centrality, 3)})."
                        " Significant logic flows through this function."
                    ),
                    context={"centrality": func_info.centrality},
                )
            )
    return smells


def detect_circular_dependencies(
    cycles: Sequence[Sequence[str]],
    functions: Mapping[str, FunctionInfo],
) -> List[CodeSmell]:
    """Detect circular dependencies in call graph."""
    smells: List[CodeSmell] = []
    for cycle in cycles:
        if len(cycle) >= 2:
            func_name = cycle[0]
            func_info = functions.get(func_name)
            if not func_info:
                continue

            smells.append(
                CodeSmell(
                    name=f"Circular Dependency: {' -> '.join(cycle)}",
                    type="circular_dependency",
                    file=func_info.file,
                    line=func_info.line,
                    severity=0.8,
                    description=(
                        f"Circular dependency detected: {' -> '.join(cycle)}."
                        " This indicates high coupling and may lead to"
                        " infinite recursion or initialization issues."
                    ),
                    context={"cycle": list(cycle)},
                )
            )
    return smells


def detect_all_smells(
    result: AnalysisResult,
    mutations_by_scope: Mapping[str, Sequence[Mutation]] | None = None,
) -> List[CodeSmell]:
    """Orchestrate detection of all code smells across an AnalysisResult."""
    if mutations_by_scope is None:
        mutations_by_scope = index_mutations_by_scope(result.mutations)

    smells: List[CodeSmell] = []
    smells.extend(
        detect_god_functions(
            result.functions, result.metrics, mutations_by_scope
        )
    )
    smells.extend(detect_god_modules(result.modules))
    smells.extend(detect_feature_envy(result.functions, mutations_by_scope))
    smells.extend(detect_data_clumps(result.functions))
    smells.extend(detect_shotgun_surgery(result.mutations, result.functions))
    smells.extend(detect_bottlenecks(result.functions))

    project_metrics = result.metrics.get("project", {})
    cycles = project_metrics.get("circular_dependencies", [])
    smells.extend(detect_circular_dependencies(cycles, result.functions))

    result.smells = smells
    return smells
