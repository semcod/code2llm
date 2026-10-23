#!/usr/bin/env bash
# Pinned analysis environment for the analyzer toolchain (pfix -> pipreqs).
#
# pipreqs 0.5.0 (the newest published release) declares
# Requires-Python >=3.8.1,<3.13, so the analyzer chain must not run on the
# application .venv (Python 3.13) until pipreqs or pfix publishes a
# 3.13-compatible release. This script materializes a separate, locked
# Python 3.12 environment (PLF-036 / issue #26).
#
# Usage:
#   scripts/analysis-env.sh            # create/sync .venv-analysis
#   scripts/analysis-env.sh --check    # sync + uv pip check + smoke test
#
# The application .venv is never touched. Remove .venv-analysis only with
# `uv python dir` knowledge; it is disposable and rebuilds deterministically
# from uv.lock.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ANALYSIS_PYTHON="${ANALYSIS_PYTHON:-3.12}"
ANALYSIS_ENV="${ANALYSIS_ENV:-$ROOT/.venv-analysis}"

cd "$ROOT"
UV_PROJECT_ENVIRONMENT="$ANALYSIS_ENV" uv sync --locked --python "$ANALYSIS_PYTHON" --all-extras

if [[ "${1:-}" == "--check" ]]; then
  UV_PROJECT_ENVIRONMENT="$ANALYSIS_ENV" uv pip check --python "$ANALYSIS_ENV/bin/python"
  # Analyzer smoke test: pipreqs resolves imports for a small sample project.
  "$ANALYSIS_ENV/bin/python" - <<'PY'
import tempfile
from pathlib import Path

from pipreqs import pipreqs

with tempfile.TemporaryDirectory() as tmp:
    sample = Path(tmp)
    (sample / "sample.py").write_text(
        "import json\nimport pathlib\nimport yaml\n\nprint(json, pathlib, yaml)\n",
        encoding="utf-8",
    )
    imports = pipreqs.get_all_imports(str(sample))
    # pipreqs filters stdlib/local imports: only third-party names remain.
    assert "yaml" in imports, f"third-party import not resolved: {imports}"
    assert "json" not in imports, f"stdlib import should be filtered: {imports}"
    print(f"analysis-env smoke OK (pipreqs resolved {len(imports)} imports)")
PY
fi
