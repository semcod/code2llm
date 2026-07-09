"""Helper utilities for TOON exporter."""

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Set

from code2llm.core.models import AnalysisResult, FunctionInfo
from code2llm.exporters.flow_constants import is_excluded_path, is_intentional_duplicate_copy

# Re-export is_excluded_path from flow_constants to eliminate duplication


def _is_excluded(path: str) -> bool:
    """Return True if the given file path should be excluded from duplicate analysis."""
    return is_excluded_path(path)


@lru_cache(maxsize=4096)
def _rel_path(fpath: str, project_path: str) -> str:
    """Return fpath relative to project_path, or fpath unchanged if resolution fails."""
    if not project_path or not fpath:
        return fpath or ""
    try:
        return str(Path(fpath).relative_to(Path(project_path).resolve()))
    except (ValueError, RuntimeError):
        try:
            return str(Path(fpath).relative_to(Path(project_path)))
        except (ValueError, RuntimeError):
            return fpath


def _package_of(rel_path: str) -> str:
    """Extract top-level package/directory from relative path."""
    parts = Path(rel_path).parts
    if len(parts) >= 2:
        return parts[0]
    # root-level .py files → group under "."
    return "."


def _package_of_module(module_name: str) -> str:
    """Return subpackage for coupling analysis.

    For 'code2llm.exporters.toon' returns 'code2llm.exporters'
    so cross-subpackage coupling is detected.
    """
    parts = module_name.split(".")
    if len(parts) >= 3:
        return ".".join(parts[:2])  # e.g. code2llm.exporters
    if len(parts) == 2:
        return parts[0]
    return parts[0] if parts else ""


def _traits_from_cfg(fi: FunctionInfo, result: AnalysisResult) -> list:
    """Derive structural trait labels (loops/cond/ret) from a function's CFG nodes."""
    traits = []
    node_types = set()
    for nid in fi.cfg_nodes or []:
        nd = result.nodes.get(nid)
        if nd:
            node_types.add(getattr(nd, "type", ""))
    if node_types & {"FOR", "WHILE"}:
        traits.append("loops")
    if "IF" in node_types:
        traits.append("cond")
    if "RETURN" in node_types:
        traits.append("ret")
    return traits


def _dup_file_set(ctx: Dict[str, Any]) -> Set[str]:
    """Return the set of file paths that appear in at least one duplicate pair."""
    s: Set[str] = set()
    for d in ctx["duplicates"]:
        s.add(d["fileA"])
        s.add(d["fileB"])
    return s


def _hotspot_description(fi: FunctionInfo, fan_out: int) -> str:
    """Generate a short human-readable description for a hotspot function."""
    if fi.name == "to_dict":
        return f"{fan_out} conditional field serializations"
    if "format" in fi.name.lower() or "dispatch" in fi.name.lower():
        return f"{fan_out}-way dispatch"
    if "export" in fi.name.lower():
        return f"export with {fan_out} outputs"
    if "analyze" in fi.name.lower() or "process" in fi.name.lower():
        return f"analysis pipeline, {fan_out} stages"
    if fi.class_name:
        return f"{fi.class_name} method, fan-out={fan_out}"
    return f"calls {fan_out} functions"


_WALK_EXCLUDE = {"venv", ".venv", "node_modules", "__pycache__", ".git", "dist", "build", ".tox", ".mypy_cache", "egg-info"}  # noqa: E501


def _fast_line_counts(pp: Path, result) -> Dict[str, int]:
    """Derive line counts from already-parsed AnalysisResult modules."""
    counts: Dict[str, int] = {}
    for _mname, mi in getattr(result, "modules", {}).items():
        if not mi.file:
            continue
        try:
            lc = len(Path(mi.file).read_text(encoding="utf-8", errors="ignore").splitlines())
            counts[mi.file] = lc
            counts[str(Path(mi.file).relative_to(pp))] = lc
        except Exception:
            pass
    return counts


def _slow_line_counts(pp: Path) -> Dict[str, int]:
    """Scan disk for line counts when AnalysisResult is unavailable."""
    from ...core.config import ALL_EXTENSIONS
    ext_set = set(ALL_EXTENSIONS)
    counts: Dict[str, int] = {}
    for root, dirs, files in (pp.walk() if hasattr(pp, "walk") else _walk_compat(pp)):
        dirs[:] = [d for d in dirs if d not in _WALK_EXCLUDE]
        for fname in files:
            if Path(fname).suffix not in ext_set:
                continue
            src = root / fname
            try:
                lc = len(src.read_text(encoding="utf-8", errors="ignore").splitlines())
                counts[str(src)] = lc
                counts[str(src.relative_to(pp))] = lc
            except Exception:
                pass
    return counts


def _scan_line_counts(project_path, result=None) -> Dict[str, int]:
    """Get line counts for project files.

    Fast path: derive from AnalysisResult modules (already parsed, no extra I/O).
    Slow fallback: single os.walk pass reading files from disk.
    """
    if not project_path:
        return {}
    pp = Path(project_path)
    if not pp.is_dir():
        return {}
    if result is not None:
        return _fast_line_counts(pp, result)
    return _slow_line_counts(pp)


def _walk_compat(path):
    """os.walk compatibility wrapper for Path (Python < 3.12)."""
    import os

    for root, dirs, files in os.walk(path):
        yield Path(root), dirs, files
