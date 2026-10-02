"""TOON format parser for plain-text and YAML variants."""
import re
from pathlib import Path
from typing import Dict, Any, Union, List
import yaml

from .models import ToonDocument, ToonHeader, FunctionEntry


def is_toon_file(filepath: Union[str, Path]) -> bool:
    """Check if file is TOON format based on extension or content."""
    path = Path(filepath)
    if path.suffix in [".toon", ".toon.yaml"] or ".toon." in path.name:
        return True
    try:
        with open(path, "r", encoding="utf-8") as f:
            first_line = f.readline()
            return first_line.startswith("# ") and (
                "func" in first_line or "CC" in first_line or "code2llm" in first_line
            )
    except Exception:
        return False


def parse_toon_content(content: str) -> Dict[str, Any]:
    """Parse TOON plain-text content into a structured dictionary."""
    data: Dict[str, Any] = {
        "meta": {},
        "stats": {},
        "health": [],
        "functions": [],
        "classes": [],
        "hotspots": [],
    }

    current_section = None
    lines = content.splitlines()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if line.startswith("# "):
            if "CC̄" in line or "CC=" in line or "critical:" in line:
                _parse_stats_line(line, data)
            elif not data["meta"].get("project"):
                _parse_header_line(line, data)
            continue

        if re.match(r"^[A-Z_]+(\[\d*\])?:", stripped):
            sec_name = stripped.split("[")[0].split(":")[0].lower()
            current_section = sec_name
            continue

        if current_section == "health":
            if any(marker in stripped for marker in ("🔴", "🟡", "!", "critical", "warning")):
                data["health"].append(stripped)
        elif current_section == "functions":
            if not stripped.startswith("summary:"):
                parts = stripped.split()
                if len(parts) >= 2:
                    try:
                        cc = float(parts[0])
                        data["functions"].append({"name": parts[1], "cc": cc})
                    except ValueError:
                        pass
        elif current_section == "classes":
            parts = stripped.split()
            if parts and not parts[0].startswith("█"):
                data["classes"].append({"name": parts[0]})
        elif current_section == "hotspots":
            if stripped.startswith("#"):
                parts = stripped.split()
                if len(parts) >= 2:
                    data["hotspots"].append({"name": parts[1]})

    return data


def _parse_header_line(line: str, data: Dict[str, Any]) -> None:
    parts = line[2:].strip().split("|")
    if parts:
        data["meta"]["project"] = parts[0].strip()
    if len(parts) > 1:
        data["meta"]["generated"] = parts[-1].strip()


def _parse_stats_line(line: str, data: Dict[str, Any]) -> None:
    parts = line[2:].strip().split("|")
    for part in parts:
        part = part.strip()
        if "critical:" in part:
            data["stats"]["critical"] = part.split(":")[-1].strip()
        elif "dups:" in part:
            data["stats"]["duplicates"] = part.split(":")[-1].strip()
        elif "cycles:" in part:
            data["stats"]["cycles"] = part.split(":")[-1].strip()
        elif "CC̄=" in part or "CC=" in part:
            data["stats"]["mean_cc"] = part.split("=")[-1].strip()


def load_toon(filepath: Union[str, Path]) -> Dict[str, Any]:
    """Load and parse a TOON file (auto-detecting YAML vs plain-text format)."""
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")

    if path.name.endswith(".yaml") or path.name.endswith(".yml"):
        try:
            yaml_data = yaml.safe_load(content)
            if isinstance(yaml_data, dict):
                return yaml_data
        except Exception:
            pass

    return parse_toon_content(content)


def load_toon_document(filepath: Union[str, Path]) -> ToonDocument:
    """Load a TOON file and return a strongly-typed ToonDocument."""
    raw = load_toon(filepath)
    doc = ToonDocument(raw_data=raw)

    stats = raw.get("stats", {})
    doc.header.project = raw.get("meta", {}).get("project", "")
    try:
        doc.header.mean_cc = float(stats.get("mean_cc", 0.0))
        doc.header.critical_count = int(stats.get("critical", 0))
        doc.header.duplicate_count = int(stats.get("duplicates", 0))
        doc.header.cycle_count = int(stats.get("cycles", 0))
    except (ValueError, TypeError):
        pass

    doc.health = list(raw.get("health", []))
    for f in raw.get("functions", []):
        if isinstance(f, dict):
            doc.functions.append(FunctionEntry(name=f.get("name", ""), cc=float(f.get("cc", 0.0))))
        elif isinstance(f, str):
            doc.functions.append(FunctionEntry(name=f, cc=0.0))

    for c in raw.get("classes", []):
        if isinstance(c, dict):
            doc.classes.append(c.get("name", ""))
        elif isinstance(c, str):
            doc.classes.append(c)

    for h in raw.get("hotspots", []):
        if isinstance(h, dict):
            doc.hotspots.append(h.get("name", ""))
        elif isinstance(h, str):
            doc.hotspots.append(h)

    return doc
