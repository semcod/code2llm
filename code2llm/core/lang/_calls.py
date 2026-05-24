"""Call-graph extraction for regex-based language analyzers."""

import re
from typing import Dict, List

from code2llm.core.lang._complexity import extract_function_body

CALL_PATTERN_C_FAMILY = re.compile(
    r"(?<!\bfunction\b\s)"
    r"(?<!\bclass\b\s)"
    r"\b([a-zA-Z_]\w*)\s*\("
    r"|"
    r"(?:this|self)\s*\.\s*(\w+)\s*\("
    r"|"
    r"\b(\w+)\s*\.\s*(\w+)\s*\("
)

_CALL_KEYWORDS = frozenset(
    {
        "if",
        "for",
        "while",
        "switch",
        "catch",
        "return",
        "throw",
        "new",
        "typeof",
        "instanceof",
        "import",
        "export",
        "require",
        "console",
        "super",
        "class",
        "function",
        "async",
        "await",
        "delete",
        "void",
        "case",
        "default",
    }
)


def _resolve_call(
    simple_call: str,
    func_qname: str,
    module_name: str,
    known_simple: Dict[str, List[str]],
    calls_seen: set,
    func_info,
) -> None:
    """Resolve a single call name and append to func_info.calls if novel."""
    if simple_call in known_simple:
        candidates = known_simple[simple_call]
        my_module = func_qname.rsplit(".", 1)[0]
        resolved = next(
            (c for c in candidates if c.rsplit(".", 1)[0] == my_module),
            candidates[0],
        )
        if resolved != func_qname and resolved not in calls_seen:
            func_info.calls.append(resolved)
            calls_seen.add(resolved)
    else:
        ext_name = f"{module_name}.{simple_call}"
        if ext_name not in calls_seen:
            func_info.calls.append(ext_name)
            calls_seen.add(ext_name)


def extract_calls_regex(content: str, module_name: str, result: Dict) -> None:
    """Extract function calls from function bodies using regex."""
    known_simple: Dict[str, List[str]] = {}
    for qname in result["functions"]:
        simple = qname.rsplit(".", 1)[-1]
        known_simple.setdefault(simple, []).append(qname)

    for func_qname, func_info in result["functions"].items():
        body = extract_function_body(content, func_info.line)
        if not body:
            continue
        calls_seen: set = set()
        for m in CALL_PATTERN_C_FAMILY.finditer(body):
            simple_call = m.group(1) or m.group(2) or m.group(4)
            if not simple_call or simple_call in _CALL_KEYWORDS:
                continue
            _resolve_call(
                simple_call,
                func_qname,
                module_name,
                known_simple,
                calls_seen,
                func_info,
            )
