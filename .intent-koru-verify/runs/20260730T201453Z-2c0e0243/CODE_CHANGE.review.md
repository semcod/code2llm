<!-- t2c.code-change-review/v1 -->
# todo2code proposed code changes

This document is a grounded **review brief**, not an auto-applied source patch.
Implement the listed paths in a normal branch, re-run the pipeline, then
`t2c evaluate-code-change`. Acceptance still requires human/CI approval before DONE.

Graph fingerprint: `72c6762224a398215bbb61a74bd37eb82d8222fa6c65c438129c97b88c3110c5`

## P1

### Implement Update code2llm/analysis.toon.yaml (`CPLAN-02bab40a11166f6a1f7f`)

- Plan hash: `02bab40a11166f6a1f7fc49649867434888b286084d7b4265c696e67d37ddd19`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1c088db1678e24d53856.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update code2llm/analysis.toon.yaml Source intent: Update code2llm/analysis.toon.yaml Paths: code2llm/analysis.toon.yaml.
- Changes:
  - `modify` `code2llm/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1c088db1678e24d53856 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/analysis.toon.yaml.
- Diagnostics: `DIAG-1c088db1678e24d53856`
- Evidence records: `INT-CHANGELOG-02a4472653d2bb6bebda`
- Rollback: Revert the proposed changes to code2llm/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update examples/docker-doql-example/DEPENDENCY_ANALYSIS.md (`CPLAN-147b7c3011a38f58916f`)

- Plan hash: `147b7c3011a38f58916f9df9ae8b105e0dce5eb110002f6fa1346aa56346f45b`
- Risk: **medium** — Derived from review_required diagnostic DIAG-6945a67ace805dfbe755.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update examples/docker-doql-example/DEPENDENCY_ANALYSIS.md Source intent: Update examples/docker-doql-example/DEPENDENCY_ANALYSIS.md Paths: examples/docker-doql-example/DEPENDENCY_ANALYSIS.md. Symbols: DEPENDENCY_ANALYSIS.
- Changes:
  - `modify` `examples/docker-doql-example/DEPENDENCY_ANALYSIS.md` symbols: `DEPENDENCY_ANALYSIS`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: DEPENDENCY_ANALYSIS.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-6945a67ace805dfbe755 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: examples/docker-doql-example/DEPENDENCY_ANALYSIS.md.
- Diagnostics: `DIAG-6945a67ace805dfbe755`
- Evidence records: `INT-CHANGELOG-3fa999fa24cbe156138a`
- Rollback: Revert the proposed changes to examples/docker-doql-example/DEPENDENCY_ANALYSIS.md and re-run todo2code diagnostics.

### Implement update project_single/prompt.txt (`CPLAN-1b2aed947ff4c51be2ba`)

- Plan hash: `1b2aed947ff4c51be2bae76ff9a61d12c5d73872e6effd4b6b7ec3b04858a16c`
- Risk: **medium** — Derived from review_required diagnostic DIAG-24c3d35517603f8d111c.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: update project_single/prompt.txt Source intent: update project_single/prompt.txt Paths: project_single/prompt.txt.
- Changes:
  - `modify` `project_single/prompt.txt`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-24c3d35517603f8d111c (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: project_single/prompt.txt.
- Diagnostics: `DIAG-24c3d35517603f8d111c`
- Evidence records: `INT-CHANGELOG-c71c7988654cc136eb5f`
- Rollback: Revert the proposed changes to project_single/prompt.txt and re-run todo2code diagnostics.

### Implement Update examples/docker-doql-example/java/Main.java (`CPLAN-1cd26dd9116746761a01`)

- Plan hash: `1cd26dd9116746761a01b5276dfe450a035517953ea49def27da8e1132ecae3d`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1d73c103fe4985fed596.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update examples/docker-doql-example/java/Main.java Source intent: Update examples/docker-doql-example/java/Main.java Paths: examples/docker-doql-example/java/Main.java.
- Changes:
  - `modify` `examples/docker-doql-example/java/Main.java`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1d73c103fe4985fed596 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: examples/docker-doql-example/java/Main.java.
- Diagnostics: `DIAG-1d73c103fe4985fed596`
- Evidence records: `INT-CHANGELOG-b399dbc7081e04cf446f`
- Rollback: Revert the proposed changes to examples/docker-doql-example/java/Main.java and re-run todo2code diagnostics.

### Implement Update project_calls_test/calls.yaml (`CPLAN-241d0a1b39da6de602be`)

- Plan hash: `241d0a1b39da6de602be327c0b5cc0b4d862b420e680757378e7e1fd8df9164f`
- Risk: **medium** — Derived from review_required diagnostic DIAG-2c3fcf5fdc23e8f38fb6.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update project_calls_test/calls.yaml Source intent: Update project_calls_test/calls.yaml Paths: project_calls_test/calls.yaml.
- Changes:
  - `modify` `project_calls_test/calls.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-2c3fcf5fdc23e8f38fb6 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: project_calls_test/calls.yaml.
- Diagnostics: `DIAG-2c3fcf5fdc23e8f38fb6`
- Evidence records: `INT-CHANGELOG-fb1ccf7d470949f81414`
- Rollback: Revert the proposed changes to project_calls_test/calls.yaml and re-run todo2code diagnostics.

### Implement update code2llm/cli_exports.py (`CPLAN-24e172da2c7c80772edc`)

- Plan hash: `24e172da2c7c80772edce08778871831a7239f3191b8a34a506551eeee3101d2`
- Risk: **medium** — Derived from review_required diagnostic DIAG-59acb3a1853c50d935d1.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: update code2llm/cli_exports.py Source intent: update code2llm/cli_exports.py Paths: code2llm/cli_exports.py.
- Changes:
  - `modify` `code2llm/cli_exports.py`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-59acb3a1853c50d935d1 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/cli_exports.py.
- Diagnostics: `DIAG-59acb3a1853c50d935d1`
- Evidence records: `INT-CHANGELOG-d5be18f5fce68e0658fe`
- Rollback: Revert the proposed changes to code2llm/cli_exports.py and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-27bf1cb6f0814d2e196a`)

- Plan hash: `27bf1cb6f0814d2e196a306e4bbf4400ec34c1d8764fa5c991fdde50a7980857`
- Risk: **medium** — Derived from review_required diagnostic DIAG-50d37b4812a612b4a6f7.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-50d37b4812a612b4a6f7 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-50d37b4812a612b4a6f7`
- Evidence records: `INT-CHANGELOG-2f580d20c715cdcfc084`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update project_calls_test/context.md (`CPLAN-2adebda4d264a60b9af3`)

- Plan hash: `2adebda4d264a60b9af335d38be26642361445d79f33918b101715f82c8dd086`
- Risk: **medium** — Derived from review_required diagnostic DIAG-74aad6bd7df24ae1e6da.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update project_calls_test/context.md Source intent: Update project_calls_test/context.md Paths: project_calls_test/context.md.
- Changes:
  - `modify` `project_calls_test/context.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-74aad6bd7df24ae1e6da (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: project_calls_test/context.md.
- Diagnostics: `DIAG-74aad6bd7df24ae1e6da`
- Evidence records: `INT-CHANGELOG-e5cacfae50307cecd114`
- Rollback: Revert the proposed changes to project_calls_test/context.md and re-run todo2code diagnostics.

### Implement Update code2llm/analysis.toon.yaml (`CPLAN-2dfc746bc601079fca0e`)

- Plan hash: `2dfc746bc601079fca0e99ec5c4944af99106da2af62845c86c9869168e2a9b0`
- Risk: **medium** — Derived from review_required diagnostic DIAG-66ae0056fe4630621ead.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update code2llm/analysis.toon.yaml Source intent: Update code2llm/analysis.toon.yaml Paths: code2llm/analysis.toon.yaml.
- Changes:
  - `modify` `code2llm/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-66ae0056fe4630621ead (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/analysis.toon.yaml.
- Diagnostics: `DIAG-66ae0056fe4630621ead`
- Evidence records: `INT-CHANGELOG-e4c8761615a06c7d2549`
- Rollback: Revert the proposed changes to code2llm/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update code2llm/analysis.toon.yaml (`CPLAN-2e5ea96c9ac91838634a`)

- Plan hash: `2e5ea96c9ac91838634a58dd44b1a7d3dd1587e8cbc369c10f8228d5bb680fe7`
- Risk: **medium** — Derived from review_required diagnostic DIAG-704ae190bda31c839751.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update code2llm/analysis.toon.yaml Source intent: Update code2llm/analysis.toon.yaml Paths: code2llm/analysis.toon.yaml.
- Changes:
  - `modify` `code2llm/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-704ae190bda31c839751 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/analysis.toon.yaml.
- Diagnostics: `DIAG-704ae190bda31c839751`
- Evidence records: `INT-CHANGELOG-cb4d398a73e1747374de`
- Rollback: Revert the proposed changes to code2llm/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update docs/METHODOLOGY.md (`CPLAN-2fac205751fa3f0dfbcd`)

- Plan hash: `2fac205751fa3f0dfbcda1e2f05ff25ab0d021aed36b8a8cd8c690898995bdf6`
- Risk: **medium** — Derived from review_required diagnostic DIAG-21ebc8c1a189efb69ea1.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update docs/METHODOLOGY.md Source intent: Update docs/METHODOLOGY.md Paths: docs/METHODOLOGY.md. Symbols: METHODOLOGY.
- Changes:
  - `modify` `docs/METHODOLOGY.md` symbols: `METHODOLOGY`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: METHODOLOGY.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-21ebc8c1a189efb69ea1 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: docs/METHODOLOGY.md.
- Diagnostics: `DIAG-21ebc8c1a189efb69ea1`
- Evidence records: `INT-CHANGELOG-bbd0c02ac96cbd71424d`
- Rollback: Revert the proposed changes to docs/METHODOLOGY.md and re-run todo2code diagnostics.

### Implement Update root/analysis.toon.yaml (`CPLAN-367f4c651569a7170fd0`)

- Plan hash: `367f4c651569a7170fd014b7954842d2f9f25a9496da554ca3328b00a8207324`
- Risk: **medium** — Derived from review_required diagnostic DIAG-470d05805c2615f5ecdc.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update root/analysis.toon.yaml Source intent: Update root/analysis.toon.yaml Paths: root/analysis.toon.yaml.
- Changes:
  - `modify` `root/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-470d05805c2615f5ecdc (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: root/analysis.toon.yaml.
- Diagnostics: `DIAG-470d05805c2615f5ecdc`
- Evidence records: `INT-CHANGELOG-10106289bbf72cc457bf`
- Rollback: Revert the proposed changes to root/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement update code2llm/cli_exports.py (`CPLAN-36e757b4aab1f87558cc`)

- Plan hash: `36e757b4aab1f87558cc0fa58c75e3e69aab2a201e4d3685de60902113c1c2fc`
- Risk: **medium** — Derived from review_required diagnostic DIAG-26269ee01a287dd524db.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: update code2llm/cli_exports.py Source intent: update code2llm/cli_exports.py Paths: code2llm/cli_exports.py.
- Changes:
  - `modify` `code2llm/cli_exports.py`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-26269ee01a287dd524db (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/cli_exports.py.
- Diagnostics: `DIAG-26269ee01a287dd524db`
- Evidence records: `INT-CHANGELOG-e747c6b7755bc8f84b75`
- Rollback: Revert the proposed changes to code2llm/cli_exports.py and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-43fd807d02bb4588cc66`)

- Plan hash: `43fd807d02bb4588cc667094b187bcdb641aa463bcf27a5695f268cc6852c364`
- Risk: **medium** — Derived from review_required diagnostic DIAG-4f50b2751987c5e35088.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-4f50b2751987c5e35088 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-4f50b2751987c5e35088`
- Evidence records: `INT-CHANGELOG-e47c51351a8ed6378740`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update test_calls_output/index.html (`CPLAN-4d7797612333a3e9d0a8`)

- Plan hash: `4d7797612333a3e9d0a8a9d771f74d04fd908d7d3bb9b438869675dc2bbb24ca`
- Risk: **medium** — Derived from review_required diagnostic DIAG-15aaea5f2a693d86c8e3.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_calls_output/index.html Source intent: Update test_calls_output/index.html Paths: test_calls_output/index.html.
- Changes:
  - `modify` `test_calls_output/index.html`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-15aaea5f2a693d86c8e3 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_calls_output/index.html.
- Diagnostics: `DIAG-15aaea5f2a693d86c8e3`
- Evidence records: `INT-CHANGELOG-cab81944baf3a0a3277a`
- Rollback: Revert the proposed changes to test_calls_output/index.html and re-run todo2code diagnostics.

### Implement Update project/map.yaml (`CPLAN-4e1778f5b6582409c3a5`)

- Plan hash: `4e1778f5b6582409c3a5bdb6bc93844ae6fe8e9ba0f50ccad810377d8c743904`
- Risk: **medium** — Derived from review_required diagnostic DIAG-61859e0ffb7638be21f9.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update project/map.yaml Source intent: Update project/map.yaml Paths: project/map.yaml.
- Changes:
  - `modify` `project/map.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-61859e0ffb7638be21f9 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: project/map.yaml.
- Diagnostics: `DIAG-61859e0ffb7638be21f9`
- Evidence records: `INT-CHANGELOG-ebbde3ba2f62c214c7a6`
- Rollback: Revert the proposed changes to project/map.yaml and re-run todo2code diagnostics.

### Implement update tests/test_sprint5.py (`CPLAN-4f916ed3e13c23fe27ff`)

- Plan hash: `4f916ed3e13c23fe27ff6f6e22e86622b8830f97bf684a81488bbfefa3fec841`
- Risk: **medium** — Derived from review_required diagnostic DIAG-0955369f06d6ec65fbf7.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: update tests/test_sprint5.py Source intent: update tests/test_sprint5.py Paths: tests/test_sprint5.py.
- Changes:
  - `modify` `tests/test_sprint5.py`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-0955369f06d6ec65fbf7 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: tests/test_sprint5.py.
- Diagnostics: `DIAG-0955369f06d6ec65fbf7`
- Evidence records: `INT-CHANGELOG-a699dbfb4a42a0600f42`
- Rollback: Revert the proposed changes to tests/test_sprint5.py and re-run todo2code diagnostics.

### Implement Update .pyqual/ruff.json (`CPLAN-539c5b155d59200663b7`)

- Plan hash: `539c5b155d59200663b7ce9f1fd6d39ea6f010f4bafd550a5556224b4e25501c`
- Risk: **medium** — Derived from review_required diagnostic DIAG-79b598bc50307527bfac.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update .pyqual/ruff.json Source intent: Update .pyqual/ruff.json Paths: .pyqual/ruff.json.
- Changes:
  - `modify` `.pyqual/ruff.json`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-79b598bc50307527bfac (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: .pyqual/ruff.json.
- Diagnostics: `DIAG-79b598bc50307527bfac`
- Evidence records: `INT-CHANGELOG-a7edc536aa5a493e5894`
- Rollback: Revert the proposed changes to .pyqual/ruff.json and re-run todo2code diagnostics.

### Implement Update code2llm_part2/analysis.toon.yaml (`CPLAN-5911ee2c2904f7bf7ca8`)

- Plan hash: `5911ee2c2904f7bf7ca8522c52cca0612f1da0381ce79081eb61e243ff2d720f`
- Risk: **medium** — Derived from review_required diagnostic DIAG-27dac45fb32893b84329.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update code2llm_part2/analysis.toon.yaml Source intent: Update code2llm_part2/analysis.toon.yaml Paths: code2llm_part2/analysis.toon.yaml.
- Changes:
  - `modify` `code2llm_part2/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-27dac45fb32893b84329 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm_part2/analysis.toon.yaml.
- Diagnostics: `DIAG-27dac45fb32893b84329`
- Evidence records: `INT-CHANGELOG-691d0d785e34b4722b4e`
- Rollback: Revert the proposed changes to code2llm_part2/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-59a6bfd3a4f4757e53f5`)

- Plan hash: `59a6bfd3a4f4757e53f549731aa744e2c8b032fa8a93054467e2f1115f9159cf`
- Risk: **medium** — Derived from review_required diagnostic DIAG-73b7eb58b6a77c127a9f.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-73b7eb58b6a77c127a9f (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-73b7eb58b6a77c127a9f`
- Evidence records: `INT-CHANGELOG-9dc6885e429cf49619b0`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update code2llm/analysis.toon.yaml (`CPLAN-5df2500286d28f656f99`)

- Plan hash: `5df2500286d28f656f995d1f8c6dc7f250e7169c2eccf28be91aab2c216dbf1e`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1603d6b051b0de06c6dc.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update code2llm/analysis.toon.yaml Source intent: Update code2llm/analysis.toon.yaml Paths: code2llm/analysis.toon.yaml.
- Changes:
  - `modify` `code2llm/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1603d6b051b0de06c6dc (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/analysis.toon.yaml.
- Diagnostics: `DIAG-1603d6b051b0de06c6dc`
- Evidence records: `INT-CHANGELOG-72ed1f75168d77ced76f`
- Rollback: Revert the proposed changes to code2llm/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement **Renamed `llm_prompt.md` → `context.md`** — LLM narrative context (`CPLAN-60d0a645171fd72b3d97`)

- Plan hash: `60d0a645171fd72b3d97d1960ba31baba86881535925677190e73c9bfe7fc407`
- Risk: **medium** — Derived from review_required diagnostic DIAG-01e17d1cd1eafcd40fb7.; Touches 2 declared paths.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: **Renamed `llm_prompt.md` → `context.md`** — LLM narrative context Source intent: **Renamed `llm_prompt.md` → `context.md`** — LLM narrative context Paths: context.md, llm_prompt.md. Symbols: context.md, LLM, llm_prompt.md.
- Changes:
  - `modify` `context.md` symbols: `LLM`, `context.md`, `llm_prompt.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
  - `modify` `llm_prompt.md` symbols: `LLM`, `context.md`, `llm_prompt.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: LLM, context.md, llm_prompt.md.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-01e17d1cd1eafcd40fb7 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: context.md, llm_prompt.md.
- Diagnostics: `DIAG-01e17d1cd1eafcd40fb7`
- Evidence records: `INT-CHANGELOG-6bc960ae574072f22679`
- Rollback: Revert the proposed changes to context.md, llm_prompt.md and re-run todo2code diagnostics.

### Implement Update test_prompt/context.md (`CPLAN-64b71c067d50cee9d6a0`)

- Plan hash: `64b71c067d50cee9d6a00b5db56282e9882d0e8a4d6eb2f11d407cf07ebfd5d9`
- Risk: **medium** — Derived from review_required diagnostic DIAG-5ee0d78e6afbc9f063c7.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_prompt/context.md Source intent: Update test_prompt/context.md Paths: test_prompt/context.md.
- Changes:
  - `modify` `test_prompt/context.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-5ee0d78e6afbc9f063c7 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_prompt/context.md.
- Diagnostics: `DIAG-5ee0d78e6afbc9f063c7`
- Evidence records: `INT-CHANGELOG-86bba057279a41b53f13`
- Rollback: Revert the proposed changes to test_prompt/context.md and re-run todo2code diagnostics.

### Implement Update code2llm/analysis.toon.yaml (`CPLAN-6e72285935fffa5ee7da`)

- Plan hash: `6e72285935fffa5ee7da00cb3a8f66f14e39e411dbe2e4337f855a1d6b3e38b7`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1eebee031167e8482697.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update code2llm/analysis.toon.yaml Source intent: Update code2llm/analysis.toon.yaml Paths: code2llm/analysis.toon.yaml.
- Changes:
  - `modify` `code2llm/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1eebee031167e8482697 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/analysis.toon.yaml.
- Diagnostics: `DIAG-1eebee031167e8482697`
- Evidence records: `INT-CHANGELOG-33bba2e3fd2373a0470c`
- Rollback: Revert the proposed changes to code2llm/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement update code2llm/cli_exports.py (`CPLAN-7c75bebdb8486e8471d2`)

- Plan hash: `7c75bebdb8486e8471d2dfc64685f18070d387dd3350e886b7bc5715422ee78a`
- Risk: **medium** — Derived from review_required diagnostic DIAG-3a8d69b2012062a156f0.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: update code2llm/cli_exports.py Source intent: update code2llm/cli_exports.py Paths: code2llm/cli_exports.py.
- Changes:
  - `modify` `code2llm/cli_exports.py`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-3a8d69b2012062a156f0 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: code2llm/cli_exports.py.
- Diagnostics: `DIAG-3a8d69b2012062a156f0`
- Evidence records: `INT-CHANGELOG-795469c71186a27ed9ee`
- Rollback: Revert the proposed changes to code2llm/cli_exports.py and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-81976016feb2a129032c`)

- Plan hash: `81976016feb2a129032cd43e945c0e280f35baeea8df8c681431553feec1609f`
- Risk: **medium** — Derived from review_required diagnostic DIAG-11eb1b72732d643ebb84.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-11eb1b72732d643ebb84 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-11eb1b72732d643ebb84`
- Evidence records: `INT-CHANGELOG-e33cce38371ec6bfe75b`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-86758ab4df4cc8845266`)

- Plan hash: `86758ab4df4cc8845266104b2ce3fca04edeee7a37f0d1679f8e9ef4d1dd9af2`
- Risk: **medium** — Derived from review_required diagnostic DIAG-73ddc461d1121821d8c7.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-73ddc461d1121821d8c7 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-73ddc461d1121821d8c7`
- Evidence records: `INT-CHANGELOG-4c1f8d49c2e24558a6a1`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update .pyqual/runtime_errors.json (`CPLAN-8d35510eccc34d3c91d4`)

- Plan hash: `8d35510eccc34d3c91d4e63d77504db10f49738ef24ad0dc414c9144ef51d9b7`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1802e1724d708d5834b0.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update .pyqual/runtime_errors.json Source intent: Update .pyqual/runtime_errors.json Paths: .pyqual/runtime_errors.json.
- Changes:
  - `modify` `.pyqual/runtime_errors.json`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1802e1724d708d5834b0 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: .pyqual/runtime_errors.json.
- Diagnostics: `DIAG-1802e1724d708d5834b0`
- Evidence records: `INT-CHANGELOG-16cbcd0dfaf32bb9abac`
- Rollback: Revert the proposed changes to .pyqual/runtime_errors.json and re-run todo2code diagnostics.

### Implement Update test_calls_output/index.html (`CPLAN-911922a9d63845a7b39c`)

- Plan hash: `911922a9d63845a7b39cc46f941278915678215f8c1a8f7ac1640ebbe0c644f2`
- Risk: **medium** — Derived from review_required diagnostic DIAG-4d0904be81d1eba21e1c.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_calls_output/index.html Source intent: Update test_calls_output/index.html Paths: test_calls_output/index.html.
- Changes:
  - `modify` `test_calls_output/index.html`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-4d0904be81d1eba21e1c (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_calls_output/index.html.
- Diagnostics: `DIAG-4d0904be81d1eba21e1c`
- Evidence records: `INT-CHANGELOG-76017debb47cfd070fc8`
- Rollback: Revert the proposed changes to test_calls_output/index.html and re-run todo2code diagnostics.

### Implement Update examples/docker-doql-example/docker-compose.yml (`CPLAN-98bd263c50ab992fad90`)

- Plan hash: `98bd263c50ab992fad90ecf72ee5fb4f9c6dc2ec008bb3ee4365bea13825321c`
- Risk: **medium** — Derived from review_required diagnostic DIAG-09317df7300bdfdd1ee8.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update examples/docker-doql-example/docker-compose.yml Source intent: Update examples/docker-doql-example/docker-compose.yml Paths: examples/docker-doql-example/docker-compose.yml.
- Changes:
  - `modify` `examples/docker-doql-example/docker-compose.yml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-09317df7300bdfdd1ee8 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: examples/docker-doql-example/docker-compose.yml.
- Diagnostics: `DIAG-09317df7300bdfdd1ee8`
- Evidence records: `INT-CHANGELOG-3c059ecebcf063d58fe6`
- Rollback: Revert the proposed changes to examples/docker-doql-example/docker-compose.yml and re-run todo2code diagnostics.

### Implement Update root/analysis.toon.yaml (`CPLAN-a05c26d9a5ef814291c9`)

- Plan hash: `a05c26d9a5ef814291c923108ab72fa231856a82b80cdb54e0a9fa493eb790ea`
- Risk: **medium** — Derived from review_required diagnostic DIAG-03013a2fe0e33fb76c6c.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update root/analysis.toon.yaml Source intent: Update root/analysis.toon.yaml Paths: root/analysis.toon.yaml.
- Changes:
  - `modify` `root/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-03013a2fe0e33fb76c6c (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: root/analysis.toon.yaml.
- Diagnostics: `DIAG-03013a2fe0e33fb76c6c`
- Evidence records: `INT-CHANGELOG-6de5d0968d839d109445`
- Rollback: Revert the proposed changes to root/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-ac839c8594193b18ec81`)

- Plan hash: `ac839c8594193b18ec81b996ac108ddd6f9937a27ba80fd2ba84cadb3eb47df2`
- Risk: **medium** — Derived from review_required diagnostic DIAG-6f8f5c71c6d94eed581e.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-6f8f5c71c6d94eed581e (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-6f8f5c71c6d94eed581e`
- Evidence records: `INT-CHANGELOG-6da064bbef9cdf2a04ef`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update examples/docker-doql-example/SUMMARY.md (`CPLAN-acce67fc8fa0b7337ee9`)

- Plan hash: `acce67fc8fa0b7337ee98d1e08ad88a3cd1e4ab68c8e631cfc6f4f98efb9bf23`
- Risk: **medium** — Derived from review_required diagnostic DIAG-735fd03f64b9038828a0.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update examples/docker-doql-example/SUMMARY.md Source intent: Update examples/docker-doql-example/SUMMARY.md Paths: examples/docker-doql-example/SUMMARY.md. Symbols: SUMMARY.
- Changes:
  - `modify` `examples/docker-doql-example/SUMMARY.md` symbols: `SUMMARY`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: SUMMARY.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-735fd03f64b9038828a0 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: examples/docker-doql-example/SUMMARY.md.
- Diagnostics: `DIAG-735fd03f64b9038828a0`
- Evidence records: `INT-CHANGELOG-3927f90e744f8d921746`
- Rollback: Revert the proposed changes to examples/docker-doql-example/SUMMARY.md and re-run todo2code diagnostics.

### Implement LLMPromptExporter now outputs `context.md` by default (`CPLAN-adb6d65784142d0e4614`)

- Plan hash: `adb6d65784142d0e4614264641344aba1206e78e05244a7984e6523aa3c01124`
- Risk: **medium** — Derived from review_required diagnostic DIAG-093be4d16219606a5648.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: LLMPromptExporter now outputs `context.md` by default Source intent: LLMPromptExporter now outputs `context.md` by default Paths: context.md. Symbols: context.md, LLMPromptExporter.
- Changes:
  - `modify` `context.md` symbols: `LLMPromptExporter`, `context.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: LLMPromptExporter, context.md.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-093be4d16219606a5648 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: context.md.
- Diagnostics: `DIAG-093be4d16219606a5648`
- Evidence records: `INT-CHANGELOG-5a7c0208748441b0ed4b`
- Rollback: Revert the proposed changes to context.md and re-run todo2code diagnostics.

### Implement Update examples/docker-doql-example/ANALYSIS.md (`CPLAN-aed170a97a5c69b2b405`)

- Plan hash: `aed170a97a5c69b2b405f4ceb83a9aa2876b6d8e5bea58cae447f73587e179f1`
- Risk: **medium** — Derived from review_required diagnostic DIAG-05abfe57fbe3ed1ae044.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update examples/docker-doql-example/ANALYSIS.md Source intent: Update examples/docker-doql-example/ANALYSIS.md Paths: examples/docker-doql-example/ANALYSIS.md. Symbols: ANALYSIS.
- Changes:
  - `modify` `examples/docker-doql-example/ANALYSIS.md` symbols: `ANALYSIS`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: ANALYSIS.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-05abfe57fbe3ed1ae044 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: examples/docker-doql-example/ANALYSIS.md.
- Diagnostics: `DIAG-05abfe57fbe3ed1ae044`
- Evidence records: `INT-CHANGELOG-d175f61f0c9679f92747`
- Rollback: Revert the proposed changes to examples/docker-doql-example/ANALYSIS.md and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-be240d0522c4c7cd07ee`)

- Plan hash: `be240d0522c4c7cd07eecfd385f841fecdd8bddd721cbf88cc15404d57b46a9b`
- Risk: **medium** — Derived from review_required diagnostic DIAG-3651ed4f64ad4c3b6668.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-3651ed4f64ad4c3b6668 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-3651ed4f64ad4c3b6668`
- Evidence records: `INT-CHANGELOG-496138fc0c85bf4d9580`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update calls_output/context.md (`CPLAN-c030f520851137943b82`)

- Plan hash: `c030f520851137943b8266b655e74a80961b5f956590b2807957fe00dbe2e633`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1cf30921590b6241e2fe.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update calls_output/context.md Source intent: Update calls_output/context.md Paths: calls_output/context.md.
- Changes:
  - `modify` `calls_output/context.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1cf30921590b6241e2fe (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: calls_output/context.md.
- Diagnostics: `DIAG-1cf30921590b6241e2fe`
- Evidence records: `INT-CHANGELOG-e4b58d3fbde3173aa0c6`
- Rollback: Revert the proposed changes to calls_output/context.md and re-run todo2code diagnostics.

### Implement Update project/evolution.yaml (`CPLAN-c07796fc01a68b12c032`)

- Plan hash: `c07796fc01a68b12c03244b00fdc8e218562a7dfa74292bfd9c55487e5f2f508`
- Risk: **medium** — Derived from review_required diagnostic DIAG-332d208995e40159500d.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update project/evolution.yaml Source intent: Update project/evolution.yaml Paths: project/evolution.yaml.
- Changes:
  - `modify` `project/evolution.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-332d208995e40159500d (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: project/evolution.yaml.
- Diagnostics: `DIAG-332d208995e40159500d`
- Evidence records: `INT-CHANGELOG-c72de6b86528d7060290`
- Rollback: Revert the proposed changes to project/evolution.yaml and re-run todo2code diagnostics.

### Implement Update project/map.yaml (`CPLAN-c7d090a3efd6e46a574c`)

- Plan hash: `c7d090a3efd6e46a574c9ca286b8c6dc1d2c22cd6db4cbcdce9a64a1e790bb96`
- Risk: **medium** — Derived from review_required diagnostic DIAG-2ea324c8744cc3d8a803.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update project/map.yaml Source intent: Update project/map.yaml Paths: project/map.yaml.
- Changes:
  - `modify` `project/map.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-2ea324c8744cc3d8a803 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: project/map.yaml.
- Diagnostics: `DIAG-2ea324c8744cc3d8a803`
- Evidence records: `INT-CHANGELOG-3a8ca95e8cd02fd485ed`
- Rollback: Revert the proposed changes to project/map.yaml and re-run todo2code diagnostics.

### Implement **22 new tests** (`tests/test_sprint3_pipelines.py`) (`CPLAN-cbea1f03e88f9af06fa2`)

- Plan hash: `cbea1f03e88f9af06fa26d3122dc6de8427f4d6fd4053707cef92a65e4a58c25`
- Risk: **medium** — Derived from review_required diagnostic DIAG-5cbfd489ad161da6795e.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: **22 new tests** (`tests/test_sprint3_pipelines.py`) Source intent: **22 new tests** (`tests/test_sprint3_pipelines.py`) Paths: tests/test_sprint3_pipelines.py.
- Changes:
  - `modify` `tests/test_sprint3_pipelines.py`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-5cbfd489ad161da6795e (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: tests/test_sprint3_pipelines.py.
- Diagnostics: `DIAG-5cbfd489ad161da6795e`
- Evidence records: `INT-CHANGELOG-9670145c13949225d763`
- Rollback: Revert the proposed changes to tests/test_sprint3_pipelines.py and re-run todo2code diagnostics.

### Implement Update docs/API.md (`CPLAN-d0613638e47fcad8309b`)

- Plan hash: `d0613638e47fcad8309b39997c4ecce97f2faa7f72d62f617d061247be18f3f7`
- Risk: **medium** — Derived from review_required diagnostic DIAG-64fd598030a9f03580f2.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update docs/API.md Source intent: Update docs/API.md Paths: docs/API.md. Symbols: API.
- Changes:
  - `modify` `docs/API.md` symbols: `API`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Provide AST evidence for symbols: API.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-64fd598030a9f03580f2 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: docs/API.md.
- Diagnostics: `DIAG-64fd598030a9f03580f2`
- Evidence records: `INT-CHANGELOG-70be5661b9310c5cf491`
- Rollback: Revert the proposed changes to docs/API.md and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-d49a76d68f36b65c0544`)

- Plan hash: `d49a76d68f36b65c05446b3ca4985a008b3cb475a708de504c3ce15139424712`
- Risk: **medium** — Derived from review_required diagnostic DIAG-1d063167af3c60a4740c.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1d063167af3c60a4740c (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-1d063167af3c60a4740c`
- Evidence records: `INT-CHANGELOG-c8d323aeda353fade9b9`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update test_calls_output/analysis.toon.yaml (`CPLAN-dcb81faa379bcf13d6ac`)

- Plan hash: `dcb81faa379bcf13d6ac55b2369c545724198d245755519e86870b8b927ff93f`
- Risk: **medium** — Derived from review_required diagnostic DIAG-0dcf9ce06d1b582f3796.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_calls_output/analysis.toon.yaml Source intent: Update test_calls_output/analysis.toon.yaml Paths: test_calls_output/analysis.toon.yaml.
- Changes:
  - `modify` `test_calls_output/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-0dcf9ce06d1b582f3796 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_calls_output/analysis.toon.yaml.
- Diagnostics: `DIAG-0dcf9ce06d1b582f3796`
- Evidence records: `INT-CHANGELOG-df2dc2530b1d38509d0e`
- Rollback: Revert the proposed changes to test_calls_output/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update test_calls_output/context.md (`CPLAN-e60c830d2c878c7ff694`)

- Plan hash: `e60c830d2c878c7ff694f19d597cb8c650bf97072ca2c6ae2389a2a790567315`
- Risk: **medium** — Derived from review_required diagnostic DIAG-22ab797f72eb89ac344d.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_calls_output/context.md Source intent: Update test_calls_output/context.md Paths: test_calls_output/context.md.
- Changes:
  - `modify` `test_calls_output/context.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-22ab797f72eb89ac344d (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_calls_output/context.md.
- Diagnostics: `DIAG-22ab797f72eb89ac344d`
- Evidence records: `INT-CHANGELOG-51f309c3b9910ab0e5b5`
- Rollback: Revert the proposed changes to test_calls_output/context.md and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-e83425789fb554a554af`)

- Plan hash: `e83425789fb554a554af3d278c2f0df7a9013ebd241d8f3d70039a63ed3a5608`
- Risk: **medium** — Derived from review_required diagnostic DIAG-42a34bd4b73452911415.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-42a34bd4b73452911415 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-42a34bd4b73452911415`
- Evidence records: `INT-CHANGELOG-140daa2e4fd43d8fa02e`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update batch_1/analysis.toon.yaml (`CPLAN-f214f255ec88016b1bf0`)

- Plan hash: `f214f255ec88016b1bf07c82485940e86b9e85e2e4cadbaabba13c19790824de`
- Risk: **medium** — Derived from review_required diagnostic DIAG-26d7a2d64dede39a24ef.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update batch_1/analysis.toon.yaml Source intent: Update batch_1/analysis.toon.yaml Paths: batch_1/analysis.toon.yaml.
- Changes:
  - `modify` `batch_1/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-26d7a2d64dede39a24ef (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: batch_1/analysis.toon.yaml.
- Diagnostics: `DIAG-26d7a2d64dede39a24ef`
- Evidence records: `INT-CHANGELOG-d3c7ce94cae642f6ed9b`
- Rollback: Revert the proposed changes to batch_1/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update test_calls_output/analysis.toon.yaml (`CPLAN-f9bba6c29597e0e9ae63`)

- Plan hash: `f9bba6c29597e0e9ae634cab584384a3012693fb07a795a78f6596805b203844`
- Risk: **medium** — Derived from review_required diagnostic DIAG-5a7f1ef871221f12bea5.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_calls_output/analysis.toon.yaml Source intent: Update test_calls_output/analysis.toon.yaml Paths: test_calls_output/analysis.toon.yaml.
- Changes:
  - `modify` `test_calls_output/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-5a7f1ef871221f12bea5 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_calls_output/analysis.toon.yaml.
- Diagnostics: `DIAG-5a7f1ef871221f12bea5`
- Evidence records: `INT-CHANGELOG-8730d3d78a6232f78359`
- Rollback: Revert the proposed changes to test_calls_output/analysis.toon.yaml and re-run todo2code diagnostics.

### Implement Update test_calls_output/context.md (`CPLAN-fda6ec81d9e23b916267`)

- Plan hash: `fda6ec81d9e23b916267975a3d5468068f987ac79b44d6a98fba95684a7ae70c`
- Risk: **medium** — Derived from review_required diagnostic DIAG-74111fff5cb1ed9240d8.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update test_calls_output/context.md Source intent: Update test_calls_output/context.md Paths: test_calls_output/context.md.
- Changes:
  - `modify` `test_calls_output/context.md`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-74111fff5cb1ed9240d8 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: test_calls_output/context.md.
- Diagnostics: `DIAG-74111fff5cb1ed9240d8`
- Evidence records: `INT-CHANGELOG-aaac5355e64e0cd4b667`
- Rollback: Revert the proposed changes to test_calls_output/context.md and re-run todo2code diagnostics.

### Implement Update root/analysis.toon.yaml (`CPLAN-fdab104a55f0bcbe3895`)

- Plan hash: `fdab104a55f0bcbe389511845fa20574e1705fa171ef674cbc4bf80950c52ac0`
- Risk: **medium** — Derived from review_required diagnostic DIAG-29bfa02aed4e72bf8182.; Touches 1 declared path.
- Confidence: 0.80
- Description: Wpis wydania nie ma powiązanego commita ani faktu AST: Update root/analysis.toon.yaml Source intent: Update root/analysis.toon.yaml Paths: root/analysis.toon.yaml.
- Changes:
  - `modify` `root/analysis.toon.yaml`
    - Zweryfikować wpis lub dodać jednoznaczne odwołanie do ticketu, commita, pliku albo symbolu.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-29bfa02aed4e72bf8182 (CHANGELOG_WITHOUT_IMPLEMENTATION).
  - [ ] Touch only the declared paths: root/analysis.toon.yaml.
- Diagnostics: `DIAG-29bfa02aed4e72bf8182`
- Evidence records: `INT-CHANGELOG-e8837dadf34a9581f7d0`
- Rollback: Revert the proposed changes to root/analysis.toon.yaml and re-run todo2code diagnostics.


## P2

### Implement Obecna struktura `generation/template_generator.py` (128 funkcji) wymaga do funkcjonalnego podziału: (`CPLAN-d5377bf67a26505a5bca`)

- Plan hash: `d5377bf67a26505a5bca0f8eab9fe863e7064b37aa666d0d08666a5abd0e48a1`
- Risk: **low** — Derived from warning diagnostic DIAG-1b1343efe9b756f73e45.; Touches 1 declared path.
- Confidence: 0.72
- Description: Nie znaleziono powiązanego rekordu Git ani faktu AST dla: Obecna struktura `generation/template_generator.py` (128 funkcji) wymaga refaktoryzacji do funkcjonalnego podziału: Source intent: Obecna struktura `generation/template_generator.py` (128 funkcji) wymaga refaktoryzacji do funkcjonalnego podziału: Paths: generation/template_generator.py.
- Changes:
  - `modify` `generation/template_generator.py`
    - Dodać identyfikator ticketu/symbolu albo dostarczyć implementację i ponownie uruchomić linker.
- Acceptance criteria:
  - [ ] Do not introduce new blocking diagnostics.
  - [ ] Re-run todo2code link+diagnose and clear diagnostic DIAG-1b1343efe9b756f73e45 (PLANNED_NOT_IMPLEMENTED).
  - [ ] Touch only the declared paths: generation/template_generator.py.
- Diagnostics: `DIAG-1b1343efe9b756f73e45`
- Evidence records: `INT-DOC-580526f0fe41dfc6fa7e`
- Rollback: Revert the proposed changes to generation/template_generator.py and re-run todo2code diagnostics.

## After implementation

1. Re-run `t2c pipeline` (or extract + link + diagnose) on the changed tree.
2. `t2c evaluate-code-change <plan.json> --before-graph … --after-graph … --out acceptance.json`.
3. Require `accepted=true` and human/CI review before marking work DONE.
