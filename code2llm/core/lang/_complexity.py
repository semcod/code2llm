"""Cyclomatic complexity estimation for regex-based language analyzers.

Backward compatibility facade delegating to the atomized code2llm.analysis.complexity engine.
"""

from __future__ import annotations

from code2llm.analysis.complexity import (
    CC_HIGH_THRESHOLD,
    CC_LOW_THRESHOLD,
    CC_MEDIUM_THRESHOLD,
    CC_PATTERNS,
    calculate_complexity_regex,
    compute_cc_rank,
    compute_cyclomatic_complexity,
    estimate_function_complexity,
    extract_function_body,
)

__all__ = [
    "CC_PATTERNS",
    "CC_LOW_THRESHOLD",
    "CC_MEDIUM_THRESHOLD",
    "CC_HIGH_THRESHOLD",
    "extract_function_body",
    "calculate_complexity_regex",
    "compute_cc_rank",
    "compute_cyclomatic_complexity",
    "estimate_function_complexity",
]
