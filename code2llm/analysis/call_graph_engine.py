"""Call graph extraction and symbol call resolution engine.

Atomized module supporting:
- Multi-language call extraction via regex and native Rust acceleration (code2llm-fast-core)
- Python AST call graph extraction with caller/callee resolution
- Call graph metrics computation (fan-in, fan-out, called_by, call edges)
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from code2llm.analysis.complexity import _find_rust_binary, extract_function_body
from code2llm.analysis.utils import ast_unparse, qualified_name
from code2llm.core.config import Config
from code2llm.core.models import AnalysisResult, FlowEdge

CALL_PATTERN_C_FAMILY = re.compile(
    r"(?<!\bfunction\b\s)"
    r"(?<!\bclass\b\s)"
    r"\b([a-zA-Z_]\w*)\s*\("
    r"|"
    r"(?:this|self)\s*\.\s*(\w+)\s*\("
    r"|"
    r"\b(\w+)\s*\.\s*(\w+)\s*\("
)

_CALL_KEYWORDS = frozenset(
    {
        "if",
        "for",
        "while",
        "switch",
        "catch",
        "return",
        "throw",
        "new",
        "typeof",
        "instanceof",
        "import",
        "export",
        "require",
        "console",
        "super",
        "class",
        "function",
        "async",
        "await",
        "delete",
        "void",
        "case",
        "default",
    }
)


def _resolve_call(
    simple_call: str,
    func_qname: str,
    module_name: str,
    known_simple: Dict[str, List[str]],
    calls_seen: set[str],
    func_info: Any,
) -> None:
    """Resolve a single call name and append to func_info.calls if novel."""
    if simple_call in known_simple:
        candidates = known_simple[simple_call]
        my_module = func_qname.rsplit(".", 1)[0]
        resolved = next(
            (c for c in candidates if c.rsplit(".", 1)[0] == my_module),
            candidates[0],
        )
        if resolved != func_qname and resolved not in calls_seen:
            func_info.calls.append(resolved)
            calls_seen.add(resolved)
    else:
        ext_name = f"{module_name}.{simple_call}"
        if ext_name not in calls_seen:
            func_info.calls.append(ext_name)
            calls_seen.add(ext_name)


def _rust_batch_calls(
    lines: list[int],
    file_path: str | None = None,
    content: str | None = None,
) -> dict[int, list[str]] | None:
    """Call native Rust binary for fast batch call extraction."""
    binary = _find_rust_binary()
    if not binary or not lines:
        return None

    lines_arg = ",".join(str(l) for l in lines)
    cmd = [str(binary), "--calls", "--lines", lines_arg]

    try:
        if file_path and Path(file_path).is_file():
            cmd.extend(["--file", str(file_path)])
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=5,
            )
        elif content is not None:
            proc = subprocess.run(
                cmd,
                input=content,
                capture_output=True,
                text=True,
                check=True,
                timeout=5,
            )
        else:
            return None

        data = json.loads(proc.stdout.strip())
        result: dict[int, list[str]] = {}
        for item in data:
            result[item["line"]] = item.get("calls", [])
        return result
    except Exception:
        return None


def extract_calls_regex(
    content: str,
    module_name: str,
    result: Dict[str, Any],
    file_path: str | None = None,
) -> None:
    """Extract function calls from function bodies using regex or native Rust acceleration."""
    functions = result.get("functions", {})
    if not functions:
        return

    known_simple: Dict[str, List[str]] = {}
    for qname in functions:
        simple = qname.rsplit(".", 1)[-1]
        known_simple.setdefault(simple, []).append(qname)

    lines = [f.line for f in functions.values() if getattr(f, "line", None)]
    rust_calls = _rust_batch_calls(lines, file_path=file_path, content=content)

    for func_qname, func_info in functions.items():
        line = getattr(func_info, "line", None)
        body = extract_function_body(content, line or 1)
        if not body:
            continue
        calls_seen: set[str] = set()

        if rust_calls and line in rust_calls:
            for simple_call in rust_calls[line]:
                _resolve_call(
                    simple_call,
                    func_qname,
                    module_name,
                    known_simple,
                    calls_seen,
                    func_info,
                )
        else:
            for m in CALL_PATTERN_C_FAMILY.finditer(body):
                simple_call = m.group(1) or m.group(2) or m.group(4)
                if not simple_call or simple_call in _CALL_KEYWORDS:
                    continue
                _resolve_call(
                    simple_call,
                    func_qname,
                    module_name,
                    known_simple,
                    calls_seen,
                    func_info,
                )


def calculate_call_metrics(
    functions: Dict[str, Any],
    metrics: Dict[str, Any] | None = None,
) -> Dict[str, Dict[str, Any]]:
    """Calculate fan-in, fan-out and populate called_by for all functions."""
    for caller_name, caller_info in functions.items():
        calls = getattr(caller_info, "calls", [])
        for callee_name in calls:
            if callee_name in functions:
                callee_info = functions[callee_name]
                called_by = getattr(callee_info, "called_by", None)
                if called_by is not None and caller_name not in called_by:
                    called_by.append(caller_name)

    res_metrics = metrics if metrics is not None else {}
    for func_name, func_info in functions.items():
        calls = getattr(func_info, "calls", [])
        called_by = getattr(func_info, "called_by", [])
        fan_out = len(set(calls))
        fan_in = len(set(called_by))
        res_metrics[func_name] = {
            "fan_in": fan_in,
            "fan_out": fan_out,
            "complexity": getattr(func_info, "complexity", 1),
        }

    return res_metrics


class CallGraphExtractor(ast.NodeVisitor):
    """Extract call graph from AST with fast resolution and optional astroid inference."""

    def __init__(self, config: Config):
        self.config = config
        self.result = AnalysisResult()
        self.module_name = ""
        self.file_path = ""

        # Context
        self.function_stack: List[str] = []
        self.class_stack: List[str] = []
        self.imports: Dict[str, str] = {}
        self.astroid_tree = None

    def extract(
        self, tree: ast.AST, module_name: str, file_path: str
    ) -> AnalysisResult:
        """Extract call graph from AST."""
        self.result = AnalysisResult()
        self.module_name = module_name
        self.file_path = file_path
        self.function_stack = []
        self.class_stack = []
        self.imports = {}

        # Lazy astroid tree import (only when not skipped)
        if not getattr(self.config.performance, "skip_astroid_inference", True):
            try:
                import astroid as _astroid

                self.astroid_tree = _astroid.MANAGER.ast_from_file(file_path)
            except Exception:
                self.astroid_tree = None
        else:
            self.astroid_tree = None

        self.visit(tree)
        self._calculate_metrics()
        return self.result

    def _calculate_metrics(self) -> None:
        """Calculate fan-in and fan-out metrics (backward compatibility)."""
        calculate_call_metrics(self.result.functions, self.result.metrics)

    def visit_Import(self, node: ast.Import) -> None:
        """Track imports."""
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imports[name] = alias.name
            if hasattr(self.result, "imports"):
                self.result.imports[name] = alias.name

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Track from imports."""
        module = node.module or ""
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            full_name = f"{module}.{alias.name}" if module else alias.name
            self.imports[name] = full_name
            if hasattr(self.result, "imports"):
                self.result.imports[name] = full_name

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Visit class definition."""
        self.class_stack.append(node.name)

        self.result.classes[node.name] = {
            "file": self.file_path,
            "line": node.lineno,
            "methods": [m.name for m in node.body if isinstance(m, ast.FunctionDef)],
            "bases": [self._expr_to_str(b) for b in node.bases],
        }

        for stmt in node.body:
            self.visit(stmt)

        self.class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Visit function definition and track calls within it."""
        func_name = qualified_name(self.module_name, self.class_stack, node.name)
        self.function_stack.append(func_name)

        for stmt in node.body:
            self.visit(stmt)

        self.function_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Visit async function."""
        self.visit_FunctionDef(node)

    def visit_Call(self, node: ast.Call) -> None:
        """Track function calls."""
        if not self.function_stack:
            self.generic_visit(node)
            return

        caller = self.function_stack[-1]
        callee = self._resolve_call(node.func)

        # If ast-based resolution returned None or None.sth, try astroid if loaded
        if (not callee or "None." in callee) and self.astroid_tree:
            astroid_callee = self._resolve_with_astroid(node)
            if astroid_callee:
                callee = astroid_callee

        if callee and caller in self.result.functions:
            self.result.functions[caller].calls.append(callee)

            edge = FlowEdge(
                source=str(-1),
                target=str(-1),
                edge_type="call",
                label=f"{caller}->{callee}",
            )
            if hasattr(self.result, "call_edges"):
                self.result.call_edges.append(edge)
            else:
                self.result.edges.append(edge)

        self.generic_visit(node)

    def _resolve_call(self, node: ast.AST) -> Optional[str]:
        """Resolve a call to its full name."""
        if isinstance(node, ast.Name):
            if node.id in self.imports:
                return self.imports[node.id]
            return f"{self.module_name}.{node.id}"

        if isinstance(node, ast.Attribute):
            parts: List[str] = []
            current = node

            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value

            if isinstance(current, ast.Name):
                parts.append(current.id)
                parts.reverse()

                root = parts[0]
                if root in self.imports:
                    return f"{self.imports[root]}.{'.'.join(parts[1:])}"

                if root in ("self", "cls") and self.class_stack:
                    return f"{self.module_name}.{self.class_stack[-1]}.{'.'.join(parts[1:])}"

                return f"{self.module_name}.{'.'.join(parts)}"

        return None

    def _resolve_with_astroid(self, node: ast.Call) -> Optional[str]:
        """Use astroid to infer the call target."""
        if not self.astroid_tree:
            return None

        try:
            import astroid as _astroid

            for astroid_node in self.astroid_tree.nodes_of_class(_astroid.Call):
                if (
                    astroid_node.lineno == node.lineno
                    and astroid_node.col_offset == node.col_offset
                ):
                    inferred = astroid_node.func.infer()
                    for target in inferred:
                        if hasattr(target, "qname"):
                            return target.qname()
                    break
        except Exception:
            pass
        return None

    def _expr_to_str(self, node: ast.AST) -> str:
        """Unparse an AST expression node to a source string."""
        return ast_unparse(node, default_none="")


__all__ = [
    "CALL_PATTERN_C_FAMILY",
    "CallGraphExtractor",
    "calculate_call_metrics",
    "extract_calls_regex",
    "_resolve_call",
    "_rust_batch_calls",
]
