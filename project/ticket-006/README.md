# ticket-006: Atomize code smell and hotspot detector

- **Status**: IN_PROGRESS / PUBLICATION
- **Workflow state**: VERIFIED

SESSION_EXECUTION_AUTHORIZATION: on 2026-09-26 the user authorized sequential refactoring, atomization, and Rust acceleration for `code2llm` (key dependency of `koru`).

## Acceptance Criteria
- [x] AC-01: Extract smell detection algorithms into pure atom `code2llm/analysis/smell_engine.py` (God Function, God Module, Feature Envy, Data Clump, Shotgun Surgery, Structural Bottleneck, Circular Dependencies).
- [x] AC-02: Support decoupled functional invocation with pure dictionaries/models, independent of full `AnalysisResult`.
- [x] AC-03: Ensure 100% backward compatibility via `SmellDetector` facade in `code2llm/analysis/smells.py`.
- [x] AC-04: Add comprehensive contract unit tests in `tests/test_smell_engine.py` (7 passed).
- [x] AC-05: Zero regressions across existing smell test suite (`tests/test_smells_data_clumps.py`, `tests/test_smells_shotgun_surgery.py`, 15 passed total).
