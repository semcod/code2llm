"""Ruby analyzer (regex-based)."""

import re
from typing import Dict

from code2llm.core.lang.base import extract_calls_regex, _extract_declarations


_RUBY_BLOCK_OPEN = re.compile(r"^\s*(def|if|unless|while|until|for|case|begin|class|module)\b")


def _is_ruby_end(line: str) -> bool:
    """Return True if a line is a bare Ruby `end` keyword."""
    return line.startswith("end") and (len(line) == 3 or line.startswith("end "))


def _extract_ruby_body(content: str, start_line: int) -> str:
    """Extract Ruby function body from def to corresponding end."""
    lines = content.split("\n")
    if start_line < 1 or start_line > len(lines):
        return ""
    def_line_idx = start_line - 1
    while def_line_idx < len(lines):
        if re.match(r"^\s*def\s+", lines[def_line_idx]):
            break
        def_line_idx += 1
    if def_line_idx >= len(lines):
        return ""
    body_lines = []
    nested_depth = 1
    i = def_line_idx + 1
    while i < len(lines) and nested_depth > 0:
        line = lines[i]
        if _is_ruby_end(line):
            nested_depth -= 1
            if nested_depth == 0:
                break
        elif _RUBY_BLOCK_OPEN.match(line):
            nested_depth += 1
        body_lines.append(line)
        i += 1
    return "\n".join(body_lines)


_RUBY_CC_PATTERN = re.compile(
    r"\b(?:if|unless|while|until|for|case|when)\b|&&|\|\||\?\s*[^:]*\s*:"
)


def _adjust_ruby_module_qualnames(
    result: Dict, module_name: str, current_module
) -> None:
    """Re-qualify class and function names when they live inside a Ruby module."""
    if not current_module:
        return
    mod_prefix = f".{current_module}"
    old_prefix = f"{module_name}."
    new_prefix = f"{module_name}{mod_prefix}."

    new_classes = {}
    for qname, cls in list(result["classes"].items()):
        new_qname = qname.replace(old_prefix, new_prefix, 1)
        cls.qualified_name = new_qname
        new_classes[new_qname] = cls
    result["classes"] = new_classes
    result["module"].classes = list(new_classes.keys())

    new_functions = {}
    for qname, func in list(result["functions"].items()):
        new_qname = qname.replace(old_prefix, new_prefix, 1)
        func.qualified_name = new_qname
        new_functions[new_qname] = func
    result["functions"] = new_functions
    result["module"].functions = list(new_functions.keys())


_RUBY_MODULE_RE = re.compile(r"^\s*module\s+(\w+)")
_RUBY_CONTROL_RE = re.compile(r"\b(def|class|module|if|unless|while|until|for|begin|case)\b")
_CC_RANK = [(5, "A"), (10, "B"), (20, "C")]


def _track_ruby_module(lines) -> str | None:
    """Scan lines to find the active Ruby module name at the end of the file."""
    current_module = None
    module_depth = 0
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        mod_match = _RUBY_MODULE_RE.match(stripped)
        if mod_match:
            current_module = mod_match.group(1)
            module_depth = len(_RUBY_CONTROL_RE.findall(stripped))
            continue
        if stripped.startswith("end") and current_module and module_depth > 0:
            module_depth -= 1
            if module_depth == 0:
                current_module = None
    return current_module


def _compute_ruby_cc(content: str, func_info) -> None:
    """Compute and assign cyclomatic complexity for a Ruby function in-place."""
    body = _extract_ruby_body(content, func_info.line)
    cc = 1 + len(_RUBY_CC_PATTERN.findall(body)) if body else 1
    rank = next((r for threshold, r in _CC_RANK if cc <= threshold), "D")
    func_info.complexity = {"cyclomatic_complexity": cc, "cc_rank": rank}


def analyze_ruby(
    content: str, file_path: str, module_name: str, ext: str, stats: Dict
) -> Dict:
    """Analyze Ruby files using shared extraction."""
    patterns = {
        "import": re.compile(r'^\s*require\s*["\']([^"\']+)["\']'),
        "class": re.compile(r"^\s*class\s+(\w+)(?:\s*<\s*(\w+))?"),
        "function": re.compile(r"^\s*def\s+(?:self\.)?([\w]+[?!]?)"),
    }
    lang_config = {
        "index_files": (),
        "brace_track": False,
        "reserved": {"if", "unless", "while", "until", "for", "class", "module"},
    }
    result = _extract_declarations(content, file_path, module_name, patterns, stats, lang_config)
    current_module = _track_ruby_module(content.split("\n"))
    _adjust_ruby_module_qualnames(result, module_name, current_module)
    for func_info in result["functions"].values():
        _compute_ruby_cc(content, func_info)
    extract_calls_regex(content, module_name, result)
    stats["files_processed"] += 1
    return result


# New LanguageParser ABC implementation (demonstrating the new pattern)
# Note: Imports at the bottom to avoid circular imports
# The __init__.py handles the actual registration
class RubyParser:
    """Ruby language parser - registered via @register_language in __init__.py."""

    supported_extensions = (".rb", ".rbw")
    language_name = "Ruby"

    def analyze(
        self, content: str, file_path: str, module_name: str, stats: Dict
    ) -> Dict:
        """Analyze Ruby file content."""
        # Delegate to the existing legacy function for now
        return analyze_ruby(content, file_path, module_name, ".rb", stats)
