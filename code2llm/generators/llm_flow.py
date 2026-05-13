"""LLM Flow generator — backward compatibility shim.

This module re-exports from the llm_flow package.
Implementation has been split into:
  - llm_flow/utils.py - YAML reading and helpers
  - llm_flow/parsing.py - Label parsing
  - llm_flow/nodes.py - Node collection and entrypoints
  - llm_flow/analysis.py - Function scoring and call graph
  - llm_flow/generator.py - Flow generation and rendering
  - llm_flow/cli.py - Command-line interface
"""

# Re-export all public names from the new package
from .llm_flow import (
    # Utils
    _FUNC_LABEL_PREFIX,
    _CALL_LABEL_PREFIX,
    _strip_bom,
    _safe_read_yaml,
    _as_dict,
    _as_list,
    _shorten,
    # Parsing
    _parse_call_label,
    _parse_func_label,
    # Nodes
    _collect_nodes,
    _group_nodes_by_file,
    _is_entrypoint_file,
    _extract_entrypoint_info,
    _deduplicate_entrypoints,
    _collect_entrypoints,
    _collect_functions,
    # Analysis
    FuncSummary,
    _node_counts_by_function,
    _pick_relevant_functions,
    _summarize_functions,
    _build_call_graph,
    _reachable,
    # Generator
    generate_llm_flow,
    render_llm_flow_md,
    # CLI
    create_parser,
    main,
)

__all__ = [
    # Utils
    "_FUNC_LABEL_PREFIX",
    "_CALL_LABEL_PREFIX",
    "_strip_bom",
    "_safe_read_yaml",
    "_as_dict",
    "_as_list",
    "_shorten",
    # Parsing
    "_parse_call_label",
    "_parse_func_label",
    # Nodes
    "_collect_nodes",
    "_group_nodes_by_file",
    "_is_entrypoint_file",
    "_extract_entrypoint_info",
    "_deduplicate_entrypoints",
    "_collect_entrypoints",
    "_collect_functions",
    # Analysis
    "FuncSummary",
    "_node_counts_by_function",
    "_pick_relevant_functions",
    "_summarize_functions",
    "_build_call_graph",
    "_reachable",
    # Generator
    "generate_llm_flow",
    "render_llm_flow_md",
    # CLI
    "create_parser",
    "main",
]


if __name__ == "__main__":
    from .llm_flow import main

    raise SystemExit(main())
