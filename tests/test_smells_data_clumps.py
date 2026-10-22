"""Tests for SmellDetector._detect_data_clumps.

2026-07-06 incident (same root cause as the Shotgun Surgery fix): grouping
functions by their argument-name set alone, ignoring file, meant a common
constructor shape like `(self, project_root, config)` -- conventionally
reused independently by unrelated classes across unrelated files -- falsely
triggered "Data Clump". Reproduced live:
`wup.anomaly_detector.AnomalyDetector.__init__` and
`wup.testql_monitor.TestQLMonitor.__init__` are two unrelated classes in
unrelated files, flagged as clumped on `project_root, self, config` purely
because both happen to take a project root and a config object.
"""

from __future__ import annotations

from code2llm.analysis.smells import SmellDetector
from code2llm.core.models import AnalysisResult, FunctionInfo


def _function(name: str, file: str, args: list[str], line: int = 1) -> FunctionInfo:
    return FunctionInfo(
        name=name, qualified_name=f"{file}::{name}", file=file, line=line, args=args
    )


def test_same_args_across_unrelated_files_is_not_a_data_clump():
    """The core regression: two unrelated classes in unrelated files each
    taking (self, project_root, config) must NOT be flagged."""
    result = AnalysisResult()
    result.functions["a::AnomalyDetector.__init__"] = _function(
        "AnomalyDetector.__init__", "wup/anomaly_detector.py", ["self", "project_root", "config"]
    )
    result.functions["b::TestQLMonitor.__init__"] = _function(
        "TestQLMonitor.__init__", "wup/testql_monitor.py", ["self", "project_root", "config"]
    )

    smells = SmellDetector(result)._detect_data_clumps()

    assert smells == []


def test_genuine_same_file_data_clump_still_detected():
    """Two methods in the SAME file sharing a 3+ arg signature is the real
    smell and must still be caught."""
    result = AnalysisResult()
    file = "core/session.py"
    result.functions["core.session::start"] = _function(
        "start", file, ["self", "user_id", "token", "scope"]
    )
    result.functions["core.session::refresh"] = _function(
        "refresh", file, ["self", "user_id", "token", "scope"]
    )

    smells = SmellDetector(result)._detect_data_clumps()

    assert len(smells) == 2
    assert all(s.name == "Data Clump: self, user_id, token, scope"
               or set(s.context["clump"]) == {"self", "user_id", "token", "scope"}
               for s in smells)
    assert all(s.file == file for s in smells)


def test_single_function_with_matching_args_in_other_file_not_flagged():
    """Only one function per file matches the arg-set -- no clump within
    either file, and cross-file coincidence must not count."""
    result = AnalysisResult()
    result.functions["a::f"] = _function("f", "a.py", ["self", "x", "y", "z"])
    result.functions["b::g"] = _function("g", "b.py", ["self", "x", "y", "z"])

    smells = SmellDetector(result)._detect_data_clumps()

    assert smells == []


def test_fewer_than_three_args_never_counted():
    result = AnalysisResult()
    file = "core/session.py"
    result.functions["core.session::start"] = _function("start", file, ["self", "user_id"])
    result.functions["core.session::refresh"] = _function("refresh", file, ["self", "user_id"])

    smells = SmellDetector(result)._detect_data_clumps()

    assert smells == []


def test_exported_clump_tickets_are_stable_across_processes(tmp_path):
    """The same finding must not create new ticket keys after a process restart."""
    import json
    import os
    from pathlib import Path
    import subprocess
    import sys
    import textwrap

    script = textwrap.dedent("""\
        import json
        import sys
        from dataclasses import asdict
        from code2llm.analysis.smells import SmellDetector
        from code2llm.core.models import AnalysisResult, FunctionInfo
        from code2llm.exporters.planfile_tickets import _smell_tickets

        reverse = sys.argv[1] == "reverse"
        functions = [("create_github_pr", 47), ("create_gitlab_mr", 80)]
        arguments = ["self", "provider", "group", "template"]
        if reverse:
            functions.reverse()
            arguments.reverse()
        result = AnalysisResult(project_path="/fixture")
        for name, line in functions:
            result.functions[name] = FunctionInfo(
                name=name, qualified_name="publish." + name,
                file="/fixture/publish.py", line=line, args=arguments,
            )
        result.smells = SmellDetector(result)._detect_data_clumps()
        tickets = [asdict(ticket) for ticket in _smell_tickets(result)]
        print(json.dumps(sorted(tickets, key=lambda t: t["dedupe_key"]), sort_keys=True))
        """)
    outputs = []
    root = str(Path(__file__).resolve().parents[1])
    for seed, order in [("1", "forward"), ("2", "forward"), ("42", "reverse")]:
        env = os.environ.copy()
        env["PYTHONHASHSEED"] = seed
        env["PYTHONPATH"] = root + os.pathsep + env.get("PYTHONPATH", "")
        child = subprocess.run(
            [sys.executable, "-c", script, order],
            cwd=tmp_path, env=env, check=True, capture_output=True,
            text=True, timeout=30,
        )
        tickets = json.loads(child.stdout)
        assert len(tickets) == 2
        assert len({ticket["dedupe_key"] for ticket in tickets}) == 2
        outputs.append(tickets)
    assert outputs[0] == outputs[1] == outputs[2]
