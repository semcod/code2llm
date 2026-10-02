# code2graph

Pure domain data models and graph query abstractions for static code analysis, extracted from `code2llm`.

## Overview

`code2graph` defines standard, language-agnostic data structures to represent:
- **Control Flow & Data Flow**: `FlowNode`, `FlowEdge`, `DataFlow`, `Mutation`
- **Source Code Structure**: `ModuleInfo`, `ClassInfo`, `FunctionInfo`
- **Analysis & Health**: `AnalysisResult`, `Pattern`, `CodeSmell`
- **Graph Queries**: In-memory query API to inspect call chains, entry points, and reachability.

## Installation

```bash
pip install code2graph
```

## Usage

```python
from code2graph import AnalysisResult, FunctionInfo, FlowEdge

result = AnalysisResult(project_path=".")
func = FunctionInfo(
    name="main",
    qualified_name="app.main",
    file="app.py",
    line=1,
)
result.functions["app.main"] = func
```

## License

Apache-2.0
