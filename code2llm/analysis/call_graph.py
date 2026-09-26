"""Call graph extractor using AST.

Backward-compatibility facade delegating to code2llm.analysis.call_graph_engine.
"""

from __future__ import annotations

from code2llm.analysis.call_graph_engine import (
    CallGraphExtractor,
    calculate_call_metrics,
)

__all__ = [
    "CallGraphExtractor",
    "calculate_call_metrics",
]
