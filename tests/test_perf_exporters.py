"""Tests for performance optimizations in exporters and code2logic dispatch."""

from pathlib import Path
from types import SimpleNamespace
from code2llm.core.models import AnalysisResult, ModuleInfo, FunctionInfo
from code2llm.exporters.toon.helpers import _fast_line_counts, _WALK_EXCLUDE
from code2llm.exporters.flow_constants import EXCLUDE_PATTERNS, is_excluded_path
from code2llm.exporters.map.utils import count_total_lines
from code2llm.exporters.toon._render_section_helpers import _calculate_purity
from code2llm.cli_exports.code2logic import _build_code2logic_cmd


def test_fast_line_counts_reuses_module_line_count():
    """Verify _fast_line_counts uses mi.line_count without reading non-existent file."""
    result = AnalysisResult()
    result.modules = {
        "fake.mod": ModuleInfo(
            name="fake.mod",
            file="/non/existent/path/fake.py",
            line_count=42,
        )
    }
    counts = _fast_line_counts(Path("/non/existent"), result)
    assert counts.get("/non/existent/path/fake.py") == 42


def test_map_count_total_lines_reuses_line_count():
    """Verify count_total_lines uses mi.line_count."""
    result = AnalysisResult()
    result.modules = {
        "mod1": ModuleInfo(name="mod1", file="/path/a.py", line_count=100),
        "mod2": ModuleInfo(name="mod2", file="/path/b.py", line_count=50),
    }
    total = count_total_lines(result, lambda p: False)
    assert total == 150


def test_calculate_purity_indexed():
    """Verify _calculate_purity works with indexed name_to_func."""
    result = AnalysisResult()
    f1 = FunctionInfo(name="func1", qualified_name="m.func1", file="a.py", line=1)
    f2 = FunctionInfo(name="func2", qualified_name="m.func2", file="a.py", line=10)
    setattr(f2, "has_side_effects", True)
    result.functions = {"m.func1": f1, "m.func2": f2}

    name_to_func = {fi.name: fi for fi in result.functions.values()}
    purity = _calculate_purity(["func1", "func2"], result, name_to_func=name_to_func)
    assert purity == 0.5


def test_build_code2logic_cmd_forwards_exclude():
    """Verify _build_code2logic_cmd forwards args.exclude."""
    args = SimpleNamespace(
        verbose=False,
        exclude=["vendor/**", "node_modules"],
    )
    cmd = _build_code2logic_cmd(args, Path("/src"), Path("/out"))
    assert "--exclude" in cmd
    idx = cmd.index("--exclude")
    assert cmd[idx + 1 : idx + 3] == ["vendor/**", "node_modules"]


def test_exclude_patterns_contain_subactor_worktrees():
    """Verify standard exclusions contain .subactor, .worktrees, etc."""
    assert ".subactor" in EXCLUDE_PATTERNS
    assert ".worktrees" in EXCLUDE_PATTERNS
    assert ".planfile" in EXCLUDE_PATTERNS
    assert ".benchmarks" in EXCLUDE_PATTERNS

    assert ".subactor" in _WALK_EXCLUDE
    assert ".worktrees" in _WALK_EXCLUDE

    assert is_excluded_path("/project/.subactor/cache/file.py")
    assert is_excluded_path("/project/.worktrees/ticket-123/main.py")
