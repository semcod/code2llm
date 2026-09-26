"""Analysis package for code2llm."""

__all__ = [
    "CFGExtractor",
    "DFGExtractor",
    "CallGraphExtractor",
    "CouplingAnalyzer",
    "SmellDetector",
    "DataAnalyzer",
    "TypeInferenceEngine",
    "SideEffectDetector",
    "PipelineDetector",
    "PipelineResolver",
    "PipelineClassifier",
    "calculate_complexity_regex",
    "calculate_python_complexity",
    "compute_cyclomatic_complexity",
    "extract_function_body",
]


def __getattr__(name):
    """Lazy import analysis modules on first access."""
    _imports = {
        "CFGExtractor": ".cfg",
        "DFGExtractor": ".dfg",
        "CallGraphExtractor": ".call_graph",
        "CouplingAnalyzer": ".coupling",
        "SmellDetector": ".smells",
        "DataAnalyzer": ".data_analysis",
        "TypeInferenceEngine": ".type_inference",
        "SideEffectDetector": ".side_effects",
        "PipelineDetector": ".pipeline_detector",
        "PipelineResolver": ".pipeline_resolver",
        "PipelineClassifier": ".pipeline_classifier",
        "calculate_complexity_regex": ".complexity",
        "calculate_python_complexity": ".complexity",
        "compute_cyclomatic_complexity": ".complexity",
        "extract_function_body": ".complexity",
    }
    if name in _imports:
        import importlib

        module = importlib.import_module(_imports[name], __package__)
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
