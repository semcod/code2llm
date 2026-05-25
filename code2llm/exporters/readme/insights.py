"""README insights extraction — parse analysis files for health metrics."""

from pathlib import Path
from typing import Any, Dict


def _parse_toon_metrics(content: str) -> Dict[str, Any]:
    """Parse critical/god/health flags from analysis.toon text content."""
    result: Dict[str, Any] = {"critical_functions": 0, "god_modules": 0, "has_health_issues": False}
    for line in content.split("\n"):
        if "critical:" in line:
            try:
                result["critical_functions"] = int(line.split("critical:")[1].split("/")[0].strip())
            except (ValueError, IndexError):
                pass
        elif "GOD" in line and "🔴" in line:
            result["god_modules"] += 1
        elif line.strip().startswith("🔴"):
            result["has_health_issues"] = True
    return result


def _parse_evolution_actions(content: str) -> int:
    """Count numbered refactoring steps in evolution.toon.yaml content."""
    return sum(
        1 for line in content.split("\n")
        if line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9."))
    )


def extract_insights(output_dir: Path) -> Dict[str, Any]:
    """Extract insights from existing analysis files."""
    insights: Dict[str, Any] = {
        "critical_functions": 0,
        "god_modules": 0,
        "refactoring_actions": 0,
        "has_health_issues": False,
        "has_evolution_plan": False,
    }
    toon_path = output_dir / "analysis.toon"
    if toon_path.exists():
        try:
            insights.update(_parse_toon_metrics(toon_path.read_text(encoding="utf-8")))
        except Exception:
            pass
    evo_path = output_dir / "evolution.toon.yaml"
    if evo_path.exists():
        try:
            content = evo_path.read_text(encoding="utf-8")
            if "REFACTOR[" in content:
                insights["refactoring_actions"] = _parse_evolution_actions(content)
                insights["has_evolution_plan"] = True
        except Exception:
            pass
    return insights


__all__ = ["extract_insights"]
