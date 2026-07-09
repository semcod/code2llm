"""Stałe dla FlowExporter.

Zawiera progi, wzorce wykluczeń i rekomendacje dotyczące podziału typów hub.
"""

from functools import lru_cache

# Progi dla wykrywania problemów
CC_HIGH = 15
FAN_OUT_THRESHOLD = 10
HUB_TYPE_THRESHOLD = 10

# Wzorce do wykluczenia (venv, cache, etc.)
EXCLUDE_PATTERNS = {
    "venv",
    ".venv",
    "env",
    ".env",
    "publish-env",
    "test-env",
    "site-packages",
    "node_modules",
    "__pycache__",
    ".git",
    "dist",
    "build",
    "egg-info",
    ".tox",
    ".mypy_cache",
    # Backup directories that often contain nested venvs
    ".algitex",
    ".backup",
    "backups",
    ".bak",
    # Additional venv patterns
    "virtualenv",
    ".virtualenv",
    "envs",
    ".envs",
}

# Paths where duplicate class names are intentional (twin sites, examples, contracts).
# Excluded from duplicate *detection* only — other metrics still apply.
INTENTIONAL_DUP_COPY_MARKERS: tuple[str, ...] = (
    "pc1/",
    "pc2/",
    "examples/",
    "-contract-",
)


@lru_cache(maxsize=4096)
def is_intentional_duplicate_copy(path: str) -> bool:
    """True when *path* is an intentional parallel copy (not actionable duplication)."""
    if not path:
        return False
    norm = path.replace("\\", "/").lower()
    return any(marker in norm for marker in INTENTIONAL_DUP_COPY_MARKERS)


@lru_cache(maxsize=4096)
def is_excluded_path(path: str) -> bool:
    """Return True if *path* matches any standard exclusion pattern (venv, cache, etc.)."""
    if not path:
        return False
    parts = set(path.lower().replace("\\", "/").split("/"))
    return bool(parts & EXCLUDE_PATTERNS)


# Rekomendacje podziału typów hub: typ -> sugerowane pod-interfejsy
HUB_SPLIT_RECOMMENDATIONS = {
    "AnalysisResult": [
        "StructureResult (modules, classes, functions)",
        "MetricsResult (complexity, coupling)",
        "FlowResult (call_graph, cfg, dfg)",
    ],
    "dict": ["replace with typed alternatives (dataclass/TypedDict)"],
    "str": [],  # primitive, expected to be ubiquitous
    "list": [],
    "Any": [],
}
