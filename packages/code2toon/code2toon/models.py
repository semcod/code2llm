"""Data models for TOON documents."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


@dataclass
class ToonHeader:
    """Header information for a TOON document."""
    project: str = ""
    generated_at: str = ""
    mean_cc: float = 0.0
    critical_count: int = 0
    duplicate_count: int = 0
    cycle_count: int = 0


@dataclass
class FunctionEntry:
    """Function metrics entry in TOON."""
    name: str
    cc: float
    file: Optional[str] = None
    line: Optional[int] = None


@dataclass
class ToonDocument:
    """Structured representation of a parsed TOON document."""
    header: ToonHeader = field(default_factory=ToonHeader)
    health: List[str] = field(default_factory=list)
    functions: List[FunctionEntry] = field(default_factory=list)
    classes: List[str] = field(default_factory=list)
    hotspots: List[str] = field(default_factory=list)
    raw_data: Dict[str, Any] = field(default_factory=dict)
