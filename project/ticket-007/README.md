# ticket-007: Fix UTF-8 char boundary panic in `code2llm-rust` complexity scanner and resolve `PERF-AUDIT` findings

- **Status**: IN_PROGRESS
- **Workflow state**: VERIFIED

SESSION_EXECUTION_AUTHORIZATION: continue analysis, repairs, and standard alignment across projects using `wellmanifest/wellman`.

## Acceptance Criteria
- [x] AC-01: Guard `body[i..]` slices in `count_c_family_branches`, `count_go_branches`, and `count_rust_branches` (`packages/code2llm-rust/src/complexity.rs`) with `body.is_char_boundary(i)` and decode `prev_char` via `body[..i].chars().next_back()`.
- [x] AC-02: Add regression test `test_multibyte_utf8_and_emoji_do_not_panic` covering Rust, Go, and C-family functions containing multi-byte UTF-8 characters and emojis (`🚀`).
- [x] AC-03: Adopt Wellmanifest baseline + `code-dsl` + `llm` standards via `wellmanifest/wellman` and resolve all `PERF-AUDIT-*` findings (`0` findings).
