# code2flow

Mermaid flow diagrams, call graph visualizations, and architectural diagrams for static code analysis.

## Features
- **Mermaid Exporters**: Generate compact architectural diagrams, full function-level flowcharts, and filtered call graphs (`flow.mmd`, `compact_flow.mmd`, `calls.mmd`).
- **Syntax Validation & Auto-fix**: Robust syntax validation for Mermaid diagrams with automated sanitization of labels, node names, and subgraph delimiters.
- **Pure Topology Input**: Accepts `AnalysisResult` from `code2graph` without coupling to file system crawlers or AST parsers.

## Installation
```bash
pip install code2flow
```
