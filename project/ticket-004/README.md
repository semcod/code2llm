# ticket-004: Atomize cyclomatic complexity engine and introduce native fast-path

- **Status**: IN_PROGRESS / PUBLICATION
- **Workflow state**: VERIFIED

SESSION_EXECUTION_AUTHORIZATION: on 2026-09-26 the user authorized sequential refactoring, atomization, and Rust acceleration for `code2llm` (key dependency of `koru`).

## Acceptance Criteria
- [x] AC-01: Extract complexity calculation and function body boundary analysis from `_complexity.py` and `file_analyzer.py` into pure atom `code2llm/analysis/complexity.py`.
- [x] AC-02: Implement native zero-dependency Rust acceleration in `packages/code2llm-fast-core` for brace extraction and keyword branching CC computation (speedup: **215x**).
- [x] AC-03: Ensure 100% backward compatibility and exact agreement with Radon/regex CC ranks (A/B/C/D).
- [x] AC-04: Add comprehensive unit tests in `tests/test_complexity.py` (9 passed).
- [x] AC-05: Zero regressions across existing `code2llm` test suite (32 passed in `test_nonpython_cc_calls.py` and `test_analyzer.py`).
