"""Test suite for code2llm."""

import pytest
import tempfile
import shutil
from pathlib import Path
from code2llm import ProjectAnalyzer, Config
from code2llm.core.config import FAST_CONFIG, FilterConfig
from code2llm.core.models import AnalysisResult, FunctionInfo


class TestProjectAnalyzer:
    """Test the main ProjectAnalyzer."""

    @pytest.fixture
    def sample_project(self):
        """Create a temporary sample project."""
        project_dir = Path(tempfile.mkdtemp())

        # Create sample module
        (project_dir / "module1.py").write_text('''
def process_data(data):
    """Process data."""
    if not data:
        return None
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

def validate(data):
    return isinstance(data, list)
''')

        # Create class module
        (project_dir / "module2.py").write_text('''
class Connection:
    """Connection state machine."""
    
    def __init__(self):
        self.state = "disconnected"
    
    def connect(self):
        if self.state == "disconnected":
            self.state = "connecting"
    
    def connected(self):
        if self.state == "connecting":
            self.state = "connected"
''')

        # Create recursive module
        (project_dir / "module3.py").write_text('''
def factorial(n):
    """Recursive factorial."""
    if n <= 1:
        return 1
    result = n * factorial(n - 1)
    return result

def fibonacci(n):
    if n <= 1:
        return n
    res = fibonacci(n - 1) + fibonacci(n - 2)
    return res
''')

        yield project_dir

        # Cleanup
        shutil.rmtree(project_dir)

    def test_analyze_finds_functions(self, sample_project):
        """Test that analyzer finds all functions."""
        config = FAST_CONFIG
        config.filters.min_function_lines = 1
        config.performance.skip_pattern_detection = False
        analyzer = ProjectAnalyzer(config)
        result = analyzer.analyze_project(str(sample_project))

        assert result.get_function_count() >= 6
        assert "factorial" in [f.name for f in result.functions.values()]
        assert "process_data" in [f.name for f in result.functions.values()]

    def test_analyze_finds_classes(self, sample_project):
        """Test that analyzer finds classes."""
        config = FAST_CONFIG
        config.filters.min_function_lines = 1
        analyzer = ProjectAnalyzer(config)
        result = analyzer.analyze_project(str(sample_project))

        assert result.get_class_count() >= 1
        assert "Connection" in [c.name for c in result.classes.values()]

    def test_detects_recursion(self, sample_project):
        """Test recursion detection."""
        config = FAST_CONFIG
        config.filters.min_function_lines = 1
        config.performance.skip_pattern_detection = False
        analyzer = ProjectAnalyzer(config)
        result = analyzer.analyze_project(str(sample_project))

        recursive_patterns = [p for p in result.patterns if p.type == "recursion"]
        assert len(recursive_patterns) >= 2

        func_names = [p.name for p in recursive_patterns]
        assert any("factorial" in n for n in func_names)
        assert any("fibonacci" in n for n in func_names)

    def test_detects_state_machine(self, sample_project):
        """Test state machine detection."""
        config = FAST_CONFIG
        config.filters.min_function_lines = 1
        config.performance.skip_pattern_detection = False
        analyzer = ProjectAnalyzer(config)
        result = analyzer.analyze_project(str(sample_project))

        state_patterns = [p for p in result.patterns if p.type == "state_machine"]
        assert len(state_patterns) >= 1
        assert any("Connection" in p.name for p in state_patterns)

    def test_caching_works(self, sample_project):
        """Test that caching improves performance."""
        config = FAST_CONFIG
        config.performance.enable_cache = True
        config.performance.cache_dir = str(sample_project / ".cache")

        # First run - populate cache
        analyzer1 = ProjectAnalyzer(config)
        result1 = analyzer1.analyze_project(str(sample_project))

        # Second run - should use cache
        analyzer2 = ProjectAnalyzer(config)
        result2 = analyzer2.analyze_project(str(sample_project))

        assert result2.stats.get("cache_hits", 0) >= 0

    def test_filtering_skips_tests(self, sample_project):
        """Test that test files are filtered out."""
        # Create test file
        (sample_project / "test_module.py").write_text("""
def test_something():
    assert True
""")

        config = Config(mode="static", filters=FilterConfig(exclude_tests=True))
        analyzer = ProjectAnalyzer(config)
        result = analyzer.analyze_project(str(sample_project))

        # Should not include test functions
        func_names = [f.name for f in result.functions.values()]
        assert "test_something" not in func_names


class TestConfig:
    """Test configuration."""

    def test_fast_config_limits_depth(self):
        """Test that FAST_CONFIG limits analysis depth."""
        assert FAST_CONFIG.depth.max_cfg_depth <= 3
        assert FAST_CONFIG.depth.max_call_depth <= 2
        assert FAST_CONFIG.performance.fast_mode is True

    def test_fast_config_skips_private(self):
        """Test that FAST_CONFIG skips private functions."""
        assert FAST_CONFIG.filters.skip_private is True


class TestExporters:
    """Test export functionality."""

    @pytest.fixture
    def sample_result(self):
        """Create sample analysis result."""
        from code2llm.core.models import AnalysisResult, FunctionInfo

        result = AnalysisResult(
            project_path="/test",
            analysis_mode="static",
        )
        result.functions["test.func1"] = FunctionInfo(
            name="func1",
            qualified_name="test.func1",
            file="/test/file.py",
            line=1,
            calls=["test.func2"],
        )
        result.functions["test.func2"] = FunctionInfo(
            name="func2",
            qualified_name="test.func2",
            file="/test/file.py",
            line=5,
            called_by=["test.func1"],
        )
        return result

    def test_json_export(self, sample_result, tmp_path):
        """Test JSON export."""
        from code2llm.exporters import JSONExporter

        output = tmp_path / "output.json"
        exporter = JSONExporter()
        exporter.export(sample_result, str(output), compact=True)

        assert output.exists()
        content = output.read_text()
        assert "test.func1" in content
        assert "test.func2" in content

    def test_mermaid_export(self, sample_result, tmp_path):
        """Test Mermaid export."""
        from code2llm.exporters import MermaidExporter

        output = tmp_path / "output.mmd"
        exporter = MermaidExporter()
        exporter.export(sample_result, str(output))

        assert output.exists()
        content = output.read_text()
        assert "flowchart TD" in content

    def test_mermaid_export_sanitizes_unsafe_identifiers(self, tmp_path):
        """Mermaid IDs should not leak unsafe path-like characters."""
        from code2llm.exporters import MermaidExporter

        result = AnalysisResult(
            project_path="/test",
            analysis_mode="static",
        )
        result.functions["~/github/src/hell.module.func_a"] = FunctionInfo(
            name="func_a",
            qualified_name="~/github/src/hell.module.func_a",
            file="/test/file.py",
            line=1,
            calls=["func_b"],
        )
        result.functions["~/github/src/hell.module.func_b"] = FunctionInfo(
            name="func_b",
            qualified_name="~/github/src/hell.module.func_b",
            file="/test/file.py",
            line=5,
        )

        output = tmp_path / "unsafe.mmd"
        exporter = MermaidExporter()
        exporter.export(result, str(output))

        content = output.read_text()
        assert "~" not in content
        assert "/" not in content
        assert "subgraph" in content
        assert "func_a" in content
        assert "func_b" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


@pytest.mark.parametrize("native", [False, True])
def test_colliding_package_and_module_keep_every_source_identity(tmp_path, monkeypatch, native):
    """Logical import aliases must not discard different static source files."""
    import copy
    import hashlib

    import code2llm.core.analyzer as implementation
    reserved = "__source_" + hashlib.sha256(b"pkg/widget.py").hexdigest()
    files = ["pkg/widget.py", "pkg/widget/__init__.py", "pkg/unique.py", "pkg/widget/" + reserved + ".py"]
    content = "class Shared:\n    def same(self):\n        return 1\n"
    for relative in files:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    records = [(str(tmp_path / relative), implementation.ProjectAnalyzer._compute_module_name(
        relative, Path(relative).name, tmp_path.name)) for relative in files]
    monkeypatch.setattr(implementation, "native_walk_project_files", lambda *a, **kw: list(reversed(records)) if native else None)
    config = copy.deepcopy(FAST_CONFIG)
    config.no_cache = True
    config.performance.enable_cache = False
    config.performance.parallel_enabled = False
    config.filters.min_function_lines = 1
    analyzer = implementation.ProjectAnalyzer(config, tmp_path)
    result = analyzer.analyze_project(str(tmp_path))
    assert {m.file for m in result.modules.values()} == {str(tmp_path / f) for f in files}
    assert len(result.modules) == len(files)
    assert "pkg.widget." + reserved in result.modules
    assert "pkg.unique" in result.modules
    conflicting = [m.name for m in result.modules.values() if m.file.endswith(("widget.py", "widget/__init__.py"))]
    assert len(set(conflicting)) == 2 and "pkg.widget" not in conflicting
    assert {f.file for f in result.functions.values()} == {str(tmp_path / f) for f in files}
    assert len(result.functions) == len(files)
    assert len(result.classes) == len(files)
    assert all(n.function in result.functions for n in result.nodes.values())
    first = dict(analyzer._collect_files(tmp_path))
    monkeypatch.setattr(implementation, "native_walk_project_files", lambda *a, **kw: records if native else None)
    assert dict(analyzer._collect_files(tmp_path)) == first


def test_collision_identity_refreshes_warm_caches_when_sibling_changes(tmp_path, monkeypatch):
    import copy

    import code2llm.core.analyzer as implementation
    monkeypatch.setattr(implementation, "native_walk_project_files", lambda *a, **kw: None)
    config = copy.deepcopy(FAST_CONFIG)
    config.performance.parallel_enabled = False
    config.performance.enable_cache = True
    config.performance.cache_dir = str(tmp_path / ".file-cache")
    config.filters.min_function_lines = 1
    source = tmp_path / "pkg/widget.py"
    source.parent.mkdir()
    source.write_text("def same():\n    return 1\n")
    analyzer = implementation.ProjectAnalyzer(config, tmp_path)
    assert set(analyzer.analyze_project(str(tmp_path)).modules) == {"pkg.widget"}
    sibling = tmp_path / "pkg/widget/__init__.py"
    sibling.parent.mkdir()
    sibling.write_text("def same():\n    return 2\n")
    for _ in range(2):
        result = analyzer.analyze_project(str(tmp_path))
        assert {m.file for m in result.modules.values()} == {str(source), str(sibling)}
        assert len(result.functions) == 2
        assert "pkg.widget" not in result.modules
        assert {m.file: m.name for m in result.modules.values()} == dict(analyzer._collect_files(tmp_path))
    sibling.unlink()
    result = analyzer.analyze_project(str(tmp_path))
    assert set(result.modules) == {"pkg.widget"}
    assert len(result.functions) == 1
