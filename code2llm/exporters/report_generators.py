"""Report generators — produce views from project.yaml (single source of truth).

Thin re-export module. Actual generators live in separate files:
  toon_view.py      → ToonViewGenerator     → project.toon.yaml
  context_view.py   → ContextViewGenerator  → context.md
  article_view.py   → ArticleViewGenerator  → status.md
  html_dashboard.py → HTMLDashboardGenerator → dashboard.html
"""

import yaml
from typing import Any, Dict

from .toon_view import ToonViewGenerator
from .context_view import ContextViewGenerator
from .article_view import ArticleViewGenerator
from .html_dashboard import HTMLDashboardGenerator


def _read_yaml_content(path: str) -> str:
    """Read raw file content or raise ValueError."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        raise ValueError(f"project.yaml not found: {path}")
    except Exception as e:
        raise ValueError(f"Cannot read project.yaml ({path}): {e}")
    if not content.strip():
        raise ValueError(f"project.yaml is empty: {path}")
    return content


def _parse_yaml_content(content: str, path: str) -> Any:
    """Parse YAML string or raise descriptive ValueError."""
    from yaml.scanner import ScannerError
    from yaml.parser import ParserError
    try:
        return yaml.safe_load(content)
    except ScannerError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else "?"
        col = e.problem_mark.column if e.problem_mark else "?"
        raise ValueError(
            f"YAML syntax error in {path} at line {line}, column {col}: {e.problem}\n"
            f"Hint: Check indentation and special characters (:, -, #)"
        )
    except ParserError as e:
        line = e.problem_mark.line + 1 if e.problem_mark else "?"
        raise ValueError(
            f"YAML parse error in {path} at line {line}: {e.problem}\n"
            f"Hint: Verify YAML structure (mapping vs list)"
        )
    except Exception as e:
        raise ValueError(f"YAML error in {path}: {e}")


def _validate_yaml_data(data: Any, path: str) -> None:
    """Raise ValueError if data fails structural validation."""
    if data is None:
        raise ValueError(f"project.yaml is null/empty: {path}")
    if not isinstance(data, dict):
        raise ValueError(
            f"Invalid project.yaml: expected dict/object, got {type(data).__name__} in {path}\n"
            f"Hint: YAML must start with key-value pairs, not a list"
        )
    if "version" not in data:
        raise ValueError(
            f"Invalid project.yaml: missing required 'version' key in {path}\n"
            f"Required keys: version, project, analysis\n"
            f"Found keys: {list(data.keys())[:10]}"
        )


def load_project_yaml(path: str) -> Dict[str, Any]:
    """Load and validate project.yaml with detailed error reporting."""
    content = _read_yaml_content(path)
    data = _parse_yaml_content(content, path)
    _validate_yaml_data(data, path)
    return data


__all__ = [
    "load_project_yaml",
    "ToonViewGenerator",
    "ContextViewGenerator",
    "ArticleViewGenerator",
    "HTMLDashboardGenerator",
]
