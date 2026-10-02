"""code2graph: Domain data models and graph representation for code analysis."""

from .models import (
    BaseModel,
    FlowNode,
    FlowEdge,
    FunctionInfo,
    ClassInfo,
    ModuleInfo,
    Pattern,
    CodeSmell,
    Mutation,
    DataFlow,
    AnalysisResult,
)
from .query import GraphQuery

__version__ = "0.1.0"

__all__ = [
    "BaseModel",
    "FlowNode",
    "FlowEdge",
    "FunctionInfo",
    "ClassInfo",
    "ModuleInfo",
    "Pattern",
    "CodeSmell",
    "Mutation",
    "DataFlow",
    "AnalysisResult",
    "GraphQuery",
    "__version__",
]
