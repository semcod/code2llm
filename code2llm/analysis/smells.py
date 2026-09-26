"""Detection of code smells using analysis metrics.

This module provides the backward-compatible SmellDetector facade,
delegating to pure functions in smell_engine.
"""

from typing import Dict, List
from code2llm.core.models import AnalysisResult, CodeSmell
from .smell_engine import (
    detect_all_smells,
    detect_god_functions,
    detect_god_modules,
    detect_feature_envy,
    detect_data_clumps,
    detect_shotgun_surgery,
    detect_bottlenecks,
    detect_circular_dependencies,
    index_mutations_by_scope,
)


class SmellDetector:
    """Detect code smells from analysis results."""

    def __init__(self, result: AnalysisResult):
        """Initialise with the analysis result to detect code smells."""
        self.result = result
        # Pre-index mutations by scope — avoids O(n×m) full scans
        self._mutations_by_scope: Dict[str, list] = (
            index_mutations_by_scope(result.mutations)
        )

    def detect(self) -> List[CodeSmell]:
        """Record and return detected code smells."""
        return detect_all_smells(self.result, self._mutations_by_scope)

    def _detect_god_functions(self) -> List[CodeSmell]:
        """Detect high fan-out / large functions."""
        return detect_god_functions(
            self.result.functions,
            self.result.metrics,
            self._mutations_by_scope,
        )

    def _detect_god_modules(self) -> List[CodeSmell]:
        """Detect oversized modules/packages."""
        return detect_god_modules(self.result.modules)

    def _detect_feature_envy(self) -> List[CodeSmell]:
        """Detect functions that use other objects more than their own."""
        return detect_feature_envy(
            self.result.functions, self._mutations_by_scope
        )

    def _detect_data_clumps(self) -> List[CodeSmell]:
        """Detect 3+ variables frequently passed together within same file."""
        return detect_data_clumps(self.result.functions)

    def _detect_shotgun_surgery(self) -> List[CodeSmell]:
        """Detect variables whose mutation spans multiple functions."""
        return detect_shotgun_surgery(
            self.result.mutations, self.result.functions
        )

    def _detect_bottlenecks(self) -> List[CodeSmell]:
        """Detect functions with high Betweenness Centrality."""
        return detect_bottlenecks(self.result.functions)

    def _detect_circular_dependencies(self) -> List[CodeSmell]:
        """Detect circular dependencies in call graph."""
        cycles = (
            self.result.metrics.get("project", {})
            .get("circular_dependencies", [])
        )
        return detect_circular_dependencies(cycles, self.result.functions)


__all__ = [
    "SmellDetector",
    "detect_all_smells",
    "detect_god_functions",
    "detect_god_modules",
    "detect_feature_envy",
    "detect_data_clumps",
    "detect_shotgun_surgery",
    "detect_bottlenecks",
    "detect_circular_dependencies",
    "index_mutations_by_scope",
]
