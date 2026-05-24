"""Planfile ticket exporter for code2llm findings."""

import json
import re
import subprocess
from collections.abc import Callable, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Optional

import yaml

from code2llm.core.models import AnalysisResult, ClassInfo, FunctionInfo

from .base import BaseExporter, export_format

Runner = Callable[[Sequence[str], Path], subprocess.CompletedProcess[str]]

_PRIORITY_RANK = {"critical": 0, "high": 1, "normal": 2, "low": 3}
_TERMINAL_STATUSES = {"done", "closed", "canceled", "cancelled"}
_CC_LIMIT = 15
_GOD_MODULE_LINES = 500
_GOD_MODULE_CLASSES = 4


@dataclass(frozen=True)
class PlanfileTicketSuggestion:
    """One planfile-ready ticket derived from code2llm analysis."""

    signal: str
    title: str
    description: str
    priority: str = "normal"
    labels: tuple[str, ...] = ()
    files: tuple[str, ...] = ()
    dedupe_key: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def collect_planfile_tickets(
    result: AnalysisResult,
    *,
    limit: int | None = None,
) -> list[PlanfileTicketSuggestion]:
    """Build actionable planfile ticket suggestions from an analysis result."""
    suggestions: list[PlanfileTicketSuggestion] = []
    suggestions.extend(_high_cc_tickets(result))
    suggestions.extend(_god_module_tickets(result))
    suggestions.extend(_duplicate_class_tickets(result))
    suggestions.extend(_smell_tickets(result))

    unique: dict[str, PlanfileTicketSuggestion] = {}
    for suggestion in suggestions:
        unique.setdefault(suggestion.dedupe_key or suggestion.title, suggestion)

    ordered = sorted(
        unique.values(),
        key=lambda item: (_PRIORITY_RANK.get(item.priority, 99), item.signal, item.title),
    )
    if limit is not None and limit >= 0:
        return ordered[:limit]
    return ordered


def apply_planfile_tickets(
    suggestions: Sequence[PlanfileTicketSuggestion],
    *,
    project_root: Path,
    source: str = "code2llm",
    sprint: str = "current",
    runner: Runner | None = None,
) -> tuple[list[str], list[str]]:
    """Create suggestions as planfile tickets, skipping active duplicates."""
    use_runner = runner or _default_runner
    existing = _existing_planfile_titles(project_root, source=source, runner=use_runner)
    applied: list[str] = []
    skipped: list[str] = []
    for suggestion in suggestions:
        if suggestion.title in existing:
            skipped.append(suggestion.title)
            continue
        cmd = [
            "planfile",
            "ticket",
            "create",
            suggestion.title,
            "--priority",
            suggestion.priority,
            "--sprint",
            sprint,
            "--source",
            source,
            "--description",
            _description_with_dedupe(suggestion),
        ]
        for label in suggestion.labels:
            cmd.extend(["--label", label])
        for file_path in suggestion.files:
            cmd.extend(["--files", file_path])
        try:
            result = use_runner(cmd, project_root)
        except (FileNotFoundError, OSError):
            skipped.append(suggestion.title)
            continue
        if result.returncode == 0:
            applied.append(suggestion.title)
            existing.add(suggestion.title)
        else:
            skipped.append(suggestion.title)
    return applied, skipped


@export_format(
    "planfile",
    description="Planfile ticket suggestions from code2llm analysis",
    extension=".yaml",
)
class PlanfileTicketsExporter(BaseExporter):
    """Export code2llm findings as planfile-ready tickets."""

    def export(
        self,
        result: AnalysisResult,
        output_path: str,
        **kwargs: Any,
    ) -> Optional[Path]:
        limit = kwargs.get("limit")
        suggestions = collect_planfile_tickets(
            result,
            limit=limit if isinstance(limit, int) else None,
        )
        project_root = _project_root(result, kwargs.get("project_root"))
        source = str(kwargs.get("source") or "code2llm")
        sprint = str(kwargs.get("sprint") or "current")
        applied: list[str] = []
        skipped: list[str] = []
        if kwargs.get("apply"):
            applied, skipped = apply_planfile_tickets(
                suggestions,
                project_root=project_root,
                source=source,
                sprint=sprint,
                runner=kwargs.get("runner"),
            )

        payload = {
            "source": source,
            "schema": "code2llm.planfile_tickets.v1",
            "project_root": str(project_root),
            "tickets": [suggestion.to_dict() for suggestion in suggestions],
            "applied": applied,
            "skipped": skipped,
        }
        path = self._ensure_dir(output_path)
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        return path


def _high_cc_tickets(result: AnalysisResult) -> list[PlanfileTicketSuggestion]:
    tickets: list[PlanfileTicketSuggestion] = []
    for func in result.functions.values():
        cc = _function_cc(func)
        if cc < _CC_LIMIT:
            continue
        rel = _rel_path(func.file, result.project_path)
        priority = "high" if cc >= 25 else "normal"
        title = f"Reduce cyclomatic complexity: {func.qualified_name} (CC={cc})"
        tickets.append(
            PlanfileTicketSuggestion(
                signal="code2llm_cc",
                title=title,
                description=(
                    f"code2llm reports `{func.qualified_name}` at `{rel}:{func.line}` "
                    f"with cyclomatic complexity {cc} (limit {_CC_LIMIT}).\n\n"
                    "Extract smaller functions, flatten conditionals, or split strategy "
                    "branches. Re-run code2llm after the change and keep tests green."
                ),
                priority=priority,
                labels=("llm-ready", "code2llm", "complexity", "refactor"),
                files=(rel,),
                dedupe_key=f"code2llm:cc:{rel}:{func.qualified_name}",
            ),
        )
    return tickets


def _god_module_tickets(result: AnalysisResult) -> list[PlanfileTicketSuggestion]:
    tickets: list[PlanfileTicketSuggestion] = []
    for module in result.modules.values():
        class_count = len(module.classes)
        if module.line_count < _GOD_MODULE_LINES or class_count < _GOD_MODULE_CLASSES:
            continue
        rel = _rel_path(module.file, result.project_path)
        tickets.append(
            PlanfileTicketSuggestion(
                signal="code2llm_god",
                title=f"Split god module: {rel}",
                description=(
                    f"code2llm reports `{rel}` as a large module "
                    f"({module.line_count} lines, {class_count} classes).\n\n"
                    "Split it by responsibility, keep public imports stable, and add focused "
                    "tests around the moved behavior."
                ),
                priority="high",
                labels=("llm-ready", "code2llm", "god-module", "refactor"),
                files=(rel,),
                dedupe_key=f"code2llm:god:{rel}",
            ),
        )
    return tickets


def _duplicate_class_tickets(result: AnalysisResult) -> list[PlanfileTicketSuggestion]:
    tickets: list[PlanfileTicketSuggestion] = []
    classes = list(result.classes.values())
    for index, left in enumerate(classes):
        left_methods = _method_names(left)
        if len(left_methods) < 3:
            continue
        for right in classes[index + 1 :]:
            if left.name != right.name:
                continue
            right_methods = _method_names(right)
            if len(right_methods) < 3:
                continue
            overlap = left_methods & right_methods
            union = left_methods | right_methods
            if not union or len(overlap) / len(union) < 0.6:
                continue
            left_file = _rel_path(left.file, result.project_path)
            right_file = _rel_path(right.file, result.project_path)
            tickets.append(
                PlanfileTicketSuggestion(
                    signal="code2llm_dup",
                    title=f"Consolidate duplicate class {left.name}",
                    description=(
                        f"code2llm found similar `{left.name}` classes in `{left_file}` "
                        f"and `{right_file}` with {len(overlap)} overlapping methods.\n\n"
                        "Extract a shared base/helper or merge the duplicated behavior, then "
                        "re-run code2llm to confirm the duplicate signal is gone."
                    ),
                    priority="high",
                    labels=("llm-ready", "code2llm", "duplication", "refactor"),
                    files=(left_file, right_file),
                    dedupe_key=f"code2llm:dup:{left.name}:{left_file}:{right_file}",
                ),
            )
    return tickets


def _smell_tickets(result: AnalysisResult) -> list[PlanfileTicketSuggestion]:
    tickets: list[PlanfileTicketSuggestion] = []
    for smell in result.smells:
        if smell.type == "god_function" and smell.context.get("complexity", 0) >= _CC_LIMIT:
            continue
        rel = _rel_path(smell.file, result.project_path)
        priority = "high" if smell.severity >= 0.75 else "normal"
        label = re.sub(r"[^a-z0-9-]+", "-", smell.type.lower()).strip("-")
        tickets.append(
            PlanfileTicketSuggestion(
                signal=f"code2llm_smell_{smell.type}",
                title=f"Address code smell: {smell.name}",
                description=(
                    f"code2llm reports `{smell.name}` in `{rel}:{smell.line}`.\n\n"
                    f"{smell.description}\n\n"
                    "Make the smallest refactor that removes the smell and run local tests."
                ),
                priority=priority,
                labels=("llm-ready", "code2llm", "code-smell", label),
                files=(rel,),
                dedupe_key=f"code2llm:smell:{smell.type}:{rel}:{smell.line}:{smell.name}",
            ),
        )
    return tickets


def _function_cc(func: FunctionInfo) -> int:
    raw = func.complexity.get("cyclomatic_complexity", func.complexity.get("cc", 0))
    try:
        return int(raw)
    except (TypeError, ValueError):
        return 0


def _method_names(cls: ClassInfo) -> set[str]:
    return {method.split(".")[-1] for method in cls.methods}


def _rel_path(path: str, project_path: str) -> str:
    if not path:
        return ""
    raw = Path(path)
    if not raw.is_absolute():
        return raw.as_posix()
    try:
        return raw.relative_to(Path(project_path).resolve()).as_posix()
    except (OSError, ValueError):
        return raw.as_posix()


def _project_root(result: AnalysisResult, override: object = None) -> Path:
    if override:
        return Path(str(override)).resolve()
    if result.project_path:
        return Path(result.project_path).resolve()
    return Path.cwd().resolve()


def _description_with_dedupe(suggestion: PlanfileTicketSuggestion) -> str:
    if not suggestion.dedupe_key:
        return suggestion.description
    return f"{suggestion.description}\n\ncode2llm-dedupe: {suggestion.dedupe_key}"


def _default_runner(
    cmd: Sequence[str],
    cwd: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(cmd),
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )


def _existing_planfile_titles(
    project_root: Path,
    *,
    source: str,
    runner: Runner,
) -> set[str]:
    try:
        result = runner(
            ["planfile", "ticket", "list", "--source", source, "--format", "json"],
            project_root,
        )
    except (FileNotFoundError, OSError):
        return set()
    if result.returncode != 0:
        return set()
    try:
        payload = json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        return set()
    if not isinstance(payload, list):
        return set()
    titles: set[str] = set()
    for entry in payload:
        if not isinstance(entry, dict):
            continue
        status = str(entry.get("status") or "").lower()
        if status in _TERMINAL_STATUSES:
            continue
        title = entry.get("name") or entry.get("title")
        if isinstance(title, str) and title:
            titles.add(title)
    return titles