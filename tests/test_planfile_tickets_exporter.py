import json
import subprocess
from pathlib import Path

import yaml

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from code2llm.cli_exports.orchestrator import _expand_all_formats, _export_single_project
from code2llm.core.models import AnalysisResult, ClassInfo, CodeSmell, FunctionInfo, ModuleInfo
from code2llm.exporters.planfile_tickets import (
    PlanfileTicketsExporter,
    apply_planfile_tickets,
    collect_planfile_tickets,
)


def _sample_result(project: Path) -> AnalysisResult:
    result = AnalysisResult(project_path=str(project))
    result.modules["pkg.big"] = ModuleInfo(
        name="pkg.big",
        file=str(project / "pkg" / "big.py"),
        line_count=900,
        classes=["pkg.big.A", "pkg.big.B", "pkg.big.C", "pkg.big.D"],
    )
    result.functions["pkg.big.complex"] = FunctionInfo(
        name="complex",
        qualified_name="pkg.big.complex",
        file=str(project / "pkg" / "big.py"),
        line=42,
        complexity={"cyclomatic_complexity": 18},
    )
    result.classes["pkg.one.Worker"] = ClassInfo(
        name="Worker",
        qualified_name="pkg.one.Worker",
        file=str(project / "pkg" / "one.py"),
        line=10,
        methods=["pkg.one.Worker.load", "pkg.one.Worker.save", "pkg.one.Worker.run"],
    )
    result.classes["pkg.two.Worker"] = ClassInfo(
        name="Worker",
        qualified_name="pkg.two.Worker",
        file=str(project / "pkg" / "two.py"),
        line=12,
        methods=["pkg.two.Worker.load", "pkg.two.Worker.save", "pkg.two.Worker.run"],
    )
    result.smells.append(
        CodeSmell(
            name="cycle between pkg.one and pkg.two",
            type="circular_dependency",
            file=str(project / "pkg" / "one.py"),
            line=1,
            severity=0.9,
            description="Modules import each other.",
        ),
    )
    return result


def test_all_format_includes_planfile_manifest() -> None:
    assert "planfile" in _expand_all_formats(["all"])


def test_planfile_apply_adds_planfile_export_even_when_not_requested(tmp_path: Path) -> None:
    args = SimpleNamespace(
        verbose=False,
        refactor=False,
        data_structures=False,
        format="toon",
        full=False,
        planfile_apply=True,
        planfile_source="code2llm",
        planfile_sprint="current",
        planfile_project=None,
        planfile_limit=None,
    )

    with patch("code2llm.cli_exports.orchestrator.get_exporter") as get_exporter, patch(
        "code2llm.cli_exports.orchestrator._export_readme"
    ), patch("code2llm.cli_exports.orchestrator._export_index_html"):
        exporter = MagicMock()
        get_exporter.return_value = lambda: exporter
        _export_single_project(
            args,
            MagicMock(),
            tmp_path,
            ["toon"],
            requested_formats=["toon"],
            source_path=tmp_path,
        )

    exported_paths = [call.args[1] for call in exporter.export.call_args_list]
    assert str(tmp_path / "planfile-tickets.yaml") in exported_paths


def test_collect_planfile_tickets_surfaces_actionable_findings(tmp_path: Path) -> None:
    tickets = collect_planfile_tickets(_sample_result(tmp_path))

    signals = {ticket.signal for ticket in tickets}
    assert {"code2llm_cc", "code2llm_god", "code2llm_dup"}.issubset(signals)
    assert any(ticket.signal == "code2llm_smell_circular_dependency" for ticket in tickets)
    assert all("llm-ready" in ticket.labels for ticket in tickets)


def test_planfile_exporter_writes_manifest(tmp_path: Path) -> None:
    output = tmp_path / "planfile-tickets.yaml"

    PlanfileTicketsExporter().export(_sample_result(tmp_path), str(output))

    payload = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert payload["schema"] == "code2llm.planfile_tickets.v1"
    assert payload["tickets"]
    assert payload["tickets"][0]["priority"] == "high"
    assert any(ticket["signal"] == "code2llm_god" for ticket in payload["tickets"])


def test_apply_planfile_tickets_skips_active_duplicates(tmp_path: Path) -> None:
    suggestions = collect_planfile_tickets(_sample_result(tmp_path), limit=2)
    existing_title = suggestions[0].title
    calls: list[list[str]] = []

    def runner(cmd, cwd):
        assert cwd == tmp_path
        if cmd[:5] == ["planfile", "ticket", "list", "--source", "code2llm"]:
            return subprocess.CompletedProcess(
                cmd,
                0,
                stdout=json.dumps([{"name": existing_title, "status": "open"}]),
                stderr="",
            )
        calls.append(list(cmd))
        return subprocess.CompletedProcess(cmd, 0, stdout="Created PLF-001", stderr="")

    applied, skipped = apply_planfile_tickets(
        suggestions,
        project_root=tmp_path,
        runner=runner,
    )

    assert skipped == [existing_title]
    assert applied == [suggestions[1].title]
    assert len(calls) == 1
    assert calls[0][:3] == ["planfile", "ticket", "create"]
    assert "--label" in calls[0]
    assert "--files" in calls[0]