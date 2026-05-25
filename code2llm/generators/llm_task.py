# ── llm_task.py overview ──────────────────────────────────────────────────────
# Module: CLI tool and library for loading, normalising, and parsing LLM task files.
# ── Utility helpers ───────────────────────────────────────────────────────────
# _strip_bom()            : remove UTF-8 BOM from raw string.
# _ensure_list()          : coerce scalar/None to list.
# _deep_get()             : safe nested dict access via key path tuple.
# _sec() / _sget()        : dict helpers with dict/str default values.
# ── Normalisation ─────────────────────────────────────────────────────────────
# normalize_llm_task()    : canonicalise raw task dict to required schema.
# ── Text parser ───────────────────────────────────────────────────────────────
# _parse_bullets()        : extract bullet-point items from a line list.
# _parse_sections()       : split text into named sections by heading patterns.
# _create_empty_task_data(): baseline empty task dict for parser output.
# _apply_simple_sections(): populate scalar section fields from parsed sections.
# _apply_bullet_sections(): populate list section fields from parsed sections.
# _parse_acceptance_tests(): extract Given/When/Then rows from acceptance section.
# parse_llm_task_text()   : orchestrate above parsers; return normalised dict.
# ── File loaders ──────────────────────────────────────────────────────────────
# _load_yaml() / _load_json(): parse raw text; raise on invalid syntax.
# load_input()            : auto-detect format by extension; return task dict.
# ── CLI ───────────────────────────────────────────────────────────────────────
# create_parser()         : build argparse parser for llm_task CLI.
# main()                  : CLI entry point; load → normalise → print JSON.

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

from ._utils import dump_yaml


def _strip_bom(text: str) -> str:
    """Strip UTF-8 BOM from the start of text if present."""
    return text[1:] if text.startswith("\ufeff") else text


def _ensure_list(value: Any) -> List[Any]:
    """Wrap scalar value in a list; return value unchanged if already a list."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _deep_get(d: Dict[str, Any], path: Tuple[str, ...]) -> Any:
    cur: Any = d
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def _sec(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Return data[key] as a dict, falling back to empty dict."""
    v = data.get(key)
    return v if isinstance(v, dict) else {}


def _sget(d: Dict[str, Any], key: str, default: str = "") -> str:
    """Return d[key] as a non-empty string, falling back to default."""
    v = d.get(key)
    return v if isinstance(v, str) and v else default


def normalize_llm_task(data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalise a raw LLM task dict into a canonical structure with all required keys."""
    task = _sec(data, "task")
    ctx = _sec(data, "context")
    deliv = _sec(data, "deliverables")
    ifaces = _sec(data, "interfaces")
    rules = _sec(data, "rules")
    accept = _sec(data, "acceptance")
    notes = _sec(data, "notes_for_llm")
    return {
        "task": {"title": _sget(task, "title"), "one_line_goal": _sget(task, "one_line_goal")},
        "context": {
            "product_area": _sget(ctx, "product_area"),
            "current_behavior": _sget(ctx, "current_behavior"),
            "desired_behavior": _sget(ctx, "desired_behavior"),
        },
        "deliverables": {
            "language": _sget(deliv, "language", "any"),
            "must_generate": _ensure_list(deliv.get("must_generate")),
            "files_to_create_or_edit": _ensure_list(deliv.get("files_to_create_or_edit")),
        },
        "interfaces": {
            "inputs": _ensure_list(ifaces.get("inputs")),
            "outputs": _ensure_list(ifaces.get("outputs")),
        },
        "rules": {
            "must": _ensure_list(rules.get("must")),
            "must_not": _ensure_list(rules.get("must_not")),
            "assumptions": _ensure_list(rules.get("assumptions")),
            "edge_cases": _ensure_list(rules.get("edge_cases")),
            "performance": _ensure_list(rules.get("performance")),
        },
        "acceptance": {
            "tests": _ensure_list(accept.get("tests")),
            "done_definition": _ensure_list(accept.get("done_definition")),
        },
        "examples": _ensure_list(data.get("examples")),
        "notes_for_llm": {
            "constraints": _ensure_list(notes.get("constraints")),
            "style": _ensure_list(notes.get("style")),
            "language_specific_hints": _ensure_list(notes.get("language_specific_hints")),
        },
    }


_SECTION_KEYS = {
    "TITLE": ("task", "title"),
    "GOAL": ("task", "one_line_goal"),
    "PRODUCT_AREA": ("context", "product_area"),
    "CURRENT": ("context", "current_behavior"),
    "DESIRED": ("context", "desired_behavior"),
}


def _parse_bullets(lines: List[str]) -> List[str]:
    items: List[str] = []
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        if s.startswith("-"):
            items.append(s[1:].strip())
        else:
            items.append(s)
    return items


def _parse_sections(lines: List[str]) -> Dict[str, List[str]]:
    """Parse text lines into sections based on headers."""
    sections: Dict[str, List[str]] = {}
    current: Optional[str] = None

    def start_section(name: str) -> None:
        nonlocal current
        current = name
        sections.setdefault(name, [])

    _SECTION_HEADERS = {
        "TITLE",
        "GOAL",
        "CURRENT",
        "DESIRED",
        "INPUTS",
        "OUTPUTS",
        "RULES (MUST)",
        "RULES (MUST NOT)",
        "EDGE CASES",
        "ACCEPTANCE TESTS",
        "DELIVERABLES",
    }

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current is not None:
                sections[current].append("")
            continue

        upper = stripped.upper()
        if upper.endswith(":"):
            key = upper[:-1].strip()
            if key in _SECTION_HEADERS:
                start_section(key)
                continue

        if current is None:
            continue
        sections[current].append(line)

    return sections


def _create_empty_task_data() -> Dict[str, Any]:
    """Create empty task data structure."""
    return {
        "task": {"title": "", "one_line_goal": ""},
        "context": {"product_area": "", "current_behavior": "", "desired_behavior": ""},
        "deliverables": {
            "language": "any",
            "must_generate": [],
            "files_to_create_or_edit": [],
        },
        "interfaces": {"inputs": [], "outputs": []},
        "rules": {
            "must": [],
            "must_not": [],
            "assumptions": [],
            "edge_cases": [],
            "performance": [],
        },
        "acceptance": {"tests": [], "done_definition": []},
        "examples": [],
        "notes_for_llm": {
            "constraints": [],
            "style": [],
            "language_specific_hints": [],
        },
    }


def _apply_simple_sections(
    sections: Dict[str, List[str]], data: Dict[str, Any]
) -> None:
    """Apply simple section key mappings to data."""
    for section_name, path in _SECTION_KEYS.items():
        content_lines = sections.get(section_name)
        if not content_lines:
            continue
        value = "\n".join(content_lines).strip()
        if value:
            parent = data
            for key in path[:-1]:
                parent = parent[key]
            parent[path[-1]] = value


def _apply_bullet_sections(
    sections: Dict[str, List[str]], data: Dict[str, Any]
) -> None:
    """Apply bullet list sections to data."""
    if sections.get("INPUTS"):
        data["interfaces"]["inputs"] = _parse_bullets(sections["INPUTS"])
    if sections.get("OUTPUTS"):
        data["interfaces"]["outputs"] = _parse_bullets(sections["OUTPUTS"])
    if sections.get("RULES (MUST)"):
        data["rules"]["must"] = _parse_bullets(sections["RULES (MUST)"])
    if sections.get("RULES (MUST NOT)"):
        data["rules"]["must_not"] = _parse_bullets(sections["RULES (MUST NOT)"])
    if sections.get("EDGE CASES"):
        data["rules"]["edge_cases"] = _parse_bullets(sections["EDGE CASES"])


def _parse_acceptance_tests(sections: Dict[str, List[str]]) -> List[Dict[str, str]]:
    """Parse acceptance tests section into structured format."""
    if not sections.get("ACCEPTANCE TESTS"):
        return []
    tests: List[Dict[str, str]] = []
    raw_items = _parse_bullets(sections["ACCEPTANCE TESTS"])
    for idx, item in enumerate(raw_items, 1):
        tests.append({"name": f"test_{idx}", "given": "", "when": "", "then": item})
    return tests


def parse_llm_task_text(text: str) -> Dict[str, Any]:
    """Parse LLM task text into structured data."""
    text = _strip_bom(text)
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    sections = _parse_sections(lines)
    data = _create_empty_task_data()

    _apply_simple_sections(sections, data)
    _apply_bullet_sections(sections, data)

    data["acceptance"]["tests"] = _parse_acceptance_tests(sections)

    if sections.get("DELIVERABLES"):
        data["deliverables"]["must_generate"] = _parse_bullets(sections["DELIVERABLES"])

    return data


def _load_yaml(raw: str, path: Path) -> Dict[str, Any]:
    """Parse *raw* as YAML with detailed error reporting tied to *path*."""
    from yaml.scanner import ScannerError
    from yaml.parser import ParserError

    try:
        loaded = yaml.safe_load(raw)
    except ScannerError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else "?"
        col = e.problem_mark.column if e.problem_mark else "?"
        raise ValueError(
            f"YAML syntax error at line {line}, column {col}: {e.problem}\n"
            f"Hint: Check indentation in {path}"
        )
    except ParserError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else "?"
        raise ValueError(
            f"YAML parse error at line {line}: {e.problem}\n"
            f"Hint: Verify YAML structure in {path}"
        )
    except Exception as e:
        raise ValueError(f"YAML error in {path}: {e}")

    if loaded is None:
        raise ValueError(f"YAML file is null/empty: {path}")
    if not isinstance(loaded, dict):
        raise ValueError(
            f"YAML must be a mapping/object, got {type(loaded).__name__} in {path}\n"
            f"Hint: File should start with 'key: value' pairs"
        )
    return loaded


def _load_json(raw: str, path: Path) -> Dict[str, Any]:
    """Parse *raw* as JSON with validation tied to *path*."""
    import json

    loaded = json.loads(raw)
    if not isinstance(loaded, dict):
        raise ValueError("JSON input must be an object at top level")
    return loaded


def load_input(path: Path) -> Dict[str, Any]:
    """Load input file with detailed YAML/JSON error reporting."""
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"Input file not found: {path}")
    except Exception as e:
        raise ValueError(f"Cannot read input file {path}: {e}")

    raw = _strip_bom(raw)

    if not raw.strip():
        raise ValueError(f"Input file is empty: {path}")

    suffix = path.suffix.lower()
    if suffix in {".yaml", ".yml"}:
        return _load_yaml(raw, path)
    if suffix == ".json":
        return _load_json(raw, path)

    return parse_llm_task_text(raw)


def create_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser for the LLM task generator."""
    p = argparse.ArgumentParser(
        prog="llm-task-generator",
        description="Generate normalized llm_task.yaml from simplified task spec (text/YAML/JSON).",
    )
    p.add_argument(
        "-i", "--input", required=True, help="Input file: .txt/.md/.yaml/.yml/.json"
    )
    p.add_argument("-o", "--output", required=True, help="Output YAML file path")
    p.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate/normalize input; do not write output file",
    )
    return p


def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for the LLM task generator CLI."""
    args = create_parser().parse_args(argv)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 2

    data = load_input(input_path)

    if "task" not in data:
        data = {"task": data}

    normalized = normalize_llm_task(data)

    if args.validate_only:
        sys.stdout.write(dump_yaml(normalized))
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(dump_yaml(normalized), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
