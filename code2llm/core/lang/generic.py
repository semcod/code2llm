"""Generic analyzer for unsupported languages."""

import re
from typing import Dict

from code2llm.core.models import ClassInfo, FunctionInfo, ModuleInfo
from code2llm.core.source_classifier import is_structural_only_file


_GENERIC_FUNC_PATTERNS = [
    re.compile(r"^\s*(?:def|function|func|fn|sub)\s+(\w+)"),
    re.compile(r"^\s*(\w+)\s*\([^)]*\)\s*\{?\s*$"),
]
_GENERIC_CLASS_PATTERNS = [
    re.compile(r"^\s*(?:class|struct|type)\s+(\w+)"),
]
_GENERIC_KEYWORDS = frozenset(("if", "for", "while", "switch", "catch", "return"))


def _scan_generic_line(
    line: str, line_no: int, module_name: str, file_path: str, result: dict, stats: dict
) -> None:
    """Match a single line against class/function patterns and update result."""
    for pattern in _GENERIC_CLASS_PATTERNS:
        m = pattern.match(line)
        if m:
            cname = m.group(1)
            qn = f"{module_name}.{cname}"
            result["classes"][qn] = ClassInfo(
                name=cname, qualified_name=qn, file=file_path, line=line_no,
                module=module_name, bases=[], methods=[], docstring="",
            )
            result["module"].classes.append(qn)
            stats["classes_found"] += 1
            return
    for pattern in _GENERIC_FUNC_PATTERNS:
        m = pattern.match(line)
        if m:
            fname = m.group(1)
            if fname not in _GENERIC_KEYWORDS:
                qn = f"{module_name}.{fname}"
                result["functions"][qn] = FunctionInfo(
                    name=fname, qualified_name=qn, file=file_path, line=line_no,
                    column=0, module=module_name, class_name=None, is_method=False,
                    is_private=fname.startswith("_"), is_property=False,
                    docstring="", args=[], decorators=[],
                )
                result["module"].functions.append(qn)
                stats["functions_found"] += 1
            break


def analyze_generic(
    content: str, file_path: str, module_name: str, ext: str, stats: Dict
) -> Dict:
    """Basic structural analysis for unsupported languages."""
    result = {
        "module": ModuleInfo(name=module_name, file=file_path, is_package=False),
        "functions": {}, "classes": {}, "nodes": {}, "edges": [],
    }
    lines = content.split("\n")
    if is_structural_only_file(file_path):
        stats["files_processed"] += 1
        return result
    for line_no, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        _scan_generic_line(line, line_no, module_name, file_path, result, stats)
    stats["files_processed"] += 1
    return result
