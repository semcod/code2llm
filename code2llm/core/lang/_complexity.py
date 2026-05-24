"""Cyclomatic complexity estimation for regex-based language analyzers."""

import re
from typing import Dict

from code2llm.core.config import (
    CC_LOW_THRESHOLD,
    CC_MEDIUM_THRESHOLD,
    CC_HIGH_THRESHOLD,
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


def calculate_complexity_regex(
    content: str, result: Dict, lang: str = "c_family"
) -> None:
    """Estimate cyclomatic complexity for every function using regex keyword counting."""
    pattern = CC_PATTERNS.get(lang, CC_PATTERNS["c_family"])
    for func_info in result["functions"].values():
        body = extract_function_body(content, func_info.line)
        if not body:
            cc = 1
        else:
            cc = 1 + len(pattern.findall(body))
        if cc <= CC_LOW_THRESHOLD:
            rank = "A"
        elif cc <= CC_MEDIUM_THRESHOLD:
            rank = "B"
        elif cc <= CC_HIGH_THRESHOLD:
            rank = "C"
        else:
            rank = "D"
        func_info.complexity = {
            "cyclomatic_complexity": cc,
            "cc_rank": rank,
        }
