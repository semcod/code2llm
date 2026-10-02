"""Native acceleration bridge for code2llm.

Provides transparent integration with `code2llm-rust` (native PyO3 extension)
with secondary fallback to CLI binary and graceful pure-Python fallback.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

# Try importing the native PyO3 extension
try:
    import code2llm_rust  # type: ignore

    _HAS_NATIVE_RUST = True
except ImportError:
    code2llm_rust = None  # type: ignore
    _HAS_NATIVE_RUST = False


def is_native_rust_available() -> bool:
    """Return True if native code2llm-rust C-extension is loaded."""
    return _HAS_NATIVE_RUST


def get_native_version() -> Optional[str]:
    """Return code2llm-rust version if available."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "__version__"):
        return str(code2llm_rust.__version__)
    return None


def native_extract_function_body(content: str, start_line: int) -> Optional[str]:
    """Extract function body using native Rust if available."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "extract_function_body"):
        try:
            return code2llm_rust.extract_function_body(content, start_line)
        except Exception as e:
            logger.debug("code2llm_rust.extract_function_body failed: %s", e)
    return None


def native_calculate_complexity(body: str, lang: str = "c_family") -> Optional[Tuple[int, str]]:
    """Compute complexity and rank using native Rust if available."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "calculate_complexity"):
        try:
            cc, rank = code2llm_rust.calculate_complexity(body, lang)
            return int(cc), str(rank)
        except Exception as e:
            logger.debug("code2llm_rust.calculate_complexity failed: %s", e)
    return None


def native_batch_complexity(
    content: str, lines: List[int], lang: str = "c_family"
) -> Optional[Dict[int, Tuple[int, str]]]:
    """Compute complexity for multiple lines in parallel using native Rust."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "batch_complexity") and lines:
        try:
            raw = code2llm_rust.batch_complexity(content, lines, lang)
            return {line: (int(cc), str(rank)) for line, cc, rank in raw}
        except Exception as e:
            logger.debug("code2llm_rust.batch_complexity failed: %s", e)
    return None


def native_extract_calls(body: str) -> Optional[List[str]]:
    """Extract calls using native Rust if available."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "extract_calls"):
        try:
            return list(code2llm_rust.extract_calls(body))
        except Exception as e:
            logger.debug("code2llm_rust.extract_calls failed: %s", e)
    return None


def native_batch_calls(
    content: str, lines: List[int]
) -> Optional[Dict[int, List[str]]]:
    """Extract calls for multiple lines in parallel using native Rust."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "batch_calls") and lines:
        try:
            raw = code2llm_rust.batch_calls(content, lines)
            return {line: calls for line, calls in raw}
        except Exception as e:
            logger.debug("code2llm_rust.batch_calls failed: %s", e)
    return None


def native_betweenness_centrality(
    nodes: List[str],
    edges: List[Tuple[str, str]],
    k: Optional[int] = None,
    normalized: bool = True,
) -> Optional[Dict[str, float]]:
    """Compute betweenness centrality natively via Brandes' algorithm."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "betweenness_centrality"):
        try:
            return code2llm_rust.betweenness_centrality(nodes, edges, k, normalized)
        except Exception as e:
            logger.debug("code2llm_rust.betweenness_centrality failed: %s", e)
    return None


def native_detect_god_functions(
    functions: List[Tuple[str, str, int, int, int, int]],
) -> Optional[List[Tuple[str, str, int, int, int, int, float]]]:
    """Detect god functions natively."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "detect_god_functions"):
        try:
            return code2llm_rust.detect_god_functions(functions)
        except Exception as e:
            logger.debug("code2llm_rust.detect_god_functions failed: %s", e)
    return None


def native_detect_data_clumps(
    func_params: List[Tuple[str, List[str]]],
    min_size: int = 3,
    min_occurrences: int = 2,
) -> Optional[List[Tuple[List[str], List[str]]]]:
    """Detect data clumps natively."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "detect_data_clumps"):
        try:
            return code2llm_rust.detect_data_clumps(func_params, min_size, min_occurrences)
        except Exception as e:
            logger.debug("code2llm_rust.detect_data_clumps failed: %s", e)
    return None


def native_detect_circular_dependencies(
    nodes: List[str],
    edges: List[Tuple[str, str]],
) -> Optional[List[List[str]]]:
    """Detect circular dependency cycles natively using Tarjan SCC."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "detect_circular_dependencies"):
        try:
            return code2llm_rust.detect_circular_dependencies(nodes, edges)
        except Exception as e:
            logger.debug("code2llm_rust.detect_circular_dependencies failed: %s", e)
    return None


def native_compute_reachability(
    nodes: List[str],
    edges: List[Tuple[str, str]],
    entry_points: List[str],
) -> Optional[Dict[str, str]]:
    """Compute reachability (reachable / unreachable) from entry points."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "compute_reachability"):
        try:
            return code2llm_rust.compute_reachability(nodes, edges, entry_points)
        except Exception as e:
            logger.debug("code2llm_rust.compute_reachability failed: %s", e)
    return None


def native_compute_module_coupling(
    func_modules: List[Tuple[str, str]],
    calls: List[Tuple[str, str]],
) -> Optional[Tuple[Dict[str, List[str]], Dict[str, Tuple[int, int, float]]]]:
    """Compute module interactions and coupling metrics natively."""
    if _HAS_NATIVE_RUST and hasattr(code2llm_rust, "compute_module_coupling"):
        try:
            return code2llm_rust.compute_module_coupling(func_modules, calls)
        except Exception as e:
            logger.debug("code2llm_rust.compute_module_coupling failed: %s", e)
    return None
