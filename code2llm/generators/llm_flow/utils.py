"""LLM Flow utilities — YAML reading and type coercion helpers."""

from pathlib import Path
from typing import Any, Dict, List

import yaml


_FUNC_LABEL_PREFIX = "FUNC:"
_CALL_LABEL_PREFIX = "CALL "


def _strip_bom(text: str) -> str:
    """Strip UTF-8 BOM from text if present."""
    return text[1:] if text.startswith("\ufeff") else text


def _read_yaml_raw(path: Path) -> str:
    """Read file content, strip BOM, or raise ValueError."""
    try:
        raw = _strip_bom(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Cannot read file {path}: {e}")
    if not raw.strip():
        raise ValueError(f"File is empty: {path}")
    return raw


def _parse_yaml_safe(raw: str, path: Path) -> Any:
    """Parse YAML or raise descriptive ValueError."""
    from yaml.scanner import ScannerError
    from yaml.parser import ParserError
    try:
        return yaml.safe_load(raw)
    except ScannerError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else "?"
        col = e.problem_mark.column if e.problem_mark else "?"
        raise ValueError(
            f"YAML syntax error in {path} at line {line}, column {col}: {e.problem}\n"
            f"Hint: Check indentation, avoid tabs, watch special characters (:, -, #)"
        )
    except ParserError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else "?"
        raise ValueError(
            f"YAML parse error in {path} at line {line}: {e.problem}\n"
            f"Hint: Verify structure - are you using list where dict expected?"
        )
    except Exception as e:
        raise ValueError(f"YAML error in {path}: {e}")


def _validate_yaml_mapping(loaded: Any, path: Path) -> None:
    """Raise ValueError if loaded is not a non-None dict."""
    if loaded is None:
        raise ValueError(f"File is null/empty YAML: {path}")
    if not isinstance(loaded, dict):
        raise ValueError(
            f"Expected YAML mapping (dict), got {type(loaded).__name__} in {path}\n"
            f"Hint: File must start with 'key: value' pairs, not a list"
        )


def _safe_read_yaml(path: Path) -> Dict[str, Any]:
    """Read YAML file safely, handling BOM and type validation with detailed errors."""
    raw = _read_yaml_raw(path)
    loaded = _parse_yaml_safe(raw, path)
    _validate_yaml_mapping(loaded, path)
    return loaded


def _as_dict(d: Any) -> Dict[str, Any]:
    """Coerce value to dict, returning empty dict if not a mapping."""
    return d if isinstance(d, dict) else {}


def _as_list(v: Any) -> List[Any]:
    """Coerce value to list, returning empty list if not a list."""
    return v if isinstance(v, list) else []


def _shorten(s: str, max_len: int) -> str:
    """Shorten string to max_len, adding ellipsis if truncated."""
    s = (s or "").strip()
    if len(s) <= max_len:
        return s
    return s[: max(0, max_len - 1)].rstrip() + "…"


__all__ = [
    "_FUNC_LABEL_PREFIX",
    "_CALL_LABEL_PREFIX",
    "_strip_bom",
    "_safe_read_yaml",
    "_as_dict",
    "_as_list",
    "_shorten",
]
