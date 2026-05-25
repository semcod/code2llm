"""Shared utilities for regex-based language analyzers.

Public API is preserved for backward compatibility; implementation lives in:
- _complexity.py  — CC patterns + extract_function_body + calculate_complexity_regex
- _calls.py       — call-graph extraction
- _c_parser.py    — C-family declaration parser helpers
"""

from typing import Dict

from code2llm.core.lang._calls import extract_calls_regex
from code2llm.core.lang._c_parser import _extract_declarations
from code2llm.core.lang._complexity import calculate_complexity_regex




def analyze_c_family(
    content: str,
    file_path: str,
    module_name: str,
    stats: Dict,
    patterns: Dict,
    lang_config: Dict,
    cc_lang: str = "c_family",
    ext: str = "",
) -> Dict:
    """Shared analyzer for C-family languages (Java, C#, C++, etc.).

    Uses tree-sitter when available (10× faster), falls back to regex.
    """
    result = None

    # Try tree-sitter first (much faster)
    if ext:
        try:
            from .ts_parser import parse_source
            from .ts_extractors import extract_declarations_ts

            tree = parse_source(content, ext)
            if tree:
                result = extract_declarations_ts(
                    tree, content.encode("utf-8"), ext, file_path, module_name
                )
        except ImportError:
            pass  # tree-sitter not installed

    # Fallback to regex
    if result is None:
        result = _extract_declarations(
            content,
            file_path,
            module_name,
            patterns,
            stats,
            lang_config,
        )

    calculate_complexity_regex(content, result, lang=cc_lang)
    extract_calls_regex(content, module_name, result)
    stats["files_processed"] += 1
    return result
