"""Hotspots and refactoring priorities builder for project.yaml."""

from pathlib import Path
from typing import Any, Dict, List

from code2llm.core.models import AnalysisResult, FunctionInfo
from code2llm.exporters.toon.helpers import _is_excluded, _rel_path
from .constants import FAN_OUT_THRESHOLD, CC_WARNING, GOD_MODULE_LINES


def build_hotspots(result: AnalysisResult) -> List[Dict[str, Any]]:
    """Build hotspots list (high fan-out functions)."""
    spots = []
    for qname, fi in result.functions.items():
        if _is_excluded(fi.file):
            continue
        fan_out = len(set(fi.calls))
        if fan_out >= FAN_OUT_THRESHOLD:
            display = fi.name
            if fi.class_name:
                display = f"{fi.class_name}.{fi.name}"
            note = hotspot_note(fi, fan_out)
            spots.append(
                {
                    "name": display,
                    "fan_out": fan_out,
                    "note": note,
                }
            )
    spots.sort(key=lambda s: s["fan_out"], reverse=True)
    return spots[:10]


def hotspot_note(fi: FunctionInfo, fan_out: int) -> str:
    """Generate descriptive note for a hotspot."""
    if "format" in fi.name.lower() or "dispatch" in fi.name.lower():
        return f"{fan_out}-way dispatch"
    if "export" in fi.name.lower():
        return f"Export with {fan_out} outputs"
    if "analyze" in fi.name.lower() or "process" in fi.name.lower():
        return f"Analysis pipeline, {fan_out} stages"
    if fi.docstring:
        return fi.docstring[:80]
    return f"Orchestrates {fan_out} calls"


def _cc_priorities(result: AnalysisResult) -> List[Dict]:
    """Return split-function actions for all high-CC functions."""
    out = []
    for _qname, fi in result.functions.items():
        if _is_excluded(fi.file):
            continue
        cc = fi.complexity.get("cyclomatic_complexity", 0)
        if cc < CC_WARNING:
            continue
        display = f"{fi.class_name}.{fi.name}" if fi.class_name else fi.name
        out.append({
            "action": f"Split {display} (CC={cc})",
            "impact": "high" if cc >= 25 else "medium",
            "effort": "low",
            "module": Path(_rel_path(fi.file, result.project_path)).name,
        })
    return out


def _cycle_priorities(result: AnalysisResult) -> List[Dict]:
    """Return break-cycle actions for the first 3 circular dependencies."""
    cycles = result.metrics.get("project", {}).get("circular_dependencies", [])
    return [
        {"action": f"Break circular dependency: {' → '.join(str(c) for c in cycle) if isinstance(cycle, list) else str(cycle)}",  # noqa: E501
         "impact": "medium", "effort": "low"}
        for cycle in cycles[:3]
    ]


def _fanout_priorities(hotspots: List[Dict]) -> List[Dict]:
    """Return reduce-fan-out actions for the top hotspots."""
    return [
        {"action": f"Reduce {s['name']} fan-out (currently {s['fan_out']})",
         "impact": "medium", "effort": "medium"}
        for s in hotspots[:3] if s["fan_out"] >= 15
    ]


def _godmod_priorities(modules: List[Dict]) -> List[Dict]:
    """Return split-module actions for god modules."""
    return [
        {"action": f"Split god module {m['path']} ({m['lines']}L, {m['classes']} classes)",
         "impact": "high", "effort": "high"}
        for m in modules if m["lines"] >= GOD_MODULE_LINES
    ]


def build_refactoring(
    result: AnalysisResult,
    modules: List[Dict],
    hotspots: List[Dict],
) -> Dict[str, Any]:
    """Build prioritized refactoring actions."""
    priorities = (
        _cc_priorities(result)
        + _cycle_priorities(result)
        + _fanout_priorities(hotspots)
        + _godmod_priorities(modules)
    )
    impact_order = {"high": 0, "medium": 1, "low": 2}
    effort_order = {"low": 0, "medium": 1, "high": 2}
    priorities.sort(key=lambda p: (
        impact_order.get(p.get("impact", "low"), 9),
        effort_order.get(p.get("effort", "medium"), 9),
    ))
    return {"priorities": priorities[:15]}
