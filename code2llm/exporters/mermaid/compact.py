"""Mermaid compact export — compact_flow.mmd module-level aggregation."""

from collections import defaultdict
from typing import Dict, Set, Tuple

from code2llm.core.models import AnalysisResult

from .utils import safe_module, resolve_callee, write_file, build_name_index


def _compute_module_stats(functions: dict, module_of) -> Tuple[Dict, Dict]:
    """Return (mod_funcs, mod_lines) counters keyed by module name."""
    mod_funcs: Dict[str, int] = defaultdict(int)
    mod_lines: Dict[str, int] = defaultdict(int)
    for func_name, fi in functions.items():
        mod = module_of(func_name)
        mod_funcs[mod] += 1
        mod_lines[mod] += (fi.end_line - fi.line if getattr(fi, "end_line", None) else 0)
    return mod_funcs, mod_lines


def _compute_cross_edges(functions: dict, name_index: dict, module_of) -> Dict[Tuple[str, str], int]:
    """Return weighted cross-module edge counter."""
    cross_edges: Dict[Tuple[str, str], int] = defaultdict(int)
    for func_name, fi in functions.items():
        src_mod = module_of(func_name)
        for callee in fi.calls:
            resolved = resolve_callee(callee, functions, name_index)
            if resolved:
                dst_mod = module_of(resolved)
                if dst_mod != src_mod:
                    cross_edges[(src_mod, dst_mod)] += 1
    return cross_edges


def export_compact(result: AnalysisResult, output_path: str) -> None:
    """Export module-level graph: one node per module, weighted edges."""
    from .utils import module_of
    lines = ["flowchart TD"]
    name_index = build_name_index(result.functions)
    mod_funcs, _ = _compute_module_stats(result.functions, module_of)
    cross_edges = _compute_cross_edges(result.functions, name_index, module_of)
    active_mods: Set[str] = {m for pair in cross_edges for m in pair} or set(mod_funcs)
    for mod in sorted(active_mods):
        lines.append(f'    {safe_module(mod)}["{mod}<br/>{mod_funcs.get(mod, 0)} funcs"]')
    for (src, dst), weight in sorted(cross_edges.items(), key=lambda x: -x[1]):
        arrow = "==>" if weight > 3 else "-->"
        lines.append(f"    {safe_module(src)} {arrow}|{weight}| {safe_module(dst)}")
    write_file(output_path, lines)


__all__ = ["export_compact"]
