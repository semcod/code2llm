"""Prompt generation — prompt.txt for LLM consumption (regular and chunked)."""

# ── Public entry points ────────────────────────────────────────────────────────
# _export_prompt_txt()         : generate a single prompt.txt from output_dir.
# _export_chunked_prompt_txt() : split prompt.txt into numbered chunk files.
# ── Path / header helpers ─────────────────────────────────────────────────────
# _get_prompt_paths()          : resolve source_path and output paths.
# _build_prompt_header()       : generate introductory header lines for prompt.
# _find_existing_prompt_file() : locate pre-existing prompt source in output_dir.
# _build_prompt_file_lines()   : assemble lines from all discovered source files.
# ── Section builders ──────────────────────────────────────────────────────────
# _build_main_files_section()      : embed primary analysis files (toon, context).
# _build_optional_files_section()  : embed supplementary files if present.
# _build_subprojects_section()     : embed per-subproject summaries.
# _build_missing_files_section()   : report which expected files are absent.
# ── Utilities ─────────────────────────────────────────────────────────────────
# _format_size()               : human-readable byte count (B/KB/MB).
# _get_missing_files()         : list expected output files not yet generated.
#
# ── Output layout ─────────────────────────────────────────────────────────────
# prompt.txt structure (single-file mode):
#   [HEADER]            project path, date, token estimate.
#   [MAIN FILES]        analysis.toon.yaml, context.md (full embed).
#   [OPTIONAL FILES]    calls.yaml, flow.toon.yaml, map.toon.yaml (if present).
#   [SUBPROJECTS]       per-subproject mini-prompt blocks (if multi-project).
#   [MISSING FILES]     list of expected-but-absent output files.
#
# prompt_NNN.txt structure (chunked mode):
#   Each chunk = header + slice of main/optional content ≤ chunk_size bytes.

import time
from pathlib import Path
from typing import List, Optional, Tuple

# ── Output filename constants ──────────────────────────────────────────────────
_F_ANALYSIS_TOON = "analysis.toon"
_F_MAP_TOON = "map.toon.yaml"
_F_EVOLUTION_TOON = "evolution.toon.yaml"
_F_PROJECT_TOON_YAML = "project.toon.yaml"
_F_CONTEXT_MD = "context.md"
_F_README_MD = "README.md"
_F_PROJECT_TOON = "project.toon"
_F_VALIDATION_TOON = "project/validation.toon.yaml"
_F_DUPLICATION_TOON = "project/duplication.toon.yaml"


def _export_prompt_txt(
    args, output_dir: Path, formats: list[str], source_path: Optional[Path] = None
) -> None:
    """Generate prompt.txt useful to send to an LLM."""
    if "code2logic" not in formats and "all" not in formats:
        return

    project_path, output_rel_path = _get_prompt_paths(source_path, output_dir)
    lines = _build_prompt_header(project_path)
    lines.extend(_build_main_files_section(output_dir, output_rel_path))
    lines.extend(_build_optional_files_section(output_dir, output_rel_path))

    missing = _get_missing_files(output_dir)
    if missing:
        lines.append("")
        lines.append("Missing files (not generated in this run):")
        for name in missing:
            if output_rel_path:
                lines.append(f"- {output_rel_path}/{name}")
            else:
                lines.append(f"- {name}")

    # Analyze generated files and build dynamic footer
    file_analysis = _analyze_generated_files(output_dir)
    lines.extend(_build_prompt_footer(chunked=False, file_analysis=file_analysis))

    prompt_path = output_dir / "prompt.txt"
    t0 = time.monotonic()
    prompt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    elapsed = time.monotonic() - t0
    from .orchestrator import _inject_generation_time

    _inject_generation_time(prompt_path, elapsed)
    if args.verbose:
        print(f"  - PROMPT: {prompt_path} ({elapsed:.2f}s)")


def _export_chunked_prompt_txt(
    args,
    output_dir: Path,
    formats: list[str],
    source_path: Optional[Path] = None,
    subprojects: list = None,
) -> None:
    """Generate prompt.txt for chunked analysis with all subproject files."""
    if "code2logic" not in formats and "all" not in formats:
        return

    project_path, output_rel_path = _get_prompt_paths(source_path, output_dir)
    lines = _build_prompt_header(project_path)
    lines.extend(_build_main_files_section(output_dir, output_rel_path))
    lines.extend(_build_optional_files_section(output_dir, output_rel_path))

    if subprojects:
        lines.extend(
            _build_subprojects_section(subprojects, output_dir, output_rel_path)
        )

    lines.extend(_build_missing_files_section(output_dir, output_rel_path))

    # Analyze generated files and build dynamic footer
    file_analysis = _analyze_generated_files(output_dir, subprojects=subprojects)
    lines.extend(_build_prompt_footer(chunked=True, file_analysis=file_analysis))

    prompt_path = output_dir / "prompt.txt"
    prompt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if args.verbose:
        print(f"  - PROMPT (chunked): {prompt_path}")


# ------------------------------------------------------------------
# helpers
# ------------------------------------------------------------------
def _get_prompt_paths(source_path: Optional[Path], output_dir: Path) -> Tuple[str, str]:
    """Determine project name and relative output path."""
    if source_path:
        project_path = source_path.name if source_path.name else str(source_path)
        try:
            output_rel_path = str(output_dir.relative_to(source_path))
        except ValueError:
            # When output is not relative to source, use empty string for just filenames
            output_rel_path = ""
    else:
        cwd = Path.cwd()
        project_path = cwd.name
        try:
            output_rel_path = str(output_dir.relative_to(cwd))
        except ValueError:
            # When output is not relative to cwd, use empty string for just filenames
            output_rel_path = ""
    return project_path, output_rel_path


_MAIN_FILES = [
    (
        _F_ANALYSIS_TOON,
        "Health diagnostics - complexity metrics, god modules, coupling issues, refactoring priorities",
        (_F_ANALYSIS_TOON, "analysis.toon.yaml"),
    ),
    (
        _F_MAP_TOON,
        "Structural map - files, sizes, imports, exports, signatures, project header",
        (_F_MAP_TOON,),
    ),
    (
        _F_EVOLUTION_TOON,
        "Refactoring queue - ranked actions by impact/effort, risks, metrics targets, history",
        (_F_EVOLUTION_TOON,),
    ),
    (
        _F_PROJECT_TOON_YAML,
        "Compact project overview - generated from project.yaml data",
        (_F_PROJECT_TOON_YAML,),
    ),
    (
        _F_CONTEXT_MD,
        "LLM narrative - architecture summary and project context",
        (_F_CONTEXT_MD,),
    ),
    (_F_README_MD, "Generated documentation - overview and usage guide", (_F_README_MD,)),
]


_OPTIONAL_FILES = [
    (
        _F_PROJECT_TOON,
        "Project logic - compact module view from code2logic",
        (_F_PROJECT_TOON, "project/project.toon", "project.toon.txt"),
    ),
    (
        _F_VALIDATION_TOON,
        "Validation analysis - generated by vallm tool",
        (_F_VALIDATION_TOON,),
    ),
    (
        _F_DUPLICATION_TOON,
        "Code duplication analysis - generated by redup tool",
        (_F_DUPLICATION_TOON,),
    ),
]


def _build_prompt_header(project_path: str) -> List[str]:
    """Build header section of prompt."""
    return [
        "You are an AI assistant helping me understand and improve a codebase.",
        "Use the attached/generated files as the authoritative context.",
        "Your goal is to refactor the project based on these files, not just summarize it.",
        "",
        f"we are in project path: {project_path}",
        "",
        "Files for analysis:",
        "",
        "Note: project/validation.toon.yaml and project/duplication.toon.yaml"
        " are generated by external tools (vallm and redup)",
    ]


def _find_existing_prompt_file(
    output_dir: Path, candidates: tuple[str, ...]
) -> Optional[str]:
    """Return the first candidate path that exists, relative to output_dir."""
    for candidate in candidates:
        if (output_dir / candidate).exists():
            return candidate
    return None


def _build_prompt_file_lines(
    output_dir: Path, output_rel_path: str, files: list
) -> List[str]:
    """Build file lines for either the required or optional prompt file sections."""
    lines = []
    for _display_name, desc, candidates in files:
        existing = _find_existing_prompt_file(output_dir, candidates)
        if not existing:
            continue

        file_path = output_dir / existing
        size_str = _format_size(file_path.stat().st_size)
        if output_rel_path:
            lines.append(f"- {output_rel_path}/{existing}  ({desc}) [{size_str}]")
        else:
            lines.append(f"- {existing}  ({desc}) [{size_str}]")

    return lines


def _build_main_files_section(output_dir: Path, output_rel_path: str) -> List[str]:
    """Build main files section with size metrics."""
    return _build_prompt_file_lines(output_dir, output_rel_path, _MAIN_FILES)


def _build_optional_files_section(output_dir: Path, output_rel_path: str) -> List[str]:
    """Build optional files section with size metrics."""
    lines = _build_prompt_file_lines(output_dir, output_rel_path, _OPTIONAL_FILES)
    if not lines:
        return []

    return ["", "Optional files:", ""] + lines


def _format_size(size_bytes: int) -> str:
    """Format file size in human readable format."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes // 1024}KB"
    else:
        return f"{size_bytes // (1024 * 1024)}MB"


def _get_missing_files(output_dir: Path) -> List[str]:
    """Return names of expected main files that are missing."""
    missing = []
    for display_name, _, candidates in _MAIN_FILES:
        if _find_existing_prompt_file(output_dir, candidates) is None:
            missing.append(display_name)
    return missing


def _build_subprojects_section(
    subprojects: list, output_dir: Path, output_rel_path: str
) -> List[str]:
    """Build subprojects section with detailed file info."""
    lines = [
        "",
        "Subproject Analysis Files (hierarchical chunking for large repository):",
    ]

    for sp in subprojects:
        sp_dir = output_dir / sp.name.replace(".", "_")
        if not sp_dir.exists():
            continue

        level_name = {0: "root", 1: "L1", 2: "L2", 3: "chunk"}.get(
            sp.level, f"L{sp.level}"
        )
        sp_files = []
        total_size = 0
        for f in [_F_ANALYSIS_TOON, _F_CONTEXT_MD, _F_EVOLUTION_TOON]:
            f_path = sp_dir / f
            if f_path.exists():
                size = f_path.stat().st_size
                total_size += size
                sp_files.append(f"{f} [{_format_size(size)}]")

        if sp_files:
            size_str = _format_size(total_size)
            file_list = ", ".join(sp_files)
            lines.append(
                f"- {output_rel_path}/{sp.name.replace('.', '_')}/"
                f"  [{level_name}] Total: {size_str} - Contains: {file_list}"
            )

    return lines


def _build_missing_files_section(output_dir: Path, output_rel_path: str) -> List[str]:
    """Build missing files section."""
    missing = _get_missing_files(output_dir)
    if not missing:
        return []
    lines = ["", "Missing files (not generated in this run):"]
    for name in missing:
        # Special handling for validation and duplication files
        if name in ["validation.toon.yaml", "duplication.toon.yaml"]:
            if output_rel_path:
                lines.append(f"- {output_rel_path}/project/{name}")
            else:
                lines.append(f"- project/{name}")
        else:
            if output_rel_path:
                lines.append(f"- {output_rel_path}/{name}")
            else:
                lines.append(f"- {name}")
    return lines


# (has_key, file_key, candidate_filenames, default_path)
_OUTPUT_FILE_SPECS = [
    ("has_analysis_toon", "analysis_file",
     (_F_ANALYSIS_TOON, "analysis.toon.yaml"), _F_ANALYSIS_TOON),
    ("has_map_toon", "map_file",
     (_F_MAP_TOON,), _F_MAP_TOON),
    ("has_evolution_toon", "evolution_file",
     (_F_EVOLUTION_TOON,), _F_EVOLUTION_TOON),
    ("has_project_toon_yaml", "project_toon_file",
     (_F_PROJECT_TOON_YAML,), _F_PROJECT_TOON_YAML),
    ("has_context_md", "context_file",
     (_F_CONTEXT_MD,), _F_CONTEXT_MD),
    ("has_readme_md", "readme_file",
     (_F_README_MD,), _F_README_MD),
    ("has_project_logic", "project_logic_file",
     (_F_PROJECT_TOON, "project/project.toon", "project.toon.txt"), _F_PROJECT_TOON),
    ("has_validation_toon", "validation_file",
     (_F_VALIDATION_TOON,), _F_VALIDATION_TOON),
    ("has_duplication_toon", "duplication_file",
     (_F_DUPLICATION_TOON,), _F_DUPLICATION_TOON),
]
_ACTIONABLE_KEYS = {"has_analysis_toon", "has_map_toon", "has_evolution_toon",
                    "has_project_toon_yaml", "has_project_logic",
                    "has_validation_toon", "has_duplication_toon"}


def _probe_output_files(output_dir: Path) -> dict:
    """Probe output_dir for known generated files, returning presence flags and paths."""
    result: dict = {}
    for has_key, file_key, candidates, default in _OUTPUT_FILE_SPECS:
        found = _find_existing_prompt_file(output_dir, candidates)
        result[has_key] = found is not None
        result[file_key] = found or default
    return result


def _analyze_generated_files(output_dir: Path, subprojects: list = None) -> dict:
    """Analyze which files were generated and determine appropriate focus areas."""
    analysis = _probe_output_files(output_dir)
    analysis["is_chunked"] = bool(subprojects)
    analysis["file_count"] = sum(1 for k in _ACTIONABLE_KEYS if analysis.get(k))
    return analysis


def _build_dynamic_focus_areas(file_analysis: dict) -> List[str]:
    """Build focus areas based on generated files."""
    focus_areas = []

    analysis_file = file_analysis.get("analysis_file", "analysis.toon")
    map_file = file_analysis.get("map_file", "map.toon.yaml")
    evolution_file = file_analysis.get("evolution_file", "evolution.toon.yaml")
    project_toon_file = file_analysis.get("project_toon_file", "project.toon.yaml")
    project_logic_file = file_analysis.get("project_logic_file", "project.toon")
    validation_file = file_analysis.get(
        "validation_file", "project/validation.toon.yaml"
    )
    duplication_file = file_analysis.get(
        "duplication_file", "project/duplication.toon.yaml"
    )

    if file_analysis["has_analysis_toon"]:
        focus_areas.append(
            f"1. **Code Health Analysis** - Review complexity metrics, god modules,"
            f" coupling issues from {analysis_file}"
        )

    if file_analysis["has_map_toon"]:
        focus_areas.append(
            f"2. **Structural Map** - Use {map_file} to inspect imports, exports, signatures, and the project header"
        )

    if file_analysis["has_evolution_toon"]:
        focus_areas.append(
            f"3. **Refactoring Priorities** - Examine ranked refactoring actions"
            f" and risk assessment from {evolution_file}"
        )

    if file_analysis.get("has_project_toon_yaml"):
        focus_areas.append(
            f"4. **Project Overview** - Review the compact project overview from {project_toon_file}"
        )

    if file_analysis.get("has_project_logic"):
        focus_areas.append(
            f"5. **Project Logic** - Review the compact module overview from {project_logic_file}"
        )

    if file_analysis["has_validation_toon"]:
        focus_areas.append(
            f"6. **Validation Analysis** - Review validation results and issues"
            f" identified by vallm from {validation_file}"
        )

    if file_analysis["has_duplication_toon"]:
        focus_areas.append(
            f"7. **Code Duplication** - Examine duplicate code patterns detected by redup from {duplication_file}"
        )

    if not focus_areas:
        focus_areas.append(
            "1. **General Code Review** - Provide overall architecture assessment and improvement recommendations"
        )

    return focus_areas


def _build_dynamic_tasks(file_analysis: dict) -> List[str]:
    """Build tasks based on available files."""
    analysis_file = file_analysis.get("analysis_file", "analysis.toon")
    map_file = file_analysis.get("map_file", "map.toon.yaml")
    evolution_file = file_analysis.get("evolution_file", "evolution.toon.yaml")
    project_toon_file = file_analysis.get("project_toon_file", "project.toon.yaml")
    validation_file = file_analysis.get(
        "validation_file", "project/validation.toon.yaml"
    )
    duplication_file = file_analysis.get(
        "duplication_file", "project/duplication.toon.yaml"
    )
    project_logic_file = file_analysis.get("project_logic_file", "project.toon")

    tasks = [
        "- Treat this prompt as a refactoring brief: identify the highest-priority"
        " changes and prepare concrete edits.",
        "- Use the file set to decide whether the first pass should focus on"
        " correctness, duplication, complexity reduction, or architecture cleanup.",
        "- If you can safely implement the refactor, do it; otherwise give an exact"
        " file-by-file change plan and test plan.",
    ]

    if file_analysis["has_analysis_toon"]:
        tasks.append(
            f"- Use {analysis_file} to locate high-CC functions and god modules that should be split first."
        )

    if file_analysis["has_map_toon"]:
        tasks.append(
            f"- Keep module boundaries intact and update imports/exports according to {map_file}."
        )

    if file_analysis["has_evolution_toon"]:
        tasks.append(
            f"- Use {evolution_file} as the execution backlog and work from the top-ranked items."
        )

    if file_analysis.get("has_project_toon_yaml"):
        tasks.append(
            f"- Keep {project_toon_file} aligned with the refactored architecture."
        )

    if file_analysis.get("has_project_logic"):
        tasks.append(
            f"- Use {project_logic_file} only as a legacy cross-check when needed."
        )

    if file_analysis["has_validation_toon"]:
        tasks.append(
            f"- Treat {validation_file} as a P0 blocker and resolve validation problems before structural cleanup."
        )

    if file_analysis["has_duplication_toon"]:
        tasks.append(
            f"- Treat {duplication_file} as a P0/P1 issue and remove duplicated logic after blockers."
        )

    return tasks


def _build_priority_order(file_analysis: dict) -> List[str]:
    """Build a state-dependent priority order for refactoring."""
    analysis_file = file_analysis.get("analysis_file", "analysis.toon")
    map_file = file_analysis.get("map_file", "map.toon.yaml")
    evolution_file = file_analysis.get("evolution_file", "evolution.toon.yaml")
    project_toon_file = file_analysis.get("project_toon_file", "project.toon.yaml")
    project_logic_file = file_analysis.get("project_logic_file", "project.toon")
    validation_file = file_analysis.get(
        "validation_file", "project/validation.toon.yaml"
    )
    duplication_file = file_analysis.get(
        "duplication_file", "project/duplication.toon.yaml"
    )

    priorities = []

    if file_analysis.get("has_validation_toon"):
        priorities.append(f"P0 — Fix validation issues from {validation_file} first.")

    if file_analysis.get("has_duplication_toon"):
        priorities.append(
            f"P0/P1 — Remove duplicated logic reported in {duplication_file}."
        )

    if file_analysis.get("has_analysis_toon"):
        priorities.append(
            f"P1 — Split or simplify the highest-CC / god modules identified in {analysis_file}."
        )

    if file_analysis.get("has_map_toon"):
        priorities.append(
            f"P1 — Preserve module boundaries and update imports/exports according to {map_file}."
        )

    if file_analysis.get("has_project_toon_yaml"):
        priorities.append(
            f"P2 — Keep the compact project overview in {project_toon_file} aligned with the refactor."
        )

    if file_analysis.get("has_evolution_toon"):
        priorities.append(
            f"P2 — Execute the highest-impact items from {evolution_file} in order of benefit/risk."
        )

    if file_analysis.get("has_project_logic"):
        priorities.append(
            f"P3 — Use {project_logic_file} only as a legacy cross-check."
        )

    if not priorities:
        priorities = [
            "P1 — Inspect analysis.toon and map.toon.yaml to identify the safest first refactor.",
            "P2 — Turn the findings into concrete code edits and tests.",
            "P3 — Keep changes minimal, backward compatible, and reversible.",
        ]

    return priorities


def _build_strategy_section(file_analysis: dict) -> List[str]:
    """Build the 'Analysis Strategy' block for the prompt footer."""
    if not file_analysis.get("file_count", 0):
        return []
    lines = ["", "Analysis Strategy:"]
    if file_analysis.get("has_analysis_toon") and file_analysis.get("has_map_toon"):
        lines.append(
            f"- Start with {file_analysis.get('analysis_file', 'analysis.toon')} for health"
            f" metrics, then {file_analysis.get('map_file', 'map.toon.yaml')} for structure and signatures"
        )
        if file_analysis.get("has_evolution_toon"):
            lines.append(
                f"- Review {file_analysis.get('evolution_file', 'evolution.toon.yaml')}"
                " for action priorities and next steps"
            )
    if file_analysis.get("has_project_toon_yaml"):
        lines.append(
            f"- Compare the compact project overview in"
            f" {file_analysis.get('project_toon_file', 'project.toon.yaml')} with the main analysis files"
        )
    if file_analysis.get("has_project_logic"):
        lines.append(
            f"- Compare the compact project overview in"
            f" {file_analysis.get('project_logic_file', 'project.toon')} with the main analysis files"
        )
    if file_analysis.get("has_validation_toon"):
        lines.append(
            f"- Check {file_analysis.get('validation_file', 'project/validation.toon.yaml')}"
            " for validation issues (vallm tool output)"
        )
    if file_analysis.get("has_duplication_toon"):
        lines.append(
            f"- Examine {file_analysis.get('duplication_file', 'project/duplication.toon.yaml')}"
            " for duplicate code patterns (redup tool output)"
        )
    return lines


def _build_prompt_footer(
    chunked: bool = False, file_analysis: dict = None
) -> List[str]:
    """Build dynamic footer section of prompt based on generated files."""
    if file_analysis is None:
        file_analysis = {}

    lines = ["", "Task:"]
    lines.extend(_build_dynamic_tasks(file_analysis))

    priorities = _build_priority_order(file_analysis)
    if priorities:
        lines += ["", "Priority Order:"] + priorities

    focus_areas = _build_dynamic_focus_areas(file_analysis)
    if focus_areas:
        lines += ["", "Focus Areas for Analysis:"] + focus_areas

    lines.extend(_build_strategy_section(file_analysis))

    lines += [
        "",
        "Constraints:",
        "- Prefer minimal, incremental changes.",
        "- Maintain full backward compatibility.",
        "- Base recommendations on concrete metrics from the provided files.",
        "- If uncertain, ask clarifying questions.",
    ]

    if chunked:
        lines.extend(
            [
                "",
                "Note: This repository was analyzed using hierarchical chunking due to its size.",
                "      Start with the main files (analysis.toon, context.md) for overview,",
                "      then examine specific subproject directories as needed.",
            ]
        )

    return lines
