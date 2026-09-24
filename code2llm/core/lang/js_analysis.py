"""JavaScript/TypeScript declarations and metrics bounded by syntax nodes."""

from importlib import import_module
from pathlib import Path

from code2llm.core.config import CC_HIGH_THRESHOLD, CC_LOW_THRESHOLD, CC_MEDIUM_THRESHOLD
from code2llm.core.lang._calls import _resolve_call
from code2llm.core.models import ClassInfo, FunctionInfo, ModuleInfo

FUNCTIONS = frozenset(
    {
        "function_declaration",
        "function_expression",
        "generator_function_declaration",
        "generator_function",
        "arrow_function",
        "method_definition",
    }
)
CLASSES = frozenset(
    {"class_declaration", "class", "abstract_class_declaration", "interface_declaration"}
)
DECISIONS = frozenset(
    {
        "if_statement",
        "for_statement",
        "for_in_statement",
        "while_statement",
        "do_statement",
        "catch_clause",
        "switch_case",
        "ternary_expression",
        "optional_chain",
    }
)


def _parse(content, ext):
    # Grammars are required package dependencies. An unavailable grammar must
    # not silently replace syntax metrics with unrelated adjacent source text.
    from tree_sitter import Language, Parser

    if ext in {".ts", ".tsx"}:
        grammar = import_module("tree_sitter_typescript")
        raw = getattr(grammar, "language_tsx" if ext == ".tsx" else "language_typescript")()
    else:
        raw = import_module("tree_sitter_javascript").language()
    language = raw if isinstance(raw, Language) else Language(raw)
    parser = Parser(language)
    tree = parser.parse(content.encode("utf-8"))
    if tree.root_node.has_error:
        raise ValueError("Cannot measure invalid JavaScript/TypeScript syntax")
    return tree


def _text(node):
    return node.text.decode("utf-8") if node is not None else ""


def _name(node):
    name = node.child_by_field_name("name")
    if name is not None and node.type not in {"function_expression", "generator_function", "class"}:
        return _text(name)
    bound = node
    while bound.parent is not None and bound.parent.type in {
        "parenthesized_expression",
        "as_expression",
        "satisfies_expression",
        "type_assertion",
    }:
        bound = bound.parent
    parent = bound.parent
    if parent is not None:
        field = {
            "variable_declarator": "name",
            "pair": "key",
            "assignment_expression": "left",
            "public_field_definition": "name",
            "field_definition": "property",
        }.get(parent.type)
        if field and parent.child_by_field_name("value") == bound:
            return _text(parent.child_by_field_name(field))
        if parent.type == "assignment_expression" and parent.child_by_field_name("right") == bound:
            return _text(parent.child_by_field_name("left"))
    return (
        _text(name)
        if name is not None
        else f"<anonymous@{node.start_point[0] + 1}:{node.start_point[1]}>"
    )


def _body_nodes(body):
    """Nested functions/classes have their own metric and call boundaries."""
    pending = [body] if body is not None else []
    while pending:
        node = pending.pop()
        if node.type in FUNCTIONS or node.type in CLASSES:
            continue
        yield node
        pending.extend(reversed(node.children))


def _metrics(nodes):
    decisions = sum(node.type in DECISIONS for node in nodes)
    decisions += sum(
        node.type == "binary_expression"
        and any(child.type in {"&&", "||", "??"} for child in node.children)
        for node in nodes
    )
    cc = 1 + decisions
    rank = (
        "A"
        if cc <= CC_LOW_THRESHOLD
        else "B" if cc <= CC_MEDIUM_THRESHOLD else "C" if cc <= CC_HIGH_THRESHOLD else "D"
    )
    return {"cyclomatic_complexity": cc, "cc_rank": rank}


def analyze_js_tree(content, file_path, module_name, ext, stats):
    tree = _parse(content, ext)
    module = ModuleInfo(
        name=module_name,
        file=file_path,
        is_package=Path(file_path).stem == "index",
        line_count=len(content.splitlines()),
    )
    result = {"module": module, "functions": {}, "classes": {}, "nodes": {}, "edges": []}
    bodies = {}

    def visit(node, scope, class_name=None, class_key=None):
        child_scope = scope
        if node.type in CLASSES:
            class_name = _name(node)
            class_key = child_scope = f"{scope}.{class_name}"
            result["classes"][class_key] = ClassInfo(
                name=class_name,
                qualified_name=class_key,
                file=file_path,
                line=node.start_point[0] + 1,
                module=module_name,
            )
            module.classes.append(class_key)
        elif node.type in FUNCTIONS:
            name = _name(node)
            key = f"{scope}.{name}"
            if key in result["functions"]:
                key += f"@{node.start_point[0] + 1}:{node.start_point[1]}"
            is_method = node.type == "method_definition" or (
                class_key is not None
                and node.parent is not None
                and node.parent.type in {"public_field_definition", "field_definition"}
            )
            function = FunctionInfo(
                name=name,
                qualified_name=key,
                file=file_path,
                line=node.start_point[0] + 1,
                column=node.start_point[1],
                module=module_name,
                class_name=class_name if is_method else None,
                is_method=is_method,
                is_private=name.startswith(("_", "#")),
            )
            bodies[key] = [
                inner
                for field in ("parameters", "parameter", "body")
                for inner in _body_nodes(node.child_by_field_name(field))
            ]
            function.complexity = _metrics(bodies[key])
            result["functions"][key] = function
            module.functions.append(key)
            if is_method and class_key:
                result["classes"][class_key].methods.append(key)
            child_scope = key
        elif node.type == "import_statement":
            source = node.child_by_field_name("source")
            if source is not None:
                module.imports.append(_text(source)[1:-1])
        for child in node.named_children:
            visit(child, child_scope, class_name, class_key)

    visit(tree.root_node, module_name)
    known = {}
    for key, function in result["functions"].items():
        known.setdefault(function.name, []).append(key)
    for key, nodes in bodies.items():
        seen = set()
        for node in nodes:
            if node.type != "call_expression":
                continue
            callee = node.child_by_field_name("function")
            if callee is not None and callee.type == "member_expression":
                callee = callee.child_by_field_name("property")
            if callee is not None and callee.type in {"identifier", "property_identifier"}:
                _resolve_call(
                    _text(callee), key, module_name, known, seen, result["functions"][key]
                )
    stats["functions_found"] += len(result["functions"])
    stats["classes_found"] += len(result["classes"])
    stats["files_processed"] += 1
    return result
