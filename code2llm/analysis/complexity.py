"""Cyclomatic complexity and code metric calculation engine.

Decoupled pure atom supporting:
- Python AST complexity analysis (via Radon cc_visit / cc_rank)
- Multi-language regex estimation (c_family, go, rust, typescript, php)
- Zero-overhead native Rust acceleration (code2llm-fast-core) with transparent Python fallback.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict

from code2llm.core.config import (
    CC_HIGH_THRESHOLD,
    CC_LOW_THRESHOLD,
    CC_MEDIUM_THRESHOLD,
)

CC_PATTERNS = {
    "c_family": re.compile(
        r"\b(?:if|else\s+if|for|while|do|switch|case|catch)\b"
        r"|&&|\|\||\?\?|\?\."
        r"|\?\s*[^:]*\s*:"
    ),
    "go": re.compile(
        r"\b(?:if|for|switch|case|select|go|defer)\b"
        r"|&&|\|\|"
    ),
    "rust": re.compile(
        r"\b(?:if|else\s+if|for|while|loop|match)\b"
        r"|&&|\|\||\?"
    ),
}

_RUST_BIN_NAME = "code2llm-fast-core"


def _find_rust_binary() -> Path | None:
    """Find native code2llm-fast-core binary if compiled."""
    # 1. Environment variable override
    env_path = os.environ.get("CODE2LLM_FAST_CORE_BIN")
    if env_path:
        p = Path(env_path)
        if p.is_file() and os.access(p, os.X_OK):
            return p

    # 2. Local packages build in workspace
    current_file = Path(__file__).resolve()
    repo_root = current_file.parents[2]
    candidate = repo_root / "packages" / "code2llm-fast-core" / "target" / "release" / _RUST_BIN_NAME
    if candidate.is_file() and os.access(candidate, os.X_OK):
        return candidate

    debug_candidate = repo_root / "packages" / "code2llm-fast-core" / "target" / "debug" / _RUST_BIN_NAME
    if debug_candidate.is_file() and os.access(debug_candidate, os.X_OK):
        return debug_candidate

    # 3. System PATH
    system_path = shutil.which(_RUST_BIN_NAME)
    if system_path:
        return Path(system_path)

    return None


def extract_function_body(content: str, start_line: int) -> str:
    """Extract the body of a function between braces from a start line (1-indexed)."""
    lines = content.split("\n")
    if start_line < 1 or start_line > len(lines):
        return ""
    depth = 0
    body_lines = []
    started = False
    for line in lines[start_line - 1 :]:
        for ch in line:
            if ch == "{":
                depth += 1
                started = True
            elif ch == "}":
                depth -= 1
        if started:
            body_lines.append(line)
        if started and depth <= 0:
            break
    return "\n".join(body_lines)


def compute_cc_rank(cc: int) -> str:
    """Determine cyclomatic complexity rank (A, B, C, D) from threshold."""
    if cc <= CC_LOW_THRESHOLD:
        return "A"
    if cc <= CC_MEDIUM_THRESHOLD:
        return "B"
    if cc <= CC_HIGH_THRESHOLD:
        return "C"
    return "D"


def compute_cyclomatic_complexity(body: str, lang: str = "c_family") -> int:
    """Compute McCabe cyclomatic complexity for a given code block."""
    if not body:
        return 1
    pattern = CC_PATTERNS.get(lang, CC_PATTERNS["c_family"])
    return 1 + len(pattern.findall(body))


def estimate_function_complexity(
    content: str, start_line: int, lang: str = "c_family"
) -> tuple[int, str]:
    """Estimate cyclomatic complexity and rank for a function starting at line."""
    body = extract_function_body(content, start_line)
    cc = compute_cyclomatic_complexity(body, lang=lang)
    rank = compute_cc_rank(cc)
    return cc, rank


def _rust_batch_complexity(
    lines: list[int],
    lang: str = "c_family",
    file_path: str | None = None,
    content: str | None = None,
) -> dict[int, tuple[int, str]] | None:
    """Call native Rust binary for fast batch complexity calculation."""
    binary = _find_rust_binary()
    if not binary or not lines:
        return None

    lines_arg = ",".join(str(l) for l in lines)
    cmd = [str(binary), "--lang", lang, "--lines", lines_arg]

    try:
        if file_path and Path(file_path).is_file():
            cmd.extend(["--file", str(file_path)])
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=5,
            )
        elif content is not None:
            proc = subprocess.run(
                cmd,
                input=content,
                capture_output=True,
                text=True,
                check=True,
                timeout=5,
            )
        else:
            return None

        data = json.loads(proc.stdout.strip())
        result: dict[int, tuple[int, str]] = {}
        for item in data:
            result[item["line"]] = (item["cc"], item["rank"])
        return result
    except Exception:
        return None


def calculate_complexity_regex(
    content: str,
    result: Dict[str, Any],
    lang: str = "c_family",
    file_path: str | None = None,
) -> None:
    """Estimate cyclomatic complexity for every function in result.
    
    Uses native Rust fast-path batch execution when available, falling back
    to pure Python regex matching.
    """
    functions = result.get("functions", {})
    if not functions:
        return

    # Attempt Rust batch calculation first
    lines = [f.line for f in functions.values() if getattr(f, "line", None)]
    rust_results = _rust_batch_complexity(lines, lang=lang, file_path=file_path, content=content)

    for func_info in functions.values():
        line = getattr(func_info, "line", None)
        if rust_results and line in rust_results:
            cc, rank = rust_results[line]
        else:
            cc, rank = estimate_function_complexity(content, line or 1, lang=lang)

        func_info.complexity = {
            "cyclomatic_complexity": cc,
            "cc_rank": rank,
        }


def calculate_python_complexity(
    content: str,
    file_path: str,
    result: Dict[str, Any],
    verbose: bool = False,
) -> None:
    """Calculate cyclomatic complexity for Python source using radon."""
    try:
        from radon.complexity import cc_rank, cc_visit

        complexity_results = cc_visit(content)
        module_name = result["module"].name if "module" in result else ""

        for entry in complexity_results:
            name = getattr(entry, "name", "")
            classname = getattr(entry, "classname", None)

            if classname:
                full_name = f"{module_name}.{classname}.{name}"
            else:
                full_name = f"{module_name}.{name}"

            if "functions" in result and full_name in result["functions"]:
                result["functions"][full_name].complexity = {
                    "cyclomatic_complexity": entry.complexity,
                    "cc_rank": cc_rank(entry.complexity),
                }
            elif "classes" in result and full_name in result["classes"]:
                cls_info = result["classes"][full_name]
                cls_info.is_state_machine = cls_info.is_state_machine or (entry.complexity > 20)
    except Exception as e:
        if verbose:
            print(f"Error calculating complexity for {file_path}: {e}")


__all__ = [
    "CC_PATTERNS",
    "CC_LOW_THRESHOLD",
    "CC_MEDIUM_THRESHOLD",
    "CC_HIGH_THRESHOLD",
    "extract_function_body",
    "compute_cc_rank",
    "compute_cyclomatic_complexity",
    "estimate_function_complexity",
    "calculate_complexity_regex",
    "calculate_python_complexity",
    "_find_rust_binary",
    "_rust_batch_complexity",
]
