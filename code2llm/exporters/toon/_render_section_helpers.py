"""Section rendering helpers extracted from ToonRenderer.

Contains: health, refactor, hotspots, classes, pipelines, external,
language label detection, and pipeline tracing utilities.
"""

from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

from code2llm.core.models import AnalysisResult
from code2llm.core.config import LANGUAGE_EXTENSIONS

from .constants import CC_WARNING, MAX_FUNCTIONS_SHOWN


def _detect_language_label(result: AnalysisResult) -> str:
    """Build language breakdown label like 'typescript:463,javascript:10,rust:1'."""
    from .helpers import _is_excluded

    langs: Dict[str, int] = defaultdict(int)
    for mi in result.modules.values():
        if _is_excluded(mi.file):
            continue
        detected = False
        for lang, extensions in LANGUAGE_EXTENSIONS.items():
            if any(mi.file.endswith(ext) for ext in extensions):
                langs[lang] += 1
                detected = True
                break
        if not detected:
            ext = Path(mi.file).suffix.lower()
            if ext:
                langs[ext.lstrip(".")] += 1
    if not langs:
        return "unknown"
    sorted_langs = sorted(langs.items(), key=lambda x: -x[1])
    return ",".join(f"{lang}:{count}" for lang, count in sorted_langs)


def render_health_section(ctx: Dict[str, Any]) -> List[str]:
    """Render health section."""
    issues = ctx["health"]
    if not issues:
        return ["HEALTH[0]: ok"]
    lines = [f"HEALTH[{len(issues)}]:"]
    for issue in issues:
        icon = "\U0001f534" if issue["severity"] == "red" else "\U0001f7e1"
        lines.append(f"  {icon} {issue['code']:5s} {issue['message']}")
    return lines


def _build_refactor_steps(ctx: Dict[str, Any]) -> List[str]:
    """Build list of refactoring step strings from health, duplicates, and cycles."""
    steps: List[str] = []
    if ctx["duplicates"]:
        steps.append(f"rm duplicates  (-{len(ctx['duplicates'])} dup classes)")
    for gi in [h for h in ctx["health"] if h["code"] == "GOD"]:
        steps.append(f"split {gi['message'].split('=')[0].strip()}  (god module)")
    cc_issues = [h for h in ctx["health"] if h["code"] == "CC"]
    if cc_issues:
        steps.append(f"split {len(cc_issues)} high-CC methods  (CC>{CC_WARNING})")
    if ctx["cycles"]:
        steps.append(f"break {len(ctx['cycles'])} circular dependencies")
    return steps


def render_refactor_section(ctx: Dict[str, Any]) -> List[str]:
    """Generate numbered refactoring steps from health issues."""
    steps = _build_refactor_steps(ctx)
    if not steps:
        return ["REFACTOR[0]: none needed"]
    lines = [f"REFACTOR[{len(steps)}]:"]
    for i, step in enumerate(steps, 1):
        lines.append(f"  {i}. {step}")
    return lines


def render_hotspots_section(ctx: Dict[str, Any]) -> List[str]:
    """Render hotspots section."""
    spots = ctx["hotspots"]
    if not spots:
        return ["HOTSPOTS: none"]
    lines = ["HOTSPOTS:"]
    for i, s in enumerate(spots, 1):
        lines.append(
            f"  #{i:<2} {s['name']:35s}  fan={s['fan_out']:<3}"
            f'  "{s["description"]}"'
        )
    return lines


def render_classes_section(ctx: Dict[str, Any]) -> List[str]:
    """Render CLASSES section with visual bar chart proportional to method count."""
    classes = ctx["class_metrics"]
    if not classes:
        return ["CLASSES: none"]
    max_methods = max(c["method_count"] for c in classes) if classes else 1
    bar_max = 24
    lines = ["CLASSES:"]
    for cm in classes:
        mc = cm["method_count"]
        bar_len = int((mc / max_methods) * bar_max) if max_methods > 0 else 0
        bar = "█" * bar_len
        markers = ""
        if cm["max_cc"] >= CC_WARNING:
            markers += "  !!"
        dup_count = sum(1 for d in ctx["duplicates"] if d["class_name"] == cm["name"])
        if dup_count > 0:
            markers += f"  ×{dup_count}"
        lines.append(
            f"  {cm['name']:30s} {bar:<{bar_max}}  {mc:>2}m"
            f"  CC̄={cm['avg_cc']:<4}  max={cm['max_cc']:<4}{markers}"
        )
    return lines


def render_external_section(_ctx: Dict[str, Any]) -> List[str]:
    """Render EXTERNAL section - cross-references to other tools."""
    return [
        "EXTERNAL:",
        "  validation: run `vallm batch .` → validation.toon",
        "  duplication: run `redup scan .` → duplication.toon",
    ]


def _trace_pipeline(start_func: str, result: AnalysisResult, depth: int) -> List[str]:
    """Trace a pipeline starting from an entry point."""
    if depth > 10:
        return []
    chain: List[str] = []
    current: Any = start_func
    visited: set = set()
    while current and current not in visited and len(chain) < 20:
        visited.add(current)
        func_info = result.functions.get(current)
        if not func_info:
            break
        chain.append(current.split(".")[-1])
        next_func = None
        for callee in func_info.calls:
            if callee in result.functions:
                next_func = callee
                break
        current = next_func
    return chain


def _calculate_purity(chain: List[str], result: AnalysisResult) -> float:
    """Calculate purity ratio (functions without side effects)."""
    if not chain:
        return 0.0
    pure_count = 0
    for func_name in chain:
        full_name = next(
            (qname for qname, fi in result.functions.items() if fi.name == func_name),
            None,
        )
        if full_name:
            func_info = result.functions.get(full_name)
            if func_info and not getattr(func_info, "has_side_effects", False):
                pure_count += 1
    return pure_count / len(chain)


def render_pipelines_section(ctx: Dict[str, Any]) -> List[str]:
    """Render PIPELINES section - data flow pipelines from entry points."""
    result: AnalysisResult = ctx["result"]
    pipelines = []
    for func_name, func_info in result.functions.items():
        if not func_info.called_by and func_info.calls:
            chain = _trace_pipeline(func_name, result, depth=0)
            if chain:
                pipelines.append(
                    {
                        "entry": func_name.split(".")[-1],
                        "chain": chain,
                        "purity": _calculate_purity(chain, result),
                    }
                )
    if not pipelines:
        return ["PIPELINES[0]: none detected"]
    lines = [f"PIPELINES[{len(pipelines)}]:"]
    for i, pipe in enumerate(pipelines[:MAX_FUNCTIONS_SHOWN], 1):
        purity_pct = int(pipe["purity"] * 100)
        chain_str = " → ".join(pipe["chain"][:4])
        if len(pipe["chain"]) > 4:
            chain_str += f" → ...({len(pipe['chain']) - 4} more)"
        lines.append(f"  [{i}] Src [{pipe['entry']}]: {chain_str}")
        lines.append(f"      PURITY: {purity_pct}% pure")
    return lines
