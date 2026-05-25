"""Rendering functions for TOON exporter."""

from typing import Any, Dict, List

from code2llm.core.models import AnalysisResult

from .helpers import _dup_file_set
from .constants import CC_CRITICAL, CC_WARNING, GOD_MODULE_LINES, MAX_FUNCTIONS_SHOWN
from ._render_coupling_helpers import (
    _select_top_packages,
    _render_coupling_header,
    _build_coupling_row,
    _coupling_row_tag,
    _render_coupling_summary,
    _render_layer_package,
    _format_layer_file_row,
    _render_zero_line_files,
    _format_function_row,
    _render_cc_summary,
)
from ._render_section_helpers import (
    _detect_language_label,
    render_health_section,
    render_refactor_section,
    render_hotspots_section,
    render_classes_section,
    render_external_section,
    render_pipelines_section,
)


class ToonRenderer:
    """Renders all sections for TOON export."""

    def render_header(self, ctx: Dict[str, Any]) -> List[str]:
        """Render header section."""
        result: AnalysisResult = ctx["result"]
        nfiles = len(ctx["files"])
        total_lines = sum(fm["lines"] for fm in ctx["files"].values())
        nfuncs = len(result.functions)
        all_cc = [f["cc"] for f in ctx["func_metrics"]]
        avg_cc = round(sum(all_cc) / len(all_cc), 1) if all_cc else 0.0
        critical = len([f for f in ctx["func_metrics"] if f["cc"] >= CC_CRITICAL])
        ndups = len(ctx["duplicates"])
        ncycles = len(ctx["cycles"])
        lang_label = _detect_language_label(result)
        return [
            f"# code2llm | {nfiles}f {total_lines}L | {lang_label} | {ctx['timestamp']}",
            f"# CC̅={avg_cc} | critical:{critical}/{nfuncs} | dups:{ndups} | cycles:{ncycles}",
        ]

    def render_health(self, ctx: Dict[str, Any]) -> List[str]:
        """Render health section."""
        return render_health_section(ctx)

    def render_refactor(self, ctx: Dict[str, Any]) -> List[str]:
        """Generate numbered refactoring steps from health issues."""
        return render_refactor_section(ctx)

    def render_coupling(self, ctx: Dict[str, Any]) -> List[str]:
        """Render coupling section."""
        matrix = ctx["coupling_matrix"]
        pkg_fan = ctx["pkg_fan"]
        if not matrix:
            return ["COUPLING: no cross-package imports detected"]
        top_pkgs = _select_top_packages(matrix, pkg_fan)
        if not top_pkgs:
            return ["COUPLING: n/a"]
        lines = _render_coupling_header(top_pkgs)
        self._render_coupling_rows(top_pkgs, matrix, pkg_fan, lines)
        _render_coupling_summary(ctx, pkg_fan, lines)
        return lines

    def _render_coupling_rows(
        self, top_pkgs: List[str], matrix: Dict, pkg_fan: Dict, lines: List[str]
    ) -> None:
        """Render one matrix row per source package."""
        col_w = max(max(len(p) for p in top_pkgs), 6)
        pad = max(len(p) for p in top_pkgs) + 2
        for src in top_pkgs:
            row_parts = _build_coupling_row(src, top_pkgs, matrix, col_w)
            tag = _coupling_row_tag(src, pkg_fan)
            lines.append(f"  {src:>{pad - 2}}  " + "  ".join(row_parts) + tag)

    def render_layers(self, ctx: Dict[str, Any]) -> List[str]:
        """Render LAYERS section — files grouped by package with metrics."""
        files = ctx["files"]
        packages = ctx["packages"]
        pkg_fan = ctx["pkg_fan"]
        dup_files = _dup_file_set(ctx)
        pkg_order = sorted(packages.keys(), key=lambda p: packages[p].get("avg_cc", 0), reverse=True)
        lines = ["LAYERS:"]
        for pkg in pkg_order:
            _render_layer_package(pkg, packages[pkg], pkg_fan, ctx, lines)
            self._render_layer_files(pkg, files, dup_files, lines)
            lines.append("  │")
        _render_zero_line_files(files, lines)
        return lines

    def _render_layer_files(
        self, pkg: str, files: Dict, dup_files: set, lines: List[str]
    ) -> None:
        """Render file rows for a single package in LAYERS."""
        pkg_files = [
            (fpath, fm)
            for fpath, fm in files.items()
            if fm["rel"].startswith(pkg + "/") or (pkg == "." and "/" not in fm["rel"])
        ]
        pkg_files.sort(key=lambda x: x[1]["lines"], reverse=True)
        for _fpath, fm in pkg_files:
            lines.append(_format_layer_file_row(fm, dup_files))

    def render_duplicates(self, ctx: Dict[str, Any]) -> List[str]:
        """Render duplicates section."""
        dupes = ctx["duplicates"]
        if not dupes:
            return ["DUPLICATES[0]: none"]
        lines = [f"DUPLICATES[{len(dupes)}]:"]
        for d in dupes:
            lines.append(f"  {d['class_name']}  {d['fileA']} ↔ {d['fileB']}")
            lines.append(f"    A: {d['countA']}m  {' '.join(d['methodsA'][:8])}")
            lines.append(f"    B: {d['countB']}m  {' '.join(d['methodsB'][:8])}")
            recommend = ""
            if d["diff"] == "IDENTICAL":
                recommend = " → rm B"
            elif d["diff"].startswith("A has"):
                recommend = " → keep A"
            elif d["diff"].startswith("B has"):
                recommend = " → keep B"
            lines.append(f"    DIFF: {d['diff']}{recommend}")
        return lines

    def render_functions(self, ctx: Dict[str, Any]) -> List[str]:
        """Render FUNCTIONS section — only CC >= threshold."""
        all_funcs = ctx["func_metrics"]
        critical = [f for f in all_funcs if f["cc"] >= CC_CRITICAL]
        total = len(all_funcs)
        dup_classes = {d["class_name"] for d in ctx["duplicates"]}
        if not critical:
            return [f"FUNCTIONS (CC≥{CC_CRITICAL}, 0 of {total}): none"]
        lines = [f"FUNCTIONS (CC≥{CC_CRITICAL}, {len(critical)} of {total}):"]
        for fm in critical[:MAX_FUNCTIONS_SHOWN]:
            lines.append(_format_function_row(fm, dup_classes))
        _render_cc_summary(all_funcs, total, lines)
        return lines

    def render_hotspots(self, ctx: Dict[str, Any]) -> List[str]:
        """Render hotspots section."""
        return render_hotspots_section(ctx)

    def render_classes(self, ctx: Dict[str, Any]) -> List[str]:
        """Render CLASSES section with visual bar chart."""
        return render_classes_section(ctx)

    def render_pipelines(self, ctx: Dict[str, Any]) -> List[str]:
        """Render PIPELINES section - data flow pipelines from entry points."""
        return render_pipelines_section(ctx)

    def render_external(self, ctx: Dict[str, Any]) -> List[str]:
        """Render EXTERNAL section - cross-references to other tools."""
        return render_external_section(ctx)
