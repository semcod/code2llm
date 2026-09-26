# ticket-005: Atomize call graph extraction engine and add native fast-path

- **Status**: IN_PROGRESS / PUBLICATION
- **Workflow state**: VERIFIED

SESSION_EXECUTION_AUTHORIZATION: on 2026-09-26 the user authorized sequential refactoring, atomization, and Rust acceleration for `code2llm` (key dependency of `koru`).

## Acceptance Criteria
- [x] AC-01: Extract call graph extraction, call resolution, and fan-in/fan-out metrics calculation into pure atom `code2llm/analysis/call_graph_engine.py`.
- [x] AC-02: Implement native zero-dependency Rust call extraction scanner in `packages/code2llm-fast-core` (`--calls` mode, 5.5x speedup).
- [x] AC-03: Ensure 100% backward compatibility via facades in `call_graph.py` and `code2llm/core/lang/_calls.py`.
- [x] AC-04: Add comprehensive contract unit tests in `tests/test_call_graph_engine.py` (4 passed).
- [x] AC-05: Zero regressions across existing `code2llm` test suite (`test_nonpython_cc_calls.py`, `test_calls_toon_export.py`, 26 passed).
