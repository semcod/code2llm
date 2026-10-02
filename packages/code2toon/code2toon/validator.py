"""Validation logic for TOON documents."""
from typing import Dict, Any, List, Tuple


class ToonValidator:
    """Validates structure and completeness of TOON data."""

    REQUIRED_METRICS = ["critical", "duplicates", "cycles"]

    def validate(self, toon_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate TOON dictionary structure.
        
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []

        if not isinstance(toon_data, dict):
            return False, ["TOON data must be a dictionary"]

        # Check meta/project
        meta = toon_data.get("meta", {})
        if not meta.get("project") and not toon_data.get("project"):
            errors.append("Missing project name in TOON header/metadata")

        # Validate sections if present
        for section in ("functions", "classes", "health", "hotspots"):
            val = toon_data.get(section)
            if val is not None and not isinstance(val, list):
                errors.append(f"Section '{section}' must be a list")

        return len(errors) == 0, errors


def validate_toon(toon_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Convenience function to validate TOON dictionary."""
    return ToonValidator().validate(toon_data)
