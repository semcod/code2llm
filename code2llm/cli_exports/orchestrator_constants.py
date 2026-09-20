"""Export orchestrator constants — format filenames, labels, and dry-run mappings.

This module centralizes all format-related constants for the export system
to avoid duplication and enable easier maintenance.
"""

import re
from typing import Dict, FrozenSet, List


# Format output filenames
FORMAT_FILENAMES: Dict[str, str] = {
    "toon": "analysis.toon.yaml",
    "map": "map.toon.yaml",
    "flow": "flow.toon.yaml",
    "context": "context.md",
    "yaml": "analysis.yaml",
    "json": "analysis.json",
    "evolution": "evolution.toon.yaml",
    "planfile": "planfile-tickets.yaml",
    "readme": "README.md",
    "project-yaml": "project.yaml",
}

# Files produced per format in dry-run preview
FORMAT_DRY_RUN_FILES: Dict[str, List[str]] = {
    "toon": ["analysis.toon"],
    "map": ["map.toon.yaml"],
    "evolution": ["evolution.toon.yaml"],
    "planfile": ["planfile-tickets.yaml"],
    "context": ["context.md"],
    "mermaid": ["calls.mmd", "calls.png"],
    "yaml": ["analysis.yaml"],
    "json": ["analysis.json"],
    "readme": ["README.md"],
}

# Human-readable labels
FORMAT_LABELS: Dict[str, str] = {
    "toon": "TOON (diagnostics)",
    "map": "MAP (structure)",
    "flow": "FLOW (data-flow)",
    "context": "CONTEXT (LLM narrative)",
    "yaml": "YAML",
    "json": "JSON",
    "evolution": "EVOLUTION (refactoring queue)",
    "planfile": "PLANFILE (ticket suggestions)",
    "readme": "README (documentation)",
    "project-yaml": "PROJECT-YAML (single source of truth)",
}

# ---------------------------------------------------------------------------
# Export-cache ownership
# ---------------------------------------------------------------------------
# The export-level cache must only snapshot/restore artifacts that code2llm
# itself produces. Foreign tools may write their exports into the same output
# directory (redup → duplication.toon.yaml, vallm → validation.toon.yaml);
# caching those snapshots and restoring them on cache hits silently reverts
# newer foreign exports to whatever happened to sit in the output directory
# when the cache entry was created (PLF-211 regression).

# Subdirectories written by code2llm handlers (refactor prompts, separated and
# split export layouts, code2logic candidate output).
CACHEABLE_EXPORT_DIRS: FrozenSet[str] = frozenset(
    {
        "prompts",
        "separated",
        "split",
        "project",
    }
)

# Output files written by handlers that are not covered by the format
# registries above (mermaid diagrams + rendered PNGs, call graphs, project
# overview, prompt bundle, file browser index, data structures, code2logic).
CACHEABLE_EXPORT_EXTRA_FILES: FrozenSet[str] = frozenset(
    {
        "flow.mmd",
        "calls.mmd",
        "compact_flow.mmd",
        "flow_detailed.mmd",
        "flow_full.mmd",
        "flow.png",
        "calls.png",
        "compact_flow.png",
        "flow_detailed.png",
        "flow_full.png",
        "calls.yaml",
        "calls.toon.yaml",
        "data_structures.yaml",
        "project.toon.yaml",
        "project.toon",
        "project.toon.txt",
        "prompt.txt",
        "index.html",
    }
)

# code2logic oversized-output split parts: project_part2.toon, project_part3…
_CODE2LOGIC_PART_RE = re.compile(r"project_part\d+\.toon\Z")

_CACHEABLE_EXPORT_FILES: FrozenSet[str] = frozenset(
    {name for names in FORMAT_DRY_RUN_FILES.values() for name in names}
) | frozenset(FORMAT_FILENAMES.values()) | CACHEABLE_EXPORT_EXTRA_FILES


def is_cacheable_export_name(name: str) -> bool:
    """Return True when *name* is a code2llm-owned export artifact name.

    Used by the export-level cache: only owned names are copied into the
    cache and only owned names are restored from it, so foreign artifacts
    that merely live in the output directory are never reverted.
    """
    if name in _CACHEABLE_EXPORT_FILES or name in CACHEABLE_EXPORT_DIRS:
        return True
    return _CODE2LOGIC_PART_RE.fullmatch(name) is not None


__all__ = [
    "CACHEABLE_EXPORT_DIRS",
    "CACHEABLE_EXPORT_EXTRA_FILES",
    "FORMAT_DRY_RUN_FILES",
    "FORMAT_FILENAMES",
    "FORMAT_LABELS",
    "is_cacheable_export_name",
]
