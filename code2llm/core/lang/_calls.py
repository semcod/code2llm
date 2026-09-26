"""Call-graph extraction for regex-based language analyzers.

Backward compatibility facade delegating to the atomized code2llm.analysis.call_graph_engine.
"""

from __future__ import annotations

from code2llm.analysis.call_graph_engine import (
    CALL_PATTERN_C_FAMILY,
    _CALL_KEYWORDS,
    _resolve_call,
    extract_calls_regex,
)

__all__ = [
    "CALL_PATTERN_C_FAMILY",
    "_CALL_KEYWORDS",
    "_resolve_call",
    "extract_calls_regex",
]
