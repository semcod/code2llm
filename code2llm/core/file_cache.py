"""File cache for parsed AST files."""

import hashlib
import os
import pickle
import time
from pathlib import Path
from typing import Any, Optional, Tuple
import ast

from code2llm import __version__


def make_cache_key(file_path: str, content: str) -> str:
    """Bind cached AST/module identities to their source path and analyzer."""
    payload = os.path.abspath(file_path).encode() + b"\0" + content.encode()
    content_hash = hashlib.md5(payload).hexdigest()[:16]
    return f"{__version__}_{Path(file_path).stem}_{content_hash}"


class FileCache:
    """Cache for parsed AST files."""

    def __init__(self, cache_dir: str = ".code2llm_cache", ttl_hours: int = 24,
                 analysis_identity: str = ""):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = ttl_hours * 3600
        self._analyzer_version = __version__
        self._analysis_identity = analysis_identity

    def _get_cache_key_stat(self, file_path: str) -> str:
        """Verify content even when a rewrite preserves mtime and size.

        The method name is retained for private-call compatibility. Metadata
        alone is never a basis for returning an old analysis payload.
        """
        identity = hashlib.sha256(os.path.abspath(file_path).encode()).hexdigest()[:16]
        try:
            content = hashlib.sha256(Path(file_path).read_bytes()).hexdigest()
            return f"{self._analyzer_version}_{self._analysis_identity}_{identity}_content1_{content}"
        except OSError:
            return f"{self._analyzer_version}_{identity}_unknown"

    def _get_cache_key(self, file_path: str, content: str) -> str:
        """Return a content-addressed cache key for the given file path and content."""
        return make_cache_key(file_path, content)

    def _get_cache_path(self, cache_key: str) -> Path:
        """Get cache file path."""
        return self.cache_dir / f"{cache_key}.pkl"

    def get(self, file_path: str, _content: str) -> Optional[Tuple[ast.AST, str]]:
        """Get cached AST if available and not expired; _content accepted for API compat."""
        cache_key = self._get_cache_key_stat(file_path)
        cache_path = self._get_cache_path(cache_key)

        if not cache_path.exists():
            return None

        # Check TTL
        age = time.time() - cache_path.stat().st_mtime
        if age > self.ttl_seconds:
            cache_path.unlink()
            return None

        try:
            with open(cache_path, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

    def put(self, file_path: str, _content: str, data: Tuple[ast.AST, str]) -> None:
        """Store AST in cache; _content accepted for API compatibility."""
        cache_key = self._get_cache_key_stat(file_path)
        cache_path = self._get_cache_path(cache_key)

        try:
            with open(cache_path, "wb") as f:
                pickle.dump(data, f)
        except Exception:
            pass

    def get_fast(self, file_path: str) -> Optional[Any]:
        """Get a cached analysis after verifying current source bytes."""
        cache_key = self._get_cache_key_stat(file_path)
        cache_path = self._get_cache_path(cache_key)

        if not cache_path.exists():
            return None

        age = time.time() - cache_path.stat().st_mtime
        if age > self.ttl_seconds:
            try:
                cache_path.unlink()
            except OSError:
                pass
            return None

        try:
            with open(cache_path, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

    def put_fast(self, file_path: str, data: Any) -> None:
        """Store full analysis result using mtime+size key."""
        cache_key = self._get_cache_key_stat(file_path)
        cache_path = self._get_cache_path(cache_key)
        try:
            with open(cache_path, "wb") as f:
                pickle.dump(data, f)
        except Exception:
            pass

    def clear(self) -> None:
        """Clear all cached files."""
        for f in self.cache_dir.glob("*.pkl"):
            f.unlink()
