"""Data Analysis logic for code2llm - split into focused analyzers.

This module provides three analyzers:
  - DataFlowAnalyzer: data pipelines, state patterns, dependencies, event flows
  - OptimizationAdvisor: data types, optimization opportunities, process patterns
  - DataAnalyzer: facade combining both analyzers (backward compatibility)

Heavy implementation details live in _data_impl to keep this file's MI above
the regix hard-gate threshold.
"""

from typing import Any, Dict, Tuple
from code2llm.core.models import AnalysisResult
from code2llm.analysis._data_impl import (
    _find_data_pipelines,
    _find_state_patterns,
    _find_data_dependencies,
    _find_event_flows,
    _analyze_data_types,
    _build_data_flow_graph,
    _identify_process_patterns,
    _analyze_optimization_opportunities,
)


_INPUT_INDICATORS = [
    "parse",
    "load",
    "read",
    "fetch",
    "get",
    "input",
    "receive",
    "extract",
]
_TRANSFORM_INDICATORS = [
    "transform",
    "convert",
    "process",
    "validate",
    "filter",
    "map",
    "reduce",
    "compute",
]
_OUTPUT_INDICATORS = [
    "serialize",
    "format",
    "write",
    "save",
    "send",
    "output",
    "render",
    "encode",
]
_MAX_PIPELINES = 15


def _categorize_functions(result: "AnalysisResult") -> Tuple[list, list, list]:
    """Categorize functions into input/transform/output based on name patterns."""
    input_funcs, transform_funcs, output_funcs = [], [], []
    for func_name, func in result.functions.items():
        name_lower = func.name.lower()
        if any(ind in name_lower for ind in _INPUT_INDICATORS):
            input_funcs.append((func_name, func))
        elif any(ind in name_lower for ind in _TRANSFORM_INDICATORS):
            transform_funcs.append((func_name, func))
        elif any(ind in name_lower for ind in _OUTPUT_INDICATORS):
            output_funcs.append((func_name, func))
    return input_funcs, transform_funcs, output_funcs


def _make_stage(label: str, func_name: str, func) -> Dict[str, str]:
    """Build a single pipeline stage dict."""
    return {
        "stage": label,
        "function": func_name,
        "description": func.docstring[:100] if func.docstring else "N/A",
    }


class DataAnalyzer:
    """Analyze data flows, structures, and optimization opportunities."""

    def analyze_data_flow(self, result: AnalysisResult) -> Dict[str, Any]:
        """Perform detailed data flow analysis."""
        return {
            "data_pipelines": _find_data_pipelines(result, _categorize_functions, _make_stage, _MAX_PIPELINES),
            "state_patterns": _find_state_patterns(result),
            "data_dependencies": _find_data_dependencies(result),
            "event_flows": _find_event_flows(result),
        }

    def analyze_data_structures(self, result: AnalysisResult) -> Dict[str, Any]:
        """Analyze data structures and optimization opportunities."""
        data_types = _analyze_data_types(result)
        data_flow_graph = _build_data_flow_graph(result)
        process_patterns = _identify_process_patterns(result)
        optimization_analysis = _analyze_optimization_opportunities(
            result, data_types, data_flow_graph
        )
        return {
            "data_types": data_types,
            "data_flow_graph": data_flow_graph,
            "process_patterns": process_patterns,
            "optimization_analysis": optimization_analysis,
        }



# ---------------------------------------------------------------------------
# Focused analyzer classes
# ---------------------------------------------------------------------------


class DataFlowAnalyzer:
    """Analyze data flows: pipelines, state patterns, dependencies, and event flows."""

    def analyze(self, result: AnalysisResult) -> Dict[str, Any]:
        """Perform complete data flow analysis."""
        return {
            "data_pipelines": self.find_data_pipelines(result),
            "state_patterns": self.find_state_patterns(result),
            "data_dependencies": self.find_data_dependencies(result),
            "event_flows": self.find_event_flows(result),
        }

    def find_data_pipelines(self, result: AnalysisResult) -> list:
        """Find data transformation pipelines."""
        return _find_data_pipelines(result, _categorize_functions, _make_stage, _MAX_PIPELINES)

    def find_state_patterns(self, result: AnalysisResult) -> list:
        """Find state management patterns."""
        return _find_state_patterns(result)

    def find_data_dependencies(self, result: AnalysisResult) -> list:
        """Find cross-module data dependencies."""
        return _find_data_dependencies(result)

    def find_event_flows(self, result: AnalysisResult) -> list:
        """Find event-driven patterns."""
        return _find_event_flows(result)


class OptimizationAdvisor:
    """Analyze optimization opportunities: data types and process patterns."""

    def analyze(self, result: AnalysisResult) -> Dict[str, Any]:
        """Perform complete optimization analysis."""
        data_types = _analyze_data_types(result)
        data_flow_graph = _build_data_flow_graph(result)
        process_patterns = _identify_process_patterns(result)
        optimization_analysis = _analyze_optimization_opportunities(result, data_types, data_flow_graph)
        return {
            "data_types": data_types,
            "data_flow_graph": data_flow_graph,
            "process_patterns": process_patterns,
            "optimization_analysis": optimization_analysis,
        }

    def analyze_data_types(self, result: AnalysisResult) -> list:
        """Analyze data types and usage."""
        return _analyze_data_types(result)

    def build_data_flow_graph(self, result: AnalysisResult) -> dict:
        """Build data flow graph from function relationships."""
        return _build_data_flow_graph(result)

    def identify_process_patterns(self, result: AnalysisResult) -> list:
        """Identify common data processing patterns."""
        return _identify_process_patterns(result)

    def analyze_optimization_opportunities(
        self, result: AnalysisResult, data_types: list, dfg: dict
    ) -> dict:
        """Analyze optimization opportunities in data handling."""
        return _analyze_optimization_opportunities(result, data_types, dfg)
