"""C-family declaration parser helpers (classes, functions, methods, decorators)."""

# Brace tracking, decorator detection, class/function extraction for C/Java/Go/Rust/TS/C++.

from typing import Dict


def _update_brace_tracking(
    raw_line, brace_depth, current_class, class_brace_depth, track_braces
):
    """Update brace depth and track current class scope."""
    if track_braces:
        for ch in raw_line:
            if ch == "{":
                brace_depth += 1
            elif ch == "}":
                brace_depth -= 1
        if current_class and brace_depth < class_brace_depth:
            current_class = None
            class_brace_depth = 0
    return brace_depth, current_class, class_brace_depth


def _process_decorators(decorator_re, line, pending_decorators):
    """Process decorator patterns and update pending list."""
    if decorator_re:
        dm = decorator_re.match(line)
        if dm:
            pending_decorators.append(dm.group(1))
            return pending_decorators
    return pending_decorators


def _process_classes(
    class_re,
    interface_re,
    line,
    line_no,
    file_path,
    module_name,
    result,
    stats,
    current_class,
    class_brace_depth,
    pending_decorators,
):
    """Process class and interface declarations."""
    from ..models import ClassInfo

    if class_re:
        cm = class_re.match(line)
        if cm:
            cname = cm.group(1)
            bases = []
            if len(cm.groups()) > 1 and cm.group(2):
                bases.append(cm.group(2).strip())
            if len(cm.groups()) > 2 and cm.group(3):
                bases.extend([b.strip() for b in cm.group(3).split(",")])
            qual = f"{module_name}.{cname}"
            result["classes"][qual] = ClassInfo(
                name=cname,
                qualified_name=qual,
                file=file_path,
                line=line_no,
                module=module_name,
                bases=bases,
                methods=[],
                docstring="",
            )
            result["module"].classes.append(qual)
            stats["classes_found"] += 1
            current_class = qual
            pending_decorators.clear()
            return current_class, class_brace_depth, pending_decorators

    if interface_re:
        imt = interface_re.match(line)
        if imt:
            cname = imt.group(1)
            qual = f"{module_name}.{cname}"
            result["classes"][qual] = ClassInfo(
                name=cname,
                qualified_name=qual,
                file=file_path,
                line=line_no,
                module=module_name,
                bases=[],
                methods=[],
                docstring="",
            )
            result["module"].classes.append(qual)
            stats["classes_found"] += 1
            pending_decorators.clear()

    return current_class, class_brace_depth, pending_decorators


def _process_standalone_function(
    func_re,
    arrow_re,
    line,
    line_no,
    file_path,
    module_name,
    result,
    stats,
    pending_decorators,
    reserved,
):
    """Register a top-level (non-method) function declaration.

    Returns (registered: bool, pending_decorators).
    """
    from ..models import FunctionInfo

    fname = None
    if func_re:
        fm = func_re.match(line)
        if fm:
            fname = fm.group(1) or (fm.group(2) if len(fm.groups()) > 1 else None)
    if not fname and arrow_re:
        am = arrow_re.match(line)
        if am:
            fname = am.group(1)

    if fname and fname not in reserved:
        qual = f"{module_name}.{fname}"
        result["functions"][qual] = FunctionInfo(
            name=fname,
            qualified_name=qual,
            file=file_path,
            line=line_no,
            column=0,
            module=module_name,
            class_name=None,
            is_method=False,
            is_private=fname.startswith("_"),
            is_property=False,
            docstring="",
            args=[],
            decorators=pending_decorators[:],
        )
        result["module"].functions.append(qual)
        stats["functions_found"] += 1
        pending_decorators.clear()
        return True, pending_decorators

    return False, pending_decorators


def _try_match_named_pattern(regex, line: str, reserved: set, extra_exclude: set = frozenset()) -> str | None:
    """Match regex against line and return name if valid, else None."""
    if not regex:
        return None
    m = regex.match(line)
    if not m:
        return None
    groups = m.groups()
    name = groups[0] or (groups[1] if len(groups) > 1 else None)
    if name and name not in reserved and name not in extra_exclude:
        return name
    return None


def _match_method_name(arrow_prop_re, method_re, func_re, line, reserved):
    """Return matched method name from any of the three patterns, or None."""
    name = _try_match_named_pattern(arrow_prop_re, line, reserved, {"constructor"})
    if name:
        return name
    for regex in (method_re, func_re):
        name = _try_match_named_pattern(regex, line, reserved)
        if name:
            return name
    return None


def _process_class_method(
    method_re,
    arrow_prop_re,
    func_re,
    line,
    line_no,
    file_path,
    module_name,
    result,
    stats,
    current_class,
    pending_decorators,
    reserved,
):
    """Register a method declaration inside a class scope."""
    from ..models import FunctionInfo

    mname = _match_method_name(arrow_prop_re, method_re, func_re, line, reserved)
    if not mname:
        return pending_decorators

    qual = f"{current_class}.{mname}"
    result["classes"][current_class].methods.append(qual)
    result["functions"][qual] = FunctionInfo(
        name=mname,
        qualified_name=qual,
        file=file_path,
        line=line_no,
        column=0,
        module=module_name,
        class_name=current_class.split(".")[-1],
        is_method=True,
        is_private=mname.startswith(("_", "#")),
        is_property=False,
        docstring="",
        args=[],
        decorators=pending_decorators[:],
    )
    result["module"].functions.append(qual)
    stats["functions_found"] += 1
    pending_decorators.clear()
    return pending_decorators


def _process_functions(
    func_re,
    arrow_re,
    method_re,
    arrow_prop_re,
    line,
    line_no,
    file_path,
    module_name,
    result,
    stats,
    current_class,
    pending_decorators,
    reserved,
):
    """Process function and method declarations."""
    if not current_class and (func_re or arrow_re):
        registered, pending_decorators = _process_standalone_function(
            func_re,
            arrow_re,
            line,
            line_no,
            file_path,
            module_name,
            result,
            stats,
            pending_decorators,
            reserved,
        )
        if registered:
            return pending_decorators

    if current_class and (method_re or arrow_prop_re or func_re):
        pending_decorators = _process_class_method(
            method_re,
            arrow_prop_re,
            func_re,
            line,
            line_no,
            file_path,
            module_name,
            result,
            stats,
            current_class,
            pending_decorators,
            reserved,
        )

    return pending_decorators


def _clear_orphaned_decorators(
    line, pending_decorators, func_re, arrow_re, class_re, interface_re, method_re
):
    """Clear decorators that don't precede any declaration."""
    if pending_decorators:
        all_patterns = [
            p for p in [func_re, arrow_re, class_re, interface_re, method_re] if p
        ]
        if not any(p and p.match(line) for p in all_patterns):
            pending_decorators.clear()
    return pending_decorators


def _extract_declarations(
    content: str,
    file_path: str,
    module_name: str,
    patterns: Dict,
    stats: Dict,
    lang_config: Dict,
) -> Dict:
    """Shared extraction logic for language parsers."""
    from pathlib import Path

    from ..models import ModuleInfo

    result = {
        "module": ModuleInfo(
            name=module_name,
            file=file_path,
            is_package=Path(file_path).name in lang_config.get("index_files", []),
        ),
        "functions": {},
        "classes": {},
        "nodes": {},
        "edges": [],
    }

    lines = content.split("\n")
    current_class = None
    class_brace_depth = 0
    brace_depth = 0
    pending_decorators = []

    import_re = patterns.get("import")
    decorator_re = patterns.get("decorator")
    class_re = patterns.get("class")
    interface_re = patterns.get("interface")
    func_re = patterns.get("function")
    arrow_re = patterns.get("arrow_func")
    method_re = patterns.get("method")
    arrow_prop_re = patterns.get("arrow_prop")

    track_braces = lang_config.get("brace_track", True)
    reserved = lang_config.get(
        "reserved", {"if", "for", "while", "switch", "return", "catch"}
    )

    for line_no, line in enumerate(lines, 1):
        raw_line = line
        line = line.strip()
        if not line:
            continue
        if line.startswith(("//", "/*", "*")):
            continue
        if (
            line.startswith("#")
            and not line.startswith("#include")
            and not line.startswith("#define")
        ):
            continue

        brace_depth, current_class, class_brace_depth = _update_brace_tracking(
            raw_line, brace_depth, current_class, class_brace_depth, track_braces
        )

        pending_decorators = _process_decorators(decorator_re, line, pending_decorators)

        if import_re:
            im = import_re.match(line)
            if im:
                result["module"].imports.append(im.group(1))
                continue

        current_class, class_brace_depth, pending_decorators = _process_classes(
            class_re,
            interface_re,
            line,
            line_no,
            file_path,
            module_name,
            result,
            stats,
            current_class,
            class_brace_depth,
            pending_decorators,
        )

        pending_decorators = _process_functions(
            func_re,
            arrow_re,
            method_re,
            arrow_prop_re,
            line,
            line_no,
            file_path,
            module_name,
            result,
            stats,
            current_class,
            pending_decorators,
            reserved,
        )

        pending_decorators = _clear_orphaned_decorators(
            line,
            pending_decorators,
            func_re,
            arrow_re,
            class_re,
            interface_re,
            method_re,
        )

    return result
