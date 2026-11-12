"""Stable public API for code2llm — primary entry point for external consumers.

This module provides a clean, stable interface for tools like code2docs
that depend on code2llm's analysis capabilities.
"""

from pathlib import Path
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
import os
import sys
import time
from typing import Optional

from .core.config import Config, FAST_CONFIG, analysis_config_digest, analysis_runtime_identity
from .core.models import (
    AnalysisResult,
    FunctionInfo,
    ClassInfo,
    ModuleInfo,
    Pattern,
    CodeSmell,
    FlowNode,
    FlowEdge,
    DataFlow,
    Mutation,
)


def analyze(project_path: str, config: Optional[Config] = None) -> AnalysisResult:
    """Analyze a Python project and return structured results.

    This is the main entry point for external consumers of code2llm.

    Args:
        project_path: Path to the project directory to analyze.
        config: Optional analysis configuration. Defaults to FAST_CONFIG.

    Returns:
        AnalysisResult with functions, classes, modules, call graph, patterns, etc.
    """
    from .core.analyzer import ProjectAnalyzer

    config = config or FAST_CONFIG
    analyzer = ProjectAnalyzer(config)
    return analyzer.analyze_project(project_path)


def analyze_file(file_path: str, config: Optional[Config] = None) -> AnalysisResult:
    """Analyze a single Python file.

    Args:
        file_path: Path to the Python file to analyze.
        config: Optional analysis configuration.

    Returns:
        AnalysisResult for the single file.
    """
    from .core.analyzer import ProjectAnalyzer

    return ProjectAnalyzer(config or FAST_CONFIG).analyze_file(file_path)


@dataclass(frozen=True)
class IncrementalAnalysis:
    """Versioned observation and reused analysis; not an atomic execution snapshot."""

    analysis: AnalysisResult
    identity: dict
    incremental: dict


def analyze_incremental(project_path: str, *, cache_dir: str,
                        config: Optional[Config] = None, cache_policy: str = "content",
                        changed_files=None) -> IncrementalAnalysis:
    """Reuse private per-file results, verifying bytes and relinking the full graph.

    ``changed_files`` is an advisory hint, including deleted relative paths. All
    selected files are still verified, so an incomplete hint cannot hide edits.
    ``content`` reads only this caller-owned private cache; ``off`` never reads
    cached pickle. Pickle is internal trusted state, never a host exchange format.
    Config/analyzer/parser identities invalidate reuse. Phase timings distinguish
    content verification, per-file analysis dispatch and complete graph linking.
    The before/after observation detects drift but cannot exclude ABA races;
    execute refactors only against a separately immutable snapshot.
    """
    from . import __version__
    from .core.analyzer import ProjectAnalyzer

    if cache_policy not in {"content", "off"}:
        raise ValueError("cache_policy must be content or off")
    root = Path(project_path).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Expected a project directory")
    cache = Path(cache_dir).resolve()
    if cache.is_relative_to(root):
        raise ValueError("Private analysis cache must be outside the source project")
    hints = set()
    if isinstance(changed_files, (str, bytes, Path)):
        raise TypeError("Changed-file hints must be an iterable of paths")
    for value in changed_files or ():
        path = Path(value)
        path = (root / path).resolve() if not path.is_absolute() else path.resolve()
        if not path.is_relative_to(root) or path == root:
            raise ValueError("Changed-file hint escapes the source project")
        hints.add(path.relative_to(root).as_posix())
    cfg = deepcopy(config or FAST_CONFIG)
    config_digest = analysis_config_digest(cfg)
    if cache_policy == "content":
        cache.mkdir(mode=0o700, parents=True, exist_ok=True)
        info = cache.stat()
        if info.st_uid != os.geteuid() or info.st_mode & 0o077:
            raise ValueError("Persistent cache must be a private caller-owned directory")
        cfg.performance.cache_dir = str(cache / "file-cache")
        cfg.persistent_cache_root = str(cache / "persistent")
    else:
        cfg.performance.enable_cache = False
        cfg.no_cache = True
    analyzer = ProjectAnalyzer(cfg, root)

    def inventory():
        selected = {}
        for path, _ in sorted(analyzer._collect_files(root)):
            source = Path(path)
            if not source.resolve(strict=True).is_relative_to(root):
                raise ValueError("Selected source escapes the project root")
            selected[source.relative_to(root).as_posix()] = hashlib.sha256(source.read_bytes()).hexdigest()
        return selected

    started = time.perf_counter()
    before = inventory()
    inventory_seconds = time.perf_counter() - started
    result = analyzer.analyze_project(str(root))
    started = time.perf_counter()
    if inventory() != before:
        raise RuntimeError("Source changed during analysis; discard the observation")
    inventory_seconds += time.perf_counter() - started
    identity = dict(schema="code2llm.incremental/v1", analyzer_version=__version__,
                    parser_runtime=sys.implementation.cache_tag, runtime=analysis_runtime_identity(),
                    config_sha256=config_digest,
                    files=before, snapshot_atomic=False)
    payload = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
    identity["snapshot_sha256"] = hashlib.sha256(payload).hexdigest()
    stats = dict(analyzer.incremental_stats, inventory_seconds=inventory_seconds,
                 cache_policy=cache_policy,
                 changed_files_hint=sorted(hints))
    return IncrementalAnalysis(result, identity, stats)


__all__ = [
    "analyze",
    "analyze_file",
    "analyze_incremental",
    "IncrementalAnalysis",
    "Config",
    "FAST_CONFIG",
    "AnalysisResult",
    "FunctionInfo",
    "ClassInfo",
    "ModuleInfo",
    "Pattern",
    "CodeSmell",
    "FlowNode",
    "FlowEdge",
    "DataFlow",
    "Mutation",
]
