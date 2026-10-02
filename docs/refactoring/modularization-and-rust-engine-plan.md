---
id: modularization-and-rust-engine-plan
title: Code2llm Ecosystem Modularization and Complete Rust Engine Migration Plan
kind: refactoring
version: 1.0.0
date: 2026-10-02
author: Antigravity Agent
status: proposed
---

# Code2llm Ecosystem Modularization and Complete Rust Engine Migration Plan

## 1. Problem Statement

`code2llm` has evolved into a monolithic repository combining fundamentally distinct domains:
1. **Multi-language AST parsing and static analysis** (Python, JS, TS, Rust, Go, C++, etc.).
2. **Graph theory algorithms and topological analysis** (CFG, DFG, Call Graph, Centrality, SCC).
3. **Software quality auditing and anti-pattern/smell detection** (God Functions, Data Clumps, Shotgun Surgery).
4. **Diagrammatic modeling and rendering** (Mermaid AST generation, PNG export, HTML dashboards).
5. **TOON format specification and view serialization** (`analysis.toon.yaml`, `map.toon.yaml`, `evolution.toon.yaml`).
6. **LLM context compression and prompt engineering** (`context.md`, chunking, token budgeting).
7. **CLI orchestration and file caching** (CLI parsing, watch mode, chunking orchestrator).

This coupling creates:
- Heavy memory and CPU footprints.
- Slow CI and test runs across unrelated domains.
- Complex dependency trees (e.g. `matplotlib`, `networkx`, `vulture`, `tree-sitter` all bundled together).
- Difficulties in maintaining clean API boundaries and isolating fast-paths.

---

## 2. Full Rust Migration: Replacing Remaining Bottlenecks in `code2llm-rust`

To achieve sub-second analysis even on large repositories (>5,000 files, >50,000 functions), the entire compute-intensive data pipeline will be migrated into `code2llm-rust`:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        code2llm-rust Engine                            │
│                                                                        │
│  ┌─────────────────────────┐         ┌──────────────────────────────┐  │
│  │   Fast File Discovery   │         │    Native Tree-sitter AST    │  │
│  │ (ignore/walkdir crates) │ ──────> │  (15+ languages in parallel) │  │
│  └─────────────────────────┘         └──────────────────────────────┘  │
│                                                      │                 │
│                                                      ▼                 │
│  ┌─────────────────────────┐         ┌──────────────────────────────┐  │
│  │    Linear-Time Graphs   │         │    Symbol Resolution &       │  │
│  │   • Brandes Centrality  │ <────── │       Call Graph Engine      │  │
│  │   • Tarjan SCC (Cycles) │         │     (string interning)       │  │
│  │   • Graph Reachability  │         └──────────────────────────────┘  │
│  └─────────────────────────┘                                           │
│               │                                                        │
│               ▼                                                        │
│  ┌─────────────────────────┐         ┌──────────────────────────────┐  │
│  │ Vectorized Smell Engine │         │     Direct TOON Serializer   │  │
│  │  (God Func, Clumps, Fo) │ ──────> │   (Instant zero-copy YAML)   │  │
│  └─────────────────────────┘         └──────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

### Detailed Bottleneck Replacements in Rust

| Bottleneck | Current Python Implementation | Target Rust Implementation in `code2llm-rust` | Target Speedup |
|---|---|---|---|
| **File Discovery & Gitignore** | `os.walk` + `fnmatch` / regex in Python | `ignore` and `walkdir` crates with parallel traversal | **15x – 40x** |
| **AST Parsing (Multi-lang)** | Python `ast.parse` + Python `tree_sitter` bindings | Native Rust Tree-sitter parsers directly linked into `code2llm-rust` | **20x – 50x** |
| **Call Graph Resolution** | Nested Python dict lookups and `rsplit(".", 1)` | String interning (`lasso` or `ustr`) + concurrent HashMap lookup | **30x – 60x** |
| **Betweenness Centrality** | `networkx.betweenness_centrality` (sampled or full) | Native Brandes' algorithm with Rayon BFS (*implemented in v0.1.0*) | **42x – 200x** |
| **Circular Dependencies** | `nx.simple_cycles` (Johnson's alg, skips >1000 nodes) | Tarjan's Strongly Connected Components (SCC) in $O(V + E)$ | **100x+** (no node cap) |
| **Dead Code / Reachability** | `vulture` Python scanner (re-reads all files from disk) | Graph reachability BFS/DFS on in-memory call graph | **80x – 150x** |
| **Coupling Metrics** | Python `CouplingAnalyzer` iterating modules | Vectorized calculation of $Ca, Ce, I = Ce/(Ca+Ce)$ in Rust | **50x** |
| **TOON YAML Export** | PyYAML `yaml.dump` / string concatenation | Native TOON formatter emitting pre-sized buffers | **20x – 35x** |

---

## 3. Proposed Project Decomposition: Separate Modular Packages

Instead of maintaining a single monolithic codebase, we recommend decomposing `code2llm` into 5 focused repositories/packages within the `semcod` organization:

### Package 1: `code2llm-rust` (Native Core Engine)
- **Role**: High-performance compute engine.
- **Tech Stack**: Rust, PyO3, Rayon, Tree-sitter.
- **Responsibilities**:
  - File tree walking with `.gitignore` compliance.
  - Multi-language AST parsing (Python, TS/JS, Rust, Go, C/C++, Java, PHP).
  - Cyclomatic complexity, Halstead metrics, fan-in/fan-out.
  - Call graph construction and Brandes' betweenness centrality.
  - Linear-time Tarjan cycle detection and dead-code reachability.
  - Code smell detector (God functions, God modules, Data clumps).
  - Emits native structs / PyO3 bindings and raw JSON/TOON primitives.

### Package 2: `code2graph` (Pure Graph & Code Representation Model)
- **Role**: Data models and semantic code graph domain abstractions.
- **Tech Stack**: Python (type annotations, pydantic / dataclasses).
- **Responsibilities**:
  - Definition of `AnalysisResult`, `FunctionInfo`, `ModuleInfo`, `FlowEdge`, `CodeSmell`.
  - In-memory graph query API (e.g. find callers, find entrypoints, path analysis).
  - Python fallback algorithms when Rust engine is unavailable.

### Package 3: `code2toon` (TOON Format Specification & Tooling)
- **Role**: Dedicated serializer, validator, and diff engine for TOON format.
- **Tech Stack**: Python / Rust bindings.
- **Responsibilities**:
  - Specification of `analysis.toon.yaml`, `map.toon.yaml`, `evolution.toon.yaml`.
  - Fast TOON schema validation.
  - TOON diffing (detecting architectural drift and metric changes between Git commits).

### Package 4: `code2flow` (Diagrams & Visualizations)
- **Role**: Visual representation of control flow and call architecture.
- **Tech Stack**: Python, Mermaid.js integration, optional Chromium/Playwright for PNG.
- **Responsibilities**:
  - Compact and full Mermaid flow diagrams (`flow.mmd`, `compact_flow.mmd`, `calls.mmd`).
  - HTML interactive dashboard generation.
  - Isolated rendering dependencies (`matplotlib`, `playwright`, etc.) so CLI users who only want TOON/Markdown do not need graphic libraries.

### Package 5: `code2llm` (Orchestrator, CLI & LLM Context Generator)
- **Role**: Top-level user-facing CLI and LLM integration tool.
- **Tech Stack**: Python CLI (`argparse` / `click`).
- **Dependencies**:
  - Requires: `code2llm-rust`, `code2graph`, `code2toon`.
  - Optional extras: `code2llm[diagrams]` (pulls in `code2flow`), `code2llm[prompt]` (pulls in tokenizers).
- **Responsibilities**:
  - Command-line parsing (`code2llm ./ --toon-yaml -o project/`).
  - Context generation (`context.md`, `prompt.txt`) optimized for LLM token windows.
  - Persistent caching (`~/.code2llm/`) and incremental watch mode.
  - Orchestration of chunked analysis for large codebases.

---

## 4. Dependency Graph of the Target Architecture

```mermaid
graph TD
    CLI["code2llm (CLI & LLM Orchestrator)"]
    RUST["code2llm-rust (Native Engine)"]
    GRAPH["code2graph (Data Models & Topology)"]
    TOON["code2toon (TOON Format & Diff)"]
    FLOW["code2flow (Diagrams & Visuals - Optional)"]

    CLI --> RUST
    CLI --> GRAPH
    CLI --> TOON
    CLI -.->|optional [diagrams]| FLOW
    FLOW --> GRAPH
    TOON --> GRAPH
    RUST -.->|FFI PyO3| GRAPH
```

---

## 5. Migration Roadmap & Next Steps

1. **Phase 1 (Complete)**:
   - Atomization of complexity, call graph, and smells.
   - Initial `code2llm-rust` package with PyO3, Rayon, Brandes' centrality (42.3x speedup), CC, and calls.
   - `native_bridge.py` in `code2llm`.

2. **Phase 2 (Complete)**:
   - Implemented Tarjan's Strongly Connected Components in `code2llm-rust` eliminating NetworkX cycle detection freeze.
   - Implemented fast in-memory graph reachability and module coupling ($Ca, Ce, I$) in Rust.

3. **Phase 3 (Complete)**:
   - Integrated `ignore` crate into `code2llm-rust` for instant parallel gitignore-aware file collection (`native_walk_project_files`).
   - Implemented parallel cache validation (`PersistentCache`) with Rayon & SHA-256 in Rust.
   - Implemented native call graph resolution with $O(1)$ candidate lookups and module affinity matching.

4. **Phase 4 (In Progress - Ecosystem Modularization)**:
   - **`code2graph` (Complete)**: Extracted graph data models (`AnalysisResult`, `FunctionInfo`, `FlowNode`, `FlowEdge`, `GraphQuery`) into standalone package at `packages/code2graph` and published to `https://github.com/semcod/code2graph`.
   - **`code2toon` (Complete)**: Extracted TOON format specification, parser, validator, and diff engine into standalone package at `packages/code2toon`.
   - **`code2flow`**: Extract visual diagrams and heavy rendering dependencies into standalone package.
