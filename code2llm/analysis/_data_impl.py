"""Private implementation helpers for DataAnalyzer.

Extracted to keep data_analysis.py under the MI hard-gate threshold.
All functions here are module-private (leading underscore) and called
exclusively from DataAnalyzer in data_analysis.py.
"""
# ── Data pipeline helpers ─────────────────────────────────────────────────────
# _find_data_pipelines()   : detect sequential transform chains from call graph.
# ── State-machine helpers ─────────────────────────────────────────────────────
# _is_state_func()         : heuristic; True if name contains state keyword.
# _state_affected_by()     : callers that mutate the given function's state.
# _find_state_patterns()   : aggregate state-machine detections per module.
# ── Data-dependency helpers ───────────────────────────────────────────────────
# _find_data_dependencies() : build producer→consumer edges from shared types.
# ── Event-flow helpers ────────────────────────────────────────────────────────
# _is_event_func()         : heuristic; True if name contains event keyword.
# _event_handlers()        : functions that consume outputs of an event source.
# _find_event_flows()      : aggregate event-flow detections across the project.
# ── Type-inference helpers ────────────────────────────────────────────────────
# _detect_types_from_name(): keyword-match on function name + docstring.
# _create_type_entry()     : initialise a type-usage dict entry.
# _update_type_stats()     : accumulate consumed/produced counts per type.
# _infer_parameter_types() : extract type hints from function parameters.
# _infer_return_types()    : extract type hints from function return annotation.
# _analyze_data_types()    : top-level driver; returns list of type-usage entries.
# _get_function_data_types(): merge name-based + annotation-based type signals.

from typing import Any, Dict, List
from code2llm.core.models import AnalysisResult


# ---------------------------------------------------------------------------
# Flow finders
# ---------------------------------------------------------------------------


def _find_data_pipelines(result: AnalysisResult, categorize_fn, make_stage_fn, max_pipelines: int) -> list:
    """Find data transformation pipelines in the codebase."""
    input_funcs, transform_funcs, output_funcs = categorize_fn(result)

    pipelines: list = []
    for in_name, in_func in input_funcs[:20]:
        for t_name, t_func in transform_funcs[:30]:
            if t_name not in in_func.calls:
                continue
            for out_name, out_func in output_funcs[:20]:
                if out_name not in t_func.calls:
                    continue
                pipelines.append(
                    {
                        "pipeline_id": f"pipeline_{len(pipelines) + 1}",
                        "stages": [
                            make_stage_fn("input", in_name, in_func),
                            make_stage_fn("transform", t_name, t_func),
                            make_stage_fn("output", out_name, out_func),
                        ],
                        "data_flow": f"{in_name} → {t_name} → {out_name}",
                    }
                )
                if len(pipelines) >= max_pipelines:
                    return pipelines
    return pipelines


_STATE_INDICATORS = ["state", "status", "mode", "phase", "lifecycle", "session", "context"]
_TRANSITION_INDICATORS = ["transition", "change", "update", "set_state", "switch"]


def _is_state_func(name_lower: str) -> bool:
    """Return True if the function name suggests state management."""
    return any(ind in name_lower for ind in _STATE_INDICATORS + _TRANSITION_INDICATORS)


def _state_affected_by(func, functions: dict) -> list:
    """Return calls that look like state-managing functions."""
    return [
        call for call in list(func.calls)[:10]
        if (cf := functions.get(call)) and any(ind in cf.name.lower() for ind in _STATE_INDICATORS)
    ]


def _find_state_patterns(result: AnalysisResult) -> list:
    """Find state management patterns."""
    patterns: list = []
    for func_name, func in result.functions.items():
        name_lower = func.name.lower()
        if not _is_state_func(name_lower):
            continue
        patterns.append({
            "function": func_name,
            "type": "state_manager" if ("set" in name_lower or "update" in name_lower) else "state_reader",
            "affects_states": _state_affected_by(func, result.functions)[:5],
            "description": func.docstring[:150] if func.docstring else "N/A",
        })
        if len(patterns) >= 20:
            break
    return patterns


def _find_data_dependencies(result: AnalysisResult) -> list:
    """Find cross-module data dependencies."""
    module_data_flow: Dict[Any, Any] = {}
    for func_name, func in result.functions.items():
        func_module = func_name.rsplit(".", 1)[0] if "." in func_name else "root"
        for called in list(func.calls)[:15]:
            called_module = called.rsplit(".", 1)[0] if "." in called else "root"
            if func_module != called_module and called in result.functions:
                key = (func_module, called_module)
                if key not in module_data_flow:
                    module_data_flow[key] = {
                        "from_module": func_module,
                        "to_module": called_module,
                        "data_functions": [],
                        "call_count": 0,
                    }
                module_data_flow[key]["data_functions"].append({"caller": func_name, "callee": called})
                module_data_flow[key]["call_count"] += 1
    deps = sorted(module_data_flow.values(), key=lambda x: x["call_count"], reverse=True)
    for dep in deps:
        dep["data_functions"] = dep["data_functions"][:10]
    return deps[:15]


_EVENT_INDICATORS = ["event", "emit", "trigger", "notify", "callback", "handler", "listen", "subscribe"]
_HOOK_INDICATORS = ["hook", "on_", "before_", "after_", "pre_", "post_"]
_EVENT_HANDLER_WORDS = _EVENT_INDICATORS + ["handle", "process"]


def _is_event_func(name_lower: str) -> bool:
    """Return True if the function name suggests event handling or emission."""
    return any(ind in name_lower for ind in _EVENT_INDICATORS) or any(
        name_lower.startswith(ind) for ind in _HOOK_INDICATORS
    )


def _event_handlers(func, functions: dict) -> list:
    """Return list of called functions that look like event handlers."""
    result = []
    for called in list(func.calls)[:10]:
        cf = functions.get(called)
        if cf and any(ind in cf.name.lower() for ind in _EVENT_HANDLER_WORDS):
            result.append(called)
    return result


def _find_event_flows(result: AnalysisResult) -> list:
    """Find event-driven patterns."""
    flows: list = []
    for func_name, func in result.functions.items():
        name_lower = func.name.lower()
        if not _is_event_func(name_lower):
            continue
        flows.append({
            "event_source": func_name,
            "type": "emitter" if ("emit" in name_lower or "trigger" in name_lower) else "handler",
            "handlers": _event_handlers(func, result.functions)[:5],
            "description": func.docstring[:150] if func.docstring else "N/A",
        })
        if len(flows) >= 20:
            break
    return flows


# ---------------------------------------------------------------------------
# Type analysis helpers
# ---------------------------------------------------------------------------


def _detect_types_from_name(func_name: str, doc: str) -> list:
    """Detect data types from function name and docstring."""
    type_indicators = {
        "list": ["list", "array", "items", "elements", "collection", "sequence"],
        "dict": ["dict", "map", "mapping", "key_value", "record", "object"],
        "str": ["string", "text", "content", "message"],
        "int": ["int", "count", "index", "number", "id"],
        "float": ["float", "decimal", "score", "probability"],
        "bool": ["bool", "flag", "is_", "has_"],
        "tuple": ["tuple", "pair"],
        "set": ["set", "unique"],
    }
    name_lower = func_name.lower()
    return [t for t, inds in type_indicators.items() if any(ind in name_lower or ind in doc for ind in inds)]


def _create_type_entry(type_key: str, detected: list, params: list, returns: list) -> dict:
    """Create a new data type entry."""
    return {
        "type_name": type_key,
        "detected_types": list(set(detected)),
        "parameter_types": list(set(params)),
        "return_types": list(set(returns)),
        "functions": [],
        "usage_count": 0,
        "cross_module_usage": 0,
    }


def _update_type_stats(entry: dict, func_name: str, func_module: str, calls: list) -> None:
    """Update type entry with function info and check cross-module usage."""
    entry["functions"].append(func_name)
    entry["usage_count"] += 1
    for called in list(calls)[:10]:
        called_module = called.rsplit(".", 1)[0] if "." in called else "root"
        if called_module != func_module:
            entry["cross_module_usage"] += 1
            break


def _infer_parameter_types(func) -> list:
    """Infer parameter types from function name patterns."""
    params: List[str] = []
    name = func.name.lower()
    if "list" in name or "items" in name:
        params.append("list")
    if "dict" in name or "map" in name:
        params.append("dict")
    if "text" in name or "string" in name:
        params.append("str")
    if "count" in name or "index" in name:
        params.append("int")
    return params


def _infer_return_types(func) -> list:
    """Infer return types from function name patterns."""
    returns: List[str] = []
    name = func.name.lower()
    if name.startswith(("get_", "find_")):
        returns.append("dict")
    if name.startswith(("is_", "has_")):
        returns.append("bool")
    if name.startswith(("count_", "len_")):
        returns.append("int")
    if name.startswith(("list_", "get_all_")):
        returns.append("list")
    return returns


def _analyze_data_types(result: AnalysisResult) -> list:
    """Analyze data types and usage across all functions."""
    data_types: Dict[str, Any] = {}
    for func_name, func in result.functions.items():
        doc = func.docstring.lower() if func.docstring else ""
        detected = _detect_types_from_name(func.name, doc)
        params = _infer_parameter_types(func)
        returns = _infer_return_types(func)
        if detected or params or returns:
            type_key = ",".join(sorted(set(detected + params + returns)))
            if type_key not in data_types:
                data_types[type_key] = _create_type_entry(type_key, detected, params, returns)
            func_module = func_name.rsplit(".", 1)[0] if "." in func_name else "root"
            _update_type_stats(data_types[type_key], func_name, func_module, func.calls)
    return sorted(data_types.values(), key=lambda x: x["usage_count"], reverse=True)


# ---------------------------------------------------------------------------
# Graph and process analysis helpers
# ---------------------------------------------------------------------------


_NAME_TYPE_KEYWORDS: List[tuple] = [
    ("list", ("list", "items")),
    ("dict", ("dict", "map")),
    ("str", ("text", "string")),
    ("int", ("count", "index")),
]
_DOC_TYPE_KEYWORDS: List[tuple] = [
    ("list", ("list",)),
    ("dict", ("dict",)),
    ("str", ("string", "text")),
]


def _get_function_data_types(func) -> list:
    """Derive data type labels for a function from its name and docstring."""
    name = func.name.lower()
    types = [dt for dt, kws in _NAME_TYPE_KEYWORDS if any(kw in name for kw in kws)]
    if func.docstring:
        doc = func.docstring.lower()
        types += [dt for dt, kws in _DOC_TYPE_KEYWORDS if any(kw in doc for kw in kws)]
    return list(set(types))


def _build_data_flow_graph(result: AnalysisResult) -> dict:
    """Build data flow graph from function relationships."""
    nodes: Dict[str, Any] = {}
    edges: list = []
    for func_name, func in result.functions.items():
        nodes[func_name] = {
            "id": func_name,
            "name": func.name.split(".")[-1],
            "module": func_name.rsplit(".", 1)[0] if "." in func_name else "root",
            "data_types": _get_function_data_types(func),
            "in_degree": len(func.called_by),
            "out_degree": len(func.calls),
            "is_hub": len(func.calls) > 5 or len(func.called_by) > 5,
        }
    for func_name, func in result.functions.items():
        for called in list(func.calls)[:15]:
            if called in result.functions:
                edges.append({"from": func_name, "to": called, "data_flow": True, "weight": 1})
    return {
        "nodes": nodes,
        "edges": edges,
        "stats": {
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "hub_nodes": sum(1 for n in nodes.values() if n["is_hub"]),
        },
    }


def _identify_process_patterns(result: AnalysisResult) -> list:
    """Identify common data processing patterns (filter, map, reduce, etc.)."""
    patterns: Dict[str, list] = {
        "filter": [], "map": [], "reduce": [], "aggregate": [], "transform": [], "validate": [],
    }
    indicators = {
        "filter": ["filter", "select", "where", "find"],
        "map": ["map", "transform", "process"],
        "reduce": ["reduce", "sum", "count", "aggregate"],
        "aggregate": ["group", "bucket", "cluster"],
        "transform": ["transform", "convert", "normalize"],
        "validate": ["validate", "check", "verify"],
    }
    for func_name, func in result.functions.items():
        name = func.name.lower()
        doc = func.docstring.lower() if func.docstring else ""
        for p_type, inds in indicators.items():
            if any(ind in name or ind in doc for ind in inds):
                patterns[p_type].append(
                    {
                        "function": func_name,
                        "description": func.docstring[:100] if func.docstring else "N/A",
                        "data_flow": f"{len(func.called_by)} → {func_name} → {len(func.calls)}",
                    }
                )
                break
    res = []
    for p_type, funcs in patterns.items():
        res.append({"pattern_type": p_type, "functions": funcs[:10], "count": len(funcs)})
    return sorted(res, key=lambda x: x["count"], reverse=True)


def _type_consolidations(data_types: list) -> list:
    """Find groups of similar data types that could be consolidated."""
    similar: Dict[str, list] = {}
    for dt in data_types:
        sig = ",".join(sorted(dt["detected_types"]))
        similar.setdefault(sig, []).append(dt)
    result = []
    for sig, sims in similar.items():
        if len(sims) > 1:
            usage = sum(s["usage_count"] for s in sims)
            if usage > 10:
                result.append({
                    "type_signature": sig,
                    "similar_types": [s["type_name"] for s in sims],
                    "total_usage": usage,
                    "potential_reduction": len(sims) - 1,
                })
    return result


def _process_consolidations(result: AnalysisResult) -> list:
    """Find repeated process patterns that could be consolidated."""
    return [
        {"pattern_type": p["pattern_type"], "function_count": p["count"],
         "potential_reduction": p["count"] // 3}
        for p in _identify_process_patterns(result) if p["count"] > 5
    ]


def _hub_optimizations(dfg: dict) -> list:
    """Identify hub nodes that are candidates for splitting or caching."""
    return [
        {"function": hub["id"], "connections": hub["in_degree"] + hub["out_degree"],
         "optimization_type": "split" if hub["out_degree"] > 10 else "cache"}
        for hub in list(n for n in dfg["nodes"].values() if n["is_hub"])[:10]
    ]


def _analyze_optimization_opportunities(
    result: AnalysisResult, data_types: list, dfg: dict
) -> dict:
    """Analyze optimization opportunities in data handling."""
    type_cons = _type_consolidations(data_types)
    proc_cons = _process_consolidations(result)
    hub_opts = _hub_optimizations(dfg)
    return {
        "potential_score": (len(type_cons) * 10 + len(proc_cons) * 15 + len(hub_opts) * 5) / 100.0,
        "type_consolidation": type_cons,
        "process_consolidation": proc_cons,
        "hub_optimization": hub_opts,
        "recommendations": [],
    }
