from types import SimpleNamespace

from code2llm.cli_exports.orchestrator import _build_export_config


def _args(**overrides):
    values = {
        "mode": "hybrid",
        "strategy": None,
        "exclude": [],
        "gitignore": True,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


def test_export_cache_key_inputs_include_scan_profile():
    full = _build_export_config(_args(), ["map"])
    scoped = _build_export_config(
        _args(mode="static", strategy="quick", exclude=["plugins", "*.md"]),
        ["map"],
    )

    assert full["mode"] == "hybrid"
    assert scoped["mode"] == "static"
    assert scoped["strategy"] == "quick"
    assert scoped["exclude"] == ["*.md", "plugins"]
    assert full != scoped
