"""Regression: duplicate class groups vs pairwise pairs (IFURI-245)."""

from __future__ import annotations

from pathlib import Path

from code2llm.core.models import AnalysisResult, ClassInfo
from code2llm.exporters.flow_constants import is_intentional_duplicate_copy
from code2llm.exporters.planfile_tickets import collect_planfile_tickets
from code2llm.exporters.toon.metrics_duplicates import DuplicatesMetricsComputer
from code2llm.exporters.toon.metrics_health import HealthMetricsComputer


def _worker(file: Path, pkg: str) -> ClassInfo:
    methods = [f"{pkg}.Worker.load", f"{pkg}.Worker.save", f"{pkg}.Worker.run"]
    return ClassInfo(
        name="Worker",
        qualified_name=f"{pkg}.Worker",
        file=str(file),
        line=1,
        methods=methods,
    )


def test_intentional_copy_paths_are_detected() -> None:
    assert is_intentional_duplicate_copy("/repo/pc1/net-user-pl/handler.py")
    assert is_intentional_duplicate_copy("/repo/examples/demo/foo.py")
    assert is_intentional_duplicate_copy("/repo/urirun-contract-windowpair/x.py")
    assert not is_intentional_duplicate_copy("/repo/app/src/handler.py")


def test_duplicate_groups_not_pair_count(tmp_path: Path) -> None:
    project = tmp_path
    result = AnalysisResult(project_path=str(project))
    for index in range(4):
        pkg = f"pkg{index}"
        path = project / f"{pkg}.py"
        path.write_text("# stub\n", encoding="utf-8")
        result.classes[f"{pkg}.Worker"] = _worker(path, pkg)

    dupes = DuplicatesMetricsComputer(str(project)).detect_duplicates(result)
    assert len(dupes) == 6  # C(4,2) pairs for same class name

    ctx = {
        "duplicates": dupes,
        "files": {str(project / f"pkg{i}.py"): {"lines": 10} for i in range(4)},
        "result": result,
        "health": [],
        "func_metrics": [],
    }
    issues = HealthMetricsComputer().compute_health(ctx)
    dup_issue = next(i for i in issues if i["code"] == "DUP")
    assert "1 duplicate class groups" in dup_issue["message"]


def test_planfile_dup_ticket_uses_stable_group_dedupe_key(tmp_path: Path) -> None:
    project = tmp_path
    result = AnalysisResult(project_path=str(project))
    for pkg in ("one", "two", "three"):
        path = project / f"{pkg}.py"
        path.write_text("# stub\n", encoding="utf-8")
        result.classes[f"pkg.{pkg}.Worker"] = _worker(path, f"pkg.{pkg}")

    dup_tickets = [t for t in collect_planfile_tickets(result) if t.signal == "code2llm_dup"]
    assert len(dup_tickets) == 1
    assert dup_tickets[0].dedupe_key == "code2llm:dup:Worker"
    assert len(dup_tickets[0].files) == 3


def test_examples_dir_excluded_from_duplicate_pairs(tmp_path: Path) -> None:
    project = tmp_path
    result = AnalysisResult(project_path=str(project))
    for pkg in ("app/main", "examples/demo"):
        path = project / f"{pkg}.py"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# stub\n", encoding="utf-8")
        result.classes[f"{pkg}.Worker"] = _worker(path, pkg.replace("/", "."))

    dupes = DuplicatesMetricsComputer(str(project)).detect_duplicates(result)
    assert dupes == []
