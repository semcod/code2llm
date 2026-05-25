"""Coupling and layer rendering helpers extracted from ToonRenderer.

All functions are module-private and called exclusively from renderer.py.
"""

from typing import Any, Dict, List

from .constants import CC_CRITICAL, CC_WARNING, GOD_MODULE_LINES, MAX_COUPLING_PACKAGES


def _select_top_packages(matrix: Dict, pkg_fan: Dict) -> List[str]:
    """Select top packages by activity (fan-in + fan-out)."""
    all_pkgs = sorted({p for pair in matrix for p in pair})
    if not all_pkgs:
        return []
    pkg_activity = [
        (p, pkg_fan.get(p, {}).get("fan_in", 0) + pkg_fan.get(p, {}).get("fan_out", 0))
        for p in all_pkgs
    ]
    pkg_activity.sort(key=lambda x: x[1], reverse=True)
    return [p for p, _ in pkg_activity[:MAX_COUPLING_PACKAGES]]


def _render_coupling_header(top_pkgs: List[str]) -> List[str]:
    """Render coupling matrix header row."""
    col_w = max(max(len(p) for p in top_pkgs), 6)
    pad = max(len(p) for p in top_pkgs) + 2
    hdr = f"{'':>{pad}}  " + "  ".join(f"{p:>{col_w}}" for p in top_pkgs)
    return ["COUPLING:", hdr]


def _build_coupling_row(src: str, top_pkgs: List[str], matrix: Dict, col_w: int) -> List[str]:
    """Build cell values for a single coupling matrix row."""
    row_parts = []
    for dst in top_pkgs:
        if src == dst:
            row_parts.append(f"{'──':>{col_w}}")
        else:
            val = matrix.get((src, dst), 0)
            cell = str(val) if val else ""
            if not val:
                rev = matrix.get((dst, src), 0)
                cell = f"←{rev}" if rev else ""
            row_parts.append(f"{cell:>{col_w}}")
    return row_parts


def _coupling_row_tag(src: str, pkg_fan: Dict) -> str:
    """Determine row tag (hub / fan-out warning)."""
    fi = pkg_fan.get(src, {}).get("fan_in", 0)
    fo = pkg_fan.get(src, {}).get("fan_out", 0)
    if fi >= 5:
        return "  hub"
    if fo >= 8:
        return "  !! fan-out"
    return ""


def _render_coupling_summary(ctx: Dict[str, Any], pkg_fan: Dict, lines: List[str]) -> None:
    """Render coupling summary: cycles, hubs, smells."""
    ncycles = len(ctx["cycles"])
    lines.append(f"  CYCLES: {'none' if ncycles == 0 else ncycles}")
    for h, d in pkg_fan.items():
        if d.get("fan_in", 0) >= 5:
            lines.append(f"  HUB: {h}/ (fan-in={d['fan_in']})")
    for s, d in pkg_fan.items():
        if d.get("fan_out", 0) >= 8:
            lines.append(f"  SMELL: {s}/ fan-out={d['fan_out']} → split needed")


def _render_layer_package(pkg: str, pd: Dict, pkg_fan: Dict, ctx: Dict, lines: List[str]) -> None:
    """Render a single package header line in LAYERS."""
    fi = pkg_fan.get(pkg, {}).get("fan_in", 0)
    fo = pkg_fan.get(pkg, {}).get("fan_out", 0)
    markers = "  !! split" if fo >= 8 else ""
    pkg_dups = any(
        d["fileA"].startswith(pkg + "/") or d["fileB"].startswith(pkg + "/")
        for d in ctx["duplicates"]
    )
    if pkg_dups:
        markers += "  ×DUP"
    lines.append(f"  {pkg + '/':30s}  CC̄={pd['avg_cc']:<5}  ←in:{fi}  →out:{fo}{markers}")


def _format_layer_file_row(fm: Dict, dup_files: set) -> str:
    """Format a single file row in LAYERS section."""
    rel = fm["rel"]
    short = rel.split("/")[-1] if "/" in rel else rel
    if short.endswith(".py"):
        short = short[:-3]
    lc, mcc, fin = fm["lines"], fm["max_cc"], fm["fan_in"]
    severity = (
        "!! "
        if (lc >= GOD_MODULE_LINES or mcc >= CC_WARNING)
        else ("!  " if mcc >= CC_CRITICAL else "")
    )
    dup_mark = "  ×DUP" if rel in dup_files else ""
    return (
        f"  │ {severity}{short:24s} {lc:>5}L  {fm['class_count']}C  {fm['methods']:>3}m"
        f"  CC={mcc:<5}  ←{fin}{dup_mark}"
    )


def _render_zero_line_files(files: Dict, lines: List[str]) -> None:
    """Render zero-line files at the end of LAYERS."""
    zero = [(fpath, fm) for fpath, fm in files.items() if fm["lines"] == 0]
    if zero:
        lines.append("  ── zero ──")
        for _fpath, fm in sorted(zero, key=lambda x: x[1]["rel"]):
            lines.append(f"     {fm['rel']:40s}  0L")


def _format_function_row(fm: Dict, dup_classes: set) -> str:
    """Format a single function row."""
    display = f"{fm['class_name']}.{fm['name']}" if fm["class_name"] else fm["name"]
    traits = "+".join(fm["traits"]) if fm["traits"] else ""
    exits_s = f"{fm['exits']}exit" if fm["exits"] else ""
    markers = ""
    if fm["class_name"] and fm["class_name"] in dup_classes:
        markers += "  ×DUP"
    if fm["cc"] >= CC_WARNING:
        markers += "  !! split"
    return (
        f"  {fm['cc']:>5.1f}  {display:40s}  {fm['nodes']:>3}n"
        f"  {exits_s:>6s}  {traits}{markers}"
    )


def _render_cc_summary(all_funcs: List[Dict], total: int, lines: List[str]) -> None:
    """Render CC distribution summary."""
    from .constants import CC_HIGH
    cc_bins = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for f in all_funcs:
        if f["cc"] >= CC_CRITICAL:
            cc_bins["critical"] += 1
        elif f["cc"] >= CC_HIGH:
            cc_bins["high"] += 1
        elif f["cc"] >= 2:
            cc_bins["medium"] += 1
        else:
            cc_bins["low"] += 1
    pct_crit = round(cc_bins["critical"] / total * 100) if total else 0
    pct_high = round((cc_bins["critical"] + cc_bins["high"]) / total * 100) if total else 0
    lines.append("")
    lines.append("  summary:")
    lines.append(
        f"    critical(≥{CC_CRITICAL}): {cc_bins['critical']}"
        f" | high({CC_HIGH}-{CC_CRITICAL}): {cc_bins['high']}"
        f" | medium(2-{CC_HIGH}): {cc_bins['medium']}"
        f" | low(<2): {cc_bins['low']}"
    )
    lines.append(f"    {pct_crit}% CC≥{CC_CRITICAL}  {pct_high}% CC≥{CC_HIGH}")
