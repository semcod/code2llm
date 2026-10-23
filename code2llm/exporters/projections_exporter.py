"""Bounded, versioned projections of code2llm analysis for intent retrieval.

Emits ``projections.json``: a deterministic, capped catalog of source
symbols with provenance (kind, symbol, file, line) and content digests.
Downstream consumers (e.g. semcod/search) index it without parsing the
full analysis or importing analyzer internals — the reuse contract is
this artifact, not the Python API (PLF-035 / issue #25).

Contract invariants:
  - ``schema`` pins the record shape; ``producer.version`` pins the
    analyzer. Bumping either invalidates downstream caches by equality
    of the embedded digests alone.
  - Byte-deterministic for identical analysis results: canonical JSON
    (sorted keys), records sorted by (file, line, kind, symbol), no
    timestamps inside records. ``generated_at`` is optional and never
    contributes to the digest.
  - Bounded: at most ``MAX_RECORDS`` records; symbol and file strings
    truncated at ``FIELD_LIMIT`` characters; ``stats.truncated`` flags
    an overflow so consumers can refuse silently-stale catalogs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from code2llm import __version__

from .base import BaseExporter, export_format

PROJECTION_SCHEMA = "code2llm.projection/v1"
PROJECTION_FILENAME = "projections.json"
MAX_RECORDS = 2048
FIELD_LIMIT = 200

_KIND_ORDER = {"module": 0, "class": 1, "function": 2}


def _canonical(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _digest(obj: Any) -> str:
    return "sha256:" + hashlib.sha256(_canonical(obj).encode("utf-8")).hexdigest()


def _bounded(value: str) -> str:
    return value[:FIELD_LIMIT]


def _record(kind: str, symbol: str, file: str, line: Optional[int]) -> Dict[str, Any]:
    record: Dict[str, Any] = {"kind": kind, "symbol": _bounded(symbol), "file": _bounded(file)}
    if line is not None:
        record["line"] = int(line)
    record["digest"] = _digest(record)
    return record


def _items(value: Any) -> Iterable[Any]:
    """Yield info objects from either a Dict[str, Info] or a list."""
    if isinstance(value, dict):
        return value.values()
    return value or []


def _iter_records(result: Any) -> Iterable[Dict[str, Any]]:
    modules = _items(getattr(result, "modules", None))
    classes = _items(getattr(result, "classes", None))
    functions = _items(getattr(result, "functions", None))
    for module in modules:
        yield _record("module", module.name, module.file, None)
    for cls in classes:
        yield _record("class", cls.qualified_name or cls.name, cls.file, cls.line)
    for func in functions:
        yield _record("function", func.qualified_name or func.name, func.file, func.line)


def build_projection(
    result: Any,
    *,
    max_records: int = MAX_RECORDS,
    generated_at: Optional[str] = None,
) -> Dict[str, Any]:
    """Build the projection document from an :class:`AnalysisResult`.

    Duck-typed on purpose: only ``modules``/``classes``/``functions``
    (``name``/``qualified_name``/``file``/``line``) are read, so tests and
    alternative frontends can feed lightweight structures.
    """
    records: List[Dict[str, Any]] = list(_iter_records(result))
    records.sort(key=lambda r: (r["file"], r.get("line", 0), _KIND_ORDER[r["kind"]], r["symbol"]))
    truncated = len(records) > max_records
    if truncated:
        records = records[:max_records]

    stats = getattr(result, "stats", None) or {}
    document: Dict[str, Any] = {
        "schema": PROJECTION_SCHEMA,
        "producer": {"tool": "code2llm", "version": __version__},
        "project": {
            "path": _bounded(str(getattr(result, "project_path", "") or "")),
            "analysis_mode": str(getattr(result, "analysis_mode", "") or ""),
        },
        "stats": {
            "files": int(stats.get("files", 0) or 0),
            "lines": int(stats.get("lines", 0) or 0),
            "symbols": len(records),
            "truncated": truncated,
        },
        "records": records,
        "digest": _digest(records),
    }
    if generated_at:
        document["generated_at"] = generated_at
    return document


@export_format(
    "projections",
    description="Bounded symbol projections for intent retrieval (projections.json)",
    extension=".json",
)
class ProjectionsExporter(BaseExporter):
    """Export the deterministic projections catalog."""

    def export(
        self,
        result: Any,
        output_path: str,
        generated_at: Optional[str] = None,
        **kwargs: Any,
    ) -> Optional[Path]:
        document = build_projection(result, generated_at=generated_at)
        path = self._ensure_dir(output_path)
        payload = json.dumps(document, sort_keys=True, ensure_ascii=False, indent=1) + "\n"
        self._write_text(path, payload)
        return path
