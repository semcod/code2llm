"""Diffing engine for TOON documents to detect architectural drift."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Union
from pathlib import Path

from .parser import load_toon_document
from .models import ToonDocument


@dataclass
class ToonDiffResult:
    """Result of diffing two TOON documents."""
    cc_delta: float = 0.0
    added_functions: List[str] = field(default_factory=list)
    removed_functions: List[str] = field(default_factory=list)
    added_classes: List[str] = field(default_factory=list)
    removed_classes: List[str] = field(default_factory=list)
    added_health_issues: List[str] = field(default_factory=list)
    resolved_health_issues: List[str] = field(default_factory=list)

    @property
    def has_drift(self) -> bool:
        """Check if any architectural drift occurred."""
        return (
            abs(self.cc_delta) > 0.01
            or bool(self.added_functions)
            or bool(self.removed_functions)
            or bool(self.added_classes)
            or bool(self.removed_classes)
            or bool(self.added_health_issues)
        )


def diff_toon(
    base: Union[str, Path, ToonDocument],
    head: Union[str, Path, ToonDocument],
) -> ToonDiffResult:
    """Compare base and head TOON documents to detect architectural drift."""
    doc_base = load_toon_document(base) if not isinstance(base, ToonDocument) else base
    doc_head = load_toon_document(head) if not isinstance(head, ToonDocument) else head

    diff = ToonDiffResult()
    diff.cc_delta = round(doc_head.header.mean_cc - doc_base.header.mean_cc, 2)

    base_funcs = {f.name for f in doc_base.functions}
    head_funcs = {f.name for f in doc_head.functions}
    diff.added_functions = sorted(list(head_funcs - base_funcs))
    diff.removed_functions = sorted(list(base_funcs - head_funcs))

    base_classes = set(doc_base.classes)
    head_classes = set(doc_head.classes)
    diff.added_classes = sorted(list(head_classes - base_classes))
    diff.removed_classes = sorted(list(base_classes - head_classes))

    base_health = set(doc_base.health)
    head_health = set(doc_head.health)
    diff.added_health_issues = sorted(list(head_health - base_health))
    diff.resolved_health_issues = sorted(list(base_health - head_health))

    return diff
