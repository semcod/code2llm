# Internal dependency updates

This repository owns its dependency configuration and this guide. The shared checker is maintained in [semcod/goal](https://github.com/semcod/goal/blob/84f18540d14c24cc8ff5b7f202d2874344779ecc/docs/internal-dependencies.md). Documentation follows the repository ownership principle in [wellmanifest/docs](https://github.com/wellmanifest/docs/blob/f64de5806577769672ebc1730d2e144b4c7671ec/README.md).

## Python support and tools

Application Python support remains `>=3.10`. Goal is used as a development/release tool; source inspection found no Goal imports or executable invocation in the application Python code. Its old declarations (dev) moved to an `automation` dependency group requiring Python >=3.12. The normal dev/test installation remains usable on the application's minimum Python version.

```sh
uv sync --locked --extra dev
uv sync --locked --group automation --python 3.12
```

The second command selects an automation environment; use a separate UV_PROJECT_ENVIRONMENT when keeping application and tool environments side by side. `code2llm` itself is excluded from the registry catalog when it is the local editable package.

## Analysis environment (pfix / pipreqs)

The analyzer toolchain (`clickmd` / `code2logic` → `pfix` → `pipreqs`) enters the
locked dependency graph transitively. `pipreqs` 0.5.0 — the newest published
release — declares `Requires-Python >=3.8.1,<3.13`, so analyzer runs must not
use the application `.venv` on Python 3.13 (PLF-036 / issue #26). Until pipreqs
or pfix publishes a 3.13-compatible release, materialize the pinned analysis
environment instead:

```sh
scripts/analysis-env.sh          # create/sync .venv-analysis (Python 3.12, uv.lock)
scripts/analysis-env.sh --check  # + uv pip check + pipreqs smoke test
```

The application `.venv` is preserved untouched until the dependency-lock
review; `.venv-analysis` is disposable and rebuilds deterministically from
`uv.lock`. Run analyzer entry points with `.venv-analysis/bin/python`.


## Daily updates and verification

[Dependabot configuration](../.github/dependabot.yml) checks the explicit internal package allowlist daily, including weekends, and groups updates in one PR. It includes transitive dependencies and may widen a manifest constraint when needed. Local or Git sources require separate review.

[Freshness CI](../.github/workflows/internal-dependency-freshness.yml) compares uv.lock with the highest published stable three-part versions using Goal 2.2.0. It runs daily, manually and on dependency PRs, has read-only repository permissions and retains JSON evidence. Resolver failures and mismatched targets stay visible. A successful audit says nothing about an already installed development or production environment.

[Locked tests](../.github/workflows/test-locked.yml) run on Python 3.10 and 3.13 before merge. Update creation does not grant merge approval. The `>=` declarations alone do not refresh uv.lock; environments must be synchronized after a tested update is merged.

## Delivery record

This change updates the internal packages to the registry targets observed on 2026-09-05, preserves application Python support and adds the scheduled checks above. Test and publication results are recorded in this repository's PR and Actions checks. The ecosystem rollout history is maintained in [costs documentation](https://github.com/semcod/costs/tree/main/docs/dependencies).
