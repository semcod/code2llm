"""File scanning functionality for streaming analyzer."""

import ast
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from code2llm.core.models import ClassInfo, FlowNode, FunctionInfo, ModuleInfo
from code2llm.core.source_classifier import classify_source_path, is_generated_artifact

from .cache import StreamingFileCache
from .prioritizer import FilePriority
from .strategies import ScanStrategy


class StreamingScanner:
    """Handles file scanning operations."""

    def __init__(
        self, strategy: ScanStrategy, cache: Optional[StreamingFileCache] = None
    ):
        self.strategy = strategy
        self.cache = cache

    def _parse_tree(
        self, file_path: str, content: str
    ) -> Optional[ast.AST]:
        """Return a parsed AST, using cache when available, or None on SyntaxError."""
        if self.cache:
            cached = self.cache.get(file_path, content)
            if cached:
                return cached[0]
            try:
                tree = ast.parse(content)
                self.cache.put(file_path, content, (tree, content))
                return tree
            except SyntaxError:
                return None
        try:
            return ast.parse(content)
        except SyntaxError:
            return None

    def _scan_ast_nodes(self, tree: ast.AST, result: Dict, priority: FilePriority) -> None:
        """Walk AST tree and populate result with classes and functions."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                cls_info = ClassInfo(
                    name=node.name,
                    qualified_name=f"{priority.module_name}.{node.name}",
                    file=priority.file_path,
                    line=node.lineno,
                    module=priority.module_name,
                )
                result["classes"][cls_info.qualified_name] = cls_info
                result["module"].classes.append(cls_info.qualified_name)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if self.strategy.skip_private_functions and node.name.startswith("_"):
                    continue
                func_info = FunctionInfo(
                    name=node.name,
                    qualified_name=f"{priority.module_name}.{node.name}",
                    file=priority.file_path,
                    line=node.lineno,
                    module=priority.module_name,
                )
                func_info.calls.extend(
                    child.func.id
                    for child in ast.walk(node)
                    if isinstance(child, ast.Call) and isinstance(child.func, ast.Name)
                )
                result["functions"][func_info.qualified_name] = func_info
                result["module"].functions.append(func_info.qualified_name)

    def quick_scan_file(self, priority: FilePriority) -> Optional[Dict]:
        """Quick scan - extract functions and classes only (no CFG)."""
        try:
            content = Path(priority.file_path).read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return None
        tree = self._parse_tree(priority.file_path, content)
        if tree is None:
            return None
        result = {
            "module": ModuleInfo(
                name=priority.module_name,
                file=priority.file_path,
                source_kind=classify_source_path(priority.file_path),
                line_count=len(content.splitlines()),
            ),
            "functions": {},
            "classes": {},
            "nodes": {},
            "edges": [],
        }
        self._scan_ast_nodes(tree, result, priority)
        return result

    def deep_analyze_file(self, priority: FilePriority) -> Optional[Dict]:
        """Deep analysis with limited CFG generation."""
        result = self.quick_scan_file(priority)
        if not result:
            return None

        # Only build CFG for functions under node limit
        for func_name, func in result["functions"].items():
            # Skip if too many calls (simplistic heuristic)
            if len(func.calls) > 20:
                continue

            # Build simplified CFG
            entry_id = f"{func_name}_entry"
            exit_id = f"{func_name}_exit"

            result["nodes"][entry_id] = FlowNode(
                id=entry_id, type="ENTRY", label="entry", function=func_name
            )
            result["nodes"][exit_id] = FlowNode(
                id=exit_id, type="EXIT", label="exit", function=func_name
            )

            # Limit total nodes
            if len(result["nodes"]) > self.strategy.max_total_nodes:
                break

        return result

    def build_call_graph_streaming(self, results: List[Dict]) -> Dict[str, List[str]]:
        """Memory-efficient call graph construction."""
        call_graph = {}

        # Build function name lookup
        all_functions = {}
        for r in results:
            all_functions.update(r.get("functions", {}))

        # Resolve calls
        for r in results:
            for func_name, func in r.get("functions", {}).items():
                resolved_calls = []
                for called in func.calls:
                    # Try to resolve to known function
                    for known_name in all_functions:
                        if known_name.endswith(f".{called}") or known_name == called:
                            resolved_calls.append(known_name)
                            break

                func.calls = resolved_calls
                call_graph[func_name] = resolved_calls

        return call_graph

    def select_important_files(
        self, prioritized: List[FilePriority], results: List[Dict]
    ) -> List[FilePriority]:
        """Select files for deep analysis based on importance."""
        important = []

        for p in prioritized:
            # Entry points are important
            if p.is_entry_point:
                important.append(p)
                continue

            # Find result for this file
            for r in results:
                mod = r.get("module")
                if mod and mod.name == p.module_name:
                    # Files with many functions are important
                    if len(mod.functions) > 5:
                        important.append(p)
                        break

                    # Files called by many others
                    if p.import_count > 3:
                        important.append(p)
                        break

        return important

    def collect_files(self, project_path: Path) -> List[Tuple[str, str]]:
        """Collect Python files with filtering."""
        files = []

        for py_file in project_path.rglob("*.py"):
            file_str = str(py_file)

            # Apply filters
            if self.strategy.skip_test_files:
                if any(x in file_str.lower() for x in ["test", "_test", "conftest"]):
                    continue

            if any(x in file_str.lower() for x in ["__pycache__", ".venv", "venv"]):
                continue
            if is_generated_artifact(py_file, project_path):
                continue

            # Calculate module name
            rel_path = py_file.relative_to(project_path)
            parts = list(rel_path.parts)[:-1]
            if py_file.name == "__init__.py":
                module_name = ".".join(parts) if parts else project_path.name
            else:
                module_name = ".".join(parts + [py_file.stem])

            files.append((file_str, module_name))

        return files
