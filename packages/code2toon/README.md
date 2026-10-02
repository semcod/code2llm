# code2toon

TOON (Topology Oriented Object Notation) specification, parser, validator, and diff engine for static code analysis.

## Features
- **Fast TOON parser**: Parses plain-text and YAML variants of TOON (`analysis.toon.yaml`, `map.toon.yaml`, `evolution.toon.yaml`).
- **Strict schema validation**: Ensures conformance to structural metrics, health markers, and module topology.
- **Architectural diff**: Compares two TOON outputs to detect architectural drift, new cycles, complexity regressions, and duplicate types.
- **Native Acceleration Ready**: Integrates with `code2llm-rust` for sub-millisecond header formatting and metric computation.

## Installation
```bash
pip install code2toon
```
