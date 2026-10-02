"""Graph query abstractions for code2graph."""

from typing import List, Optional, Set
from .models import AnalysisResult, FunctionInfo


class GraphQuery:
    """Convenience queries over an AnalysisResult."""

    def __init__(self, result: AnalysisResult):
        self.result = result

    def get_function(self, qname: str) -> Optional[FunctionInfo]:
        """Look up function by qualified name."""
        return self.result.functions.get(qname)

    def get_callees(self, qname: str) -> List[str]:
        """Return list of functions called by qname."""
        func = self.get_function(qname)
        return list(func.calls) if func else []

    def get_callers(self, qname: str) -> List[str]:
        """Return list of functions that call qname."""
        func = self.get_function(qname)
        return list(func.called_by) if func else []

    def get_entry_points(self) -> List[str]:
        """Return functions with zero callers."""
        if self.result.entry_points:
            return list(self.result.entry_points)
        return [
            name for name, f in self.result.functions.items()
            if not f.called_by
        ]

    def find_reachable(self, start_nodes: List[str]) -> Set[str]:
        """Find all functions transitively reachable from start_nodes via BFS."""
        visited: Set[str] = set()
        queue = list(start_nodes)
        for node in start_nodes:
            visited.add(node)

        while queue:
            curr = queue.pop(0)
            func = self.get_function(curr)
            if not func:
                continue
            for callee in func.calls:
                if callee not in visited and callee in self.result.functions:
                    visited.add(callee)
                    queue.append(callee)

        return visited
