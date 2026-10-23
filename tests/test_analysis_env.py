"""Guardrails for the pinned Python 3.12 analysis environment (PLF-036 / #26).

The analyzer chain clickmd/code2logic -> pfix -> pipreqs cannot run on the
Python 3.13 application venv: pipreqs 0.5.0 declares Requires-Python
>=3.8.1,<3.13 and no newer release exists. These tests keep the analysis
environment script and its documentation discoverable and pinned.
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "analysis-env.sh"
DOCS = ROOT / "docs" / "dependencies.md"


def test_analysis_env_script_exists_and_is_executable():
    assert SCRIPT.is_file()
    assert SCRIPT.stat().st_mode & 0o111, "analysis-env.sh must be executable"


def test_analysis_env_script_pins_python_312_and_locked_sync():
    content = SCRIPT.read_text(encoding="utf-8")
    assert 'ANALYSIS_PYTHON="${ANALYSIS_PYTHON:-3.12}"' in content
    assert "uv sync --locked" in content
    # The application venv must never be the target of the sync.
    assert "UV_PROJECT_ENVIRONMENT" in content
    assert "--all-extras" in content


@pytest.mark.parametrize(
    ("fragment",),
    [
        ("pipreqs",),
        (">=3.8.1,<3.13",),
        ("scripts/analysis-env.sh",),
        (".venv-analysis",),
    ],
)
def test_dependency_docs_explain_the_analysis_environment(fragment):
    assert fragment in DOCS.read_text(encoding="utf-8")


def test_gitignore_covers_analysis_environment():
    ignores = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert ".venv-analysis/" in ignores
