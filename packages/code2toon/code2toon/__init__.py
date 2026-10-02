"""code2toon: TOON (Topology Oriented Object Notation) specification and tooling."""

from .models import ToonDocument, ToonHeader, FunctionEntry
from .parser import (
    is_toon_file,
    parse_toon_content,
    load_toon,
    load_toon_document,
)
from .validator import ToonValidator, validate_toon
from .diff import ToonDiffResult, diff_toon

__version__ = "0.1.0"

__all__ = [
    "ToonDocument",
    "ToonHeader",
    "FunctionEntry",
    "is_toon_file",
    "parse_toon_content",
    "load_toon",
    "load_toon_document",
    "ToonValidator",
    "validate_toon",
    "ToonDiffResult",
    "diff_toon",
    "__version__",
]
