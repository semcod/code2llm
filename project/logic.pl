% ── Project Metadata ─────────────────────────────────────
project_metadata('code2llm', '0.5.160', 'python').

% ── Project Files ────────────────────────────────────────
project_file('app.doql.less', 60, 'less').
project_file('badges/server.py', 133, 'python').
project_file('benchmarks/benchmark_constants.py', 30, 'python').
project_file('benchmarks/benchmark_evolution.py', 145, 'python').
project_file('benchmarks/benchmark_format_quality.py', 156, 'python').
project_file('benchmarks/benchmark_optimizations.py', 159, 'python').
project_file('benchmarks/benchmark_performance.py', 318, 'python').
project_file('benchmarks/format_evaluator.py', 174, 'python').
project_file('benchmarks/project_generator.py', 236, 'python').
project_file('benchmarks/reporting.py', 192, 'python').
project_file('benchmarks/test_performance.py', 269, 'python').
project_file('code2llm/__init__.py', 60, 'python').
project_file('code2llm/__main__.py', 7, 'python').
project_file('code2llm/analysis/__init__.py', 39, 'python').
project_file('code2llm/analysis/_data_impl.py', 393, 'python').
project_file('code2llm/analysis/call_graph.py', 208, 'python').
project_file('code2llm/analysis/cfg.py', 287, 'python').
project_file('code2llm/analysis/coupling.py', 80, 'python').
project_file('code2llm/analysis/data_analysis.py', 178, 'python').
project_file('code2llm/analysis/dfg.py', 242, 'python').
project_file('code2llm/analysis/pipeline_classifier.py', 133, 'python').
project_file('code2llm/analysis/pipeline_detector.py', 356, 'python').
project_file('code2llm/analysis/pipeline_resolver.py', 93, 'python').
project_file('code2llm/analysis/side_effects.py', 366, 'python').
project_file('code2llm/analysis/smells.py', 226, 'python').
project_file('code2llm/analysis/type_inference.py', 299, 'python').
project_file('code2llm/analysis/utils/__init__.py', 18, 'python').
project_file('code2llm/analysis/utils/ast_helpers.py', 88, 'python').
project_file('code2llm/api.py', 74, 'python').
project_file('code2llm/cli.py', 66, 'python').
project_file('code2llm/cli_analysis.py', 360, 'python').
project_file('code2llm/cli_commands.py', 336, 'python').
project_file('code2llm/cli_exports/__init__.py', 55, 'python').
project_file('code2llm/cli_exports/code2logic.py', 143, 'python').
project_file('code2llm/cli_exports/formats.py', 360, 'python').
project_file('code2llm/cli_exports/orchestrator.py', 405, 'python').
project_file('code2llm/cli_exports/orchestrator_chunked.py', 95, 'python').
project_file('code2llm/cli_exports/orchestrator_constants.py', 56, 'python').
project_file('code2llm/cli_exports/orchestrator_handlers.py', 185, 'python').
project_file('code2llm/cli_exports/prompt.py', 591, 'python').
project_file('code2llm/cli_parser.py', 355, 'python').
project_file('code2llm/core/__init__.py', 69, 'python').
project_file('code2llm/core/analyzer.py', 578, 'python').
project_file('code2llm/core/ast_registry.py', 103, 'python').
project_file('code2llm/core/config.py', 399, 'python').
project_file('code2llm/core/export_pipeline.py', 159, 'python').
project_file('code2llm/core/file_analyzer.py', 533, 'python').
project_file('code2llm/core/file_cache.py', 108, 'python').
project_file('code2llm/core/file_filter.py', 188, 'python').
project_file('code2llm/core/gitignore.py', 148, 'python').
project_file('code2llm/core/incremental.py', 151, 'python').
project_file('code2llm/core/lang/__init__.py', 171, 'python').
project_file('code2llm/core/lang/_c_parser.py', 397, 'python').
project_file('code2llm/core/lang/_calls.py', 97, 'python').
project_file('code2llm/core/lang/_complexity.py', 74, 'python').
project_file('code2llm/core/lang/base.py', 77, 'python').
project_file('code2llm/core/lang/cpp.py', 42, 'python').
project_file('code2llm/core/lang/csharp.py', 58, 'python').
project_file('code2llm/core/lang/generic.py', 72, 'python').
project_file('code2llm/core/lang/go_lang.py', 127, 'python').
project_file('code2llm/core/lang/java.py', 59, 'python').
project_file('code2llm/core/lang/php.py', 123, 'python').
project_file('code2llm/core/lang/ruby.py', 154, 'python').
project_file('code2llm/core/lang/rust.py', 117, 'python').
project_file('code2llm/core/lang/ts_extractors.py', 212, 'python').
project_file('code2llm/core/lang/ts_parser.py', 164, 'python').
project_file('code2llm/core/lang/typescript.py', 72, 'python').
project_file('code2llm/core/large_repo.py', 545, 'python').
project_file('code2llm/core/models.py', 208, 'python').
project_file('code2llm/core/persistent_cache.py', 459, 'python').
project_file('code2llm/core/refactoring.py', 234, 'python').
project_file('code2llm/core/repo_files.py', 216, 'python').
project_file('code2llm/core/source_classifier.py', 251, 'python').
project_file('code2llm/core/streaming/__init__.py', 8, 'python').
project_file('code2llm/core/streaming/cache.py', 53, 'python').
project_file('code2llm/core/streaming/incremental.py', 79, 'python').
project_file('code2llm/core/streaming/prioritizer.py', 134, 'python').
project_file('code2llm/core/streaming/scanner.py', 208, 'python').
project_file('code2llm/core/streaming/strategies.py', 70, 'python').
project_file('code2llm/core/streaming_analyzer.py', 166, 'python').
project_file('code2llm/core/toon_size_manager.py', 279, 'python').
project_file('code2llm/exporters/__init__.py', 87, 'python').
project_file('code2llm/exporters/article_view.py', 177, 'python').
project_file('code2llm/exporters/base.py', 175, 'python').
project_file('code2llm/exporters/context_exporter.py', 343, 'python').
project_file('code2llm/exporters/context_view.py', 154, 'python').
project_file('code2llm/exporters/dashboard_data.py', 209, 'python').
project_file('code2llm/exporters/dashboard_renderer.py', 357, 'python').
project_file('code2llm/exporters/evolution/__init__.py', 79, 'python').
project_file('code2llm/exporters/evolution/computation.py', 212, 'python').
project_file('code2llm/exporters/evolution/constants.py', 42, 'python').
project_file('code2llm/exporters/evolution/exclusion.py', 18, 'python').
project_file('code2llm/exporters/evolution/render.py', 196, 'python').
project_file('code2llm/exporters/evolution/yaml_export.py', 101, 'python').
project_file('code2llm/exporters/evolution_exporter.py', 82, 'python').
project_file('code2llm/exporters/flow_constants.py', 64, 'python').
project_file('code2llm/exporters/flow_exporter.py', 400, 'python').
project_file('code2llm/exporters/flow_renderer.py', 181, 'python').
project_file('code2llm/exporters/html_dashboard.py', 81, 'python').
project_file('code2llm/exporters/index_generator/__init__.py', 74, 'python').
project_file('code2llm/exporters/index_generator/renderer.py', 638, 'python').
project_file('code2llm/exporters/index_generator/scanner.py', 134, 'python').
project_file('code2llm/exporters/index_generator.py', 30, 'python').
project_file('code2llm/exporters/json_exporter.py', 28, 'python').
project_file('code2llm/exporters/llm_exporter.py', 13, 'python').
project_file('code2llm/exporters/map/__init__.py', 61, 'python').
project_file('code2llm/exporters/map/alerts.py', 85, 'python').
project_file('code2llm/exporters/map/details.py', 105, 'python').
project_file('code2llm/exporters/map/header.py', 82, 'python').
project_file('code2llm/exporters/map/module_list.py', 27, 'python').
project_file('code2llm/exporters/map/utils.py', 75, 'python').
project_file('code2llm/exporters/map/yaml_export.py', 119, 'python').
project_file('code2llm/exporters/map_exporter.py', 54, 'python').
project_file('code2llm/exporters/mermaid/__init__.py', 67, 'python').
project_file('code2llm/exporters/mermaid/calls.py', 71, 'python').
project_file('code2llm/exporters/mermaid/classic.py', 107, 'python').
project_file('code2llm/exporters/mermaid/compact.py', 53, 'python').
project_file('code2llm/exporters/mermaid/flow_compact.py', 181, 'python').
project_file('code2llm/exporters/mermaid/flow_detailed.py', 85, 'python').
project_file('code2llm/exporters/mermaid/flow_full.py', 85, 'python').
project_file('code2llm/exporters/mermaid/utils.py', 102, 'python').
project_file('code2llm/exporters/mermaid_exporter.py', 71, 'python').
project_file('code2llm/exporters/mermaid_flow_helpers.py', 296, 'python').
project_file('code2llm/exporters/planfile_tickets.py', 410, 'python').
project_file('code2llm/exporters/project_yaml/__init__.py', 16, 'python').
project_file('code2llm/exporters/project_yaml/constants.py', 16, 'python').
project_file('code2llm/exporters/project_yaml/core.py', 114, 'python').
project_file('code2llm/exporters/project_yaml/evolution.py', 47, 'python').
project_file('code2llm/exporters/project_yaml/health.py', 108, 'python').
project_file('code2llm/exporters/project_yaml/hotspots.py', 113, 'python').
project_file('code2llm/exporters/project_yaml/modules.py', 153, 'python').
project_file('code2llm/exporters/project_yaml_exporter.py', 16, 'python').
project_file('code2llm/exporters/readme/__init__.py', 41, 'python').
project_file('code2llm/exporters/readme/content.py', 349, 'python').
project_file('code2llm/exporters/readme/files.py', 27, 'python').
project_file('code2llm/exporters/readme/insights.py', 59, 'python').
project_file('code2llm/exporters/readme/sections.py', 94, 'python').
project_file('code2llm/exporters/readme_exporter.py', 81, 'python').
project_file('code2llm/exporters/report_generators.py', 88, 'python').
project_file('code2llm/exporters/toon/__init__.py', 242, 'python').
project_file('code2llm/exporters/toon/_render_coupling_helpers.py', 153, 'python').
project_file('code2llm/exporters/toon/_render_section_helpers.py', 192, 'python').
project_file('code2llm/exporters/toon/constants.py', 10, 'python').
project_file('code2llm/exporters/toon/helpers.py', 156, 'python').
project_file('code2llm/exporters/toon/metrics.py', 104, 'python').
project_file('code2llm/exporters/toon/metrics_core.py', 312, 'python').
project_file('code2llm/exporters/toon/metrics_duplicates.py', 98, 'python').
project_file('code2llm/exporters/toon/metrics_health.py', 124, 'python').
project_file('code2llm/exporters/toon/module_detail.py', 174, 'python').
project_file('code2llm/exporters/toon/renderer.py', 162, 'python').
project_file('code2llm/exporters/toon.py', 10, 'python').
project_file('code2llm/exporters/toon_view.py', 194, 'python').
project_file('code2llm/exporters/validate_project.py', 115, 'python').
project_file('code2llm/exporters/yaml_exporter.py', 457, 'python').
project_file('code2llm/generators/__init__.py', 16, 'python').
project_file('code2llm/generators/_utils.py', 16, 'python').
project_file('code2llm/generators/llm_flow/__init__.py', 99, 'python').
project_file('code2llm/generators/llm_flow/analysis.py', 185, 'python').
project_file('code2llm/generators/llm_flow/cli.py', 79, 'python').
project_file('code2llm/generators/llm_flow/generator.py', 122, 'python').
project_file('code2llm/generators/llm_flow/nodes.py', 108, 'python').
project_file('code2llm/generators/llm_flow/parsing.py', 40, 'python').
project_file('code2llm/generators/llm_flow/utils.py', 100, 'python').
project_file('code2llm/generators/llm_flow.py', 89, 'python').
project_file('code2llm/generators/llm_task.py', 384, 'python').
project_file('code2llm/generators/mermaid/__init__.py', 71, 'python').
project_file('code2llm/generators/mermaid/fix.py', 151, 'python').
project_file('code2llm/generators/mermaid/png.py', 330, 'python').
project_file('code2llm/generators/mermaid/validation.py', 138, 'python').
project_file('code2llm/generators/mermaid.py', 88, 'python').
project_file('code2llm/nlp/__init__.py', 24, 'python').
project_file('code2llm/nlp/config.py', 186, 'python').
project_file('code2llm/nlp/entity_resolution.py', 315, 'python').
project_file('code2llm/nlp/intent_matching.py', 324, 'python').
project_file('code2llm/nlp/normalization.py', 124, 'python').
project_file('code2llm/nlp/pipeline.py', 398, 'python').
project_file('code2llm/parsers/toon_parser.py', 148, 'python').
project_file('code2llm/patterns/__init__.py', 1, 'python').
project_file('code2llm/patterns/detector.py', 188, 'python').
project_file('code2llm/refactor/__init__.py', 1, 'python').
project_file('code2llm/refactor/prompt_engine.py', 186, 'python').
project_file('demo_langs/invalid/sample_bad.go', 25, 'go').
project_file('demo_langs/invalid/sample_bad.py', 24, 'python').
project_file('demo_langs/invalid/sample_bad.rs', 19, 'rust').
project_file('demo_langs/invalid/sample_bad.ts', 21, 'typescript').
project_file('demo_langs/valid/sample.go', 47, 'go').
project_file('demo_langs/valid/sample.py', 55, 'python').
project_file('demo_langs/valid/sample.rs', 48, 'rust').
project_file('demo_langs/valid/sample.ts', 27, 'typescript').
project_file('examples/docker-doql-example/app/main.py', 25, 'python').
project_file('examples/docker-doql-example/app.doql.less', 516, 'less').
project_file('examples/docker-doql-example/go/main.go', 57, 'go').
project_file('examples/docker-doql-example/node/index.js', 38, 'javascript').
project_file('examples/docker-doql-example/run-doql.sh', 428, 'shell').
project_file('examples/docker-doql-example/rust/src/main.rs', 48, 'rust').
project_file('examples/docker-doql-example/worker/worker.py', 32, 'python').
project_file('examples/functional_refactoring/__init__.py', 7, 'python').
project_file('examples/functional_refactoring/cache.py', 129, 'python').
project_file('examples/functional_refactoring/cli.py', 45, 'python').
project_file('examples/functional_refactoring/entity_preparers.py', 146, 'python').
project_file('examples/functional_refactoring/generator.py', 59, 'python').
project_file('examples/functional_refactoring/models.py', 29, 'python').
project_file('examples/functional_refactoring/template_engine.py', 109, 'python').
project_file('examples/functional_refactoring_example.py', 64, 'python').
project_file('examples/litellm/run.py', 134, 'python').
project_file('examples/streaming-analyzer/demo.py', 268, 'python').
project_file('examples/streaming-analyzer/sample_project/__init__.py', 2, 'python').
project_file('examples/streaming-analyzer/sample_project/api.py', 73, 'python').
project_file('examples/streaming-analyzer/sample_project/auth.py', 91, 'python').
project_file('examples/streaming-analyzer/sample_project/database.py', 155, 'python').
project_file('examples/streaming-analyzer/sample_project/main.py', 160, 'python').
project_file('examples/streaming-analyzer/sample_project/utils.py', 81, 'python').
project_file('examples/streaming-analyzer/test_example.py', 99, 'python').
project_file('orchestrator.sh', 83, 'shell').
project_file('pipeline.py', 215, 'python').
project_file('project.sh', 53, 'shell').
project_file('project2.sh', 50, 'shell').
project_file('scripts/benchmark_badges.py', 394, 'python').
project_file('scripts/bump_version.py', 103, 'python').
project_file('setup.py', 77, 'python').
project_file('test_langs/invalid/sample_bad.go', 25, 'go').
project_file('test_langs/invalid/sample_bad.py', 24, 'python').
project_file('test_langs/invalid/sample_bad.rs', 19, 'rust').
project_file('test_langs/invalid/sample_bad.ts', 21, 'typescript').
project_file('test_langs/valid/sample.go', 47, 'go').
project_file('test_langs/valid/sample.py', 42, 'python').
project_file('test_langs/valid/sample.rs', 48, 'rust').
project_file('test_langs/valid/sample.ts', 27, 'typescript').
project_file('test_python_only/invalid/__init__.py', 2, 'python').
project_file('test_python_only/invalid/sample_bad.py', 24, 'python').
project_file('test_python_only/valid/__init__.py', 2, 'python').
project_file('test_python_only/valid/sample.py', 42, 'python').
project_file('tests/test_advanced_analysis.py', 116, 'python').
project_file('tests/test_analyzer.py', 259, 'python').
project_file('tests/test_cache_invalidation_e2e.py', 118, 'python').
project_file('tests/test_calls_toon_export.py', 241, 'python').
project_file('tests/test_declarative_collection.py', 284, 'python').
project_file('tests/test_deep_analysis.py', 83, 'python').
project_file('tests/test_edge_cases.py', 412, 'python').
project_file('tests/test_export_cache_flags.py', 28, 'python').
project_file('tests/test_file_analyzer_tagging.py', 70, 'python').
project_file('tests/test_flow_exporter.py', 502, 'python').
project_file('tests/test_format_quality.py', 391, 'python').
project_file('tests/test_multilanguage_e2e.py', 379, 'python').
project_file('tests/test_nlp_pipeline.py', 333, 'python').
project_file('tests/test_nonpython_cc_calls.py', 708, 'python').
project_file('tests/test_orchestrator_cache_mtime.py', 56, 'python').
project_file('tests/test_persistent_cache.py', 401, 'python').
project_file('tests/test_pipeline_detector.py', 515, 'python').
project_file('tests/test_planfile_tickets_exporter.py', 146, 'python').
project_file('tests/test_project_toon_export.py', 85, 'python').
project_file('tests/test_prompt_engine.py', 80, 'python').
project_file('tests/test_prompt_txt.py', 303, 'python').
project_file('tests/test_refactoring_engine.py', 89, 'python').
project_file('tests/test_toon_v2.py', 307, 'python').
project_file('validate_toon.py', 399, 'python').

% ── Python Functions ─────────────────────────────────────
python_function('badges/server.py', 'index', 0, 1, 2).
python_function('badges/server.py', 'generate_badges', 0, 4, 4).
python_function('badges/server.py', 'get_badges', 0, 3, 6).
python_function('benchmarks/benchmark_evolution.py', 'parse_evolution_metrics', 1, 13, 7).
python_function('benchmarks/benchmark_evolution.py', 'load_previous', 1, 3, 3).
python_function('benchmarks/benchmark_evolution.py', 'save_current', 2, 1, 3).
python_function('benchmarks/benchmark_evolution.py', 'run_benchmark', 1, 9, 15).
python_function('benchmarks/benchmark_format_quality.py', '_print_benchmark_header', 0, 1, 1).
python_function('benchmarks/benchmark_format_quality.py', '_print_ground_truth_info', 1, 1, 2).
python_function('benchmarks/benchmark_format_quality.py', '_generate_format_outputs', 2, 4, 13).
python_function('benchmarks/benchmark_format_quality.py', '_create_offline_scores', 0, 2, 1).
python_function('benchmarks/benchmark_format_quality.py', 'run_benchmark', 0, 2, 18).
python_function('benchmarks/benchmark_optimizations.py', 'clear_caches', 1, 3, 6).
python_function('benchmarks/benchmark_optimizations.py', 'run_analysis', 2, 1, 5).
python_function('benchmarks/benchmark_optimizations.py', 'benchmark_cold_vs_warm', 2, 7, 15).
python_function('benchmarks/benchmark_optimizations.py', 'print_summary', 1, 1, 3).
python_function('benchmarks/benchmark_optimizations.py', 'main', 0, 3, 9).
python_function('benchmarks/benchmark_performance.py', 'save_report', 2, 2, 9).
python_function('benchmarks/benchmark_performance.py', 'create_test_project', 1, 5, 8).
python_function('benchmarks/benchmark_performance.py', 'benchmark_original_analyzer', 2, 3, 11).
python_function('benchmarks/benchmark_performance.py', 'benchmark_streaming_analyzer', 2, 5, 10).
python_function('benchmarks/benchmark_performance.py', 'benchmark_with_strategies', 1, 6, 6).
python_function('benchmarks/benchmark_performance.py', 'print_comparison', 2, 2, 1).
python_function('benchmarks/benchmark_performance.py', 'main', 0, 1, 8).
python_function('benchmarks/format_evaluator.py', '_detect_problems', 1, 1, 2).
python_function('benchmarks/format_evaluator.py', '_detect_pipelines', 1, 5, 5).
python_function('benchmarks/format_evaluator.py', '_detect_hub_types', 1, 2, 2).
python_function('benchmarks/format_evaluator.py', '_check_structural_features', 1, 1, 2).
python_function('benchmarks/format_evaluator.py', 'evaluate_format', 3, 4, 13).
python_function('benchmarks/project_generator.py', 'create_core_py', 1, 1, 2).
python_function('benchmarks/project_generator.py', 'create_etl_py', 1, 1, 2).
python_function('benchmarks/project_generator.py', 'create_validation_py', 1, 1, 2).
python_function('benchmarks/project_generator.py', 'create_utils_py', 1, 1, 2).
python_function('benchmarks/project_generator.py', 'add_validator_to_core', 1, 1, 3).
python_function('benchmarks/project_generator.py', 'create_ground_truth_project', 1, 1, 6).
python_function('benchmarks/reporting.py', '_print_header', 0, 1, 1).
python_function('benchmarks/reporting.py', '_print_scores_table', 1, 3, 5).
python_function('benchmarks/reporting.py', '_print_problems_detail', 1, 5, 7).
python_function('benchmarks/reporting.py', '_print_pipelines_detail', 1, 5, 5).
python_function('benchmarks/reporting.py', '_print_structural_features', 1, 5, 5).
python_function('benchmarks/reporting.py', '_print_gap_analysis', 1, 6, 5).
python_function('benchmarks/reporting.py', 'print_results', 1, 1, 6).
python_function('benchmarks/reporting.py', 'build_report', 1, 3, 7).
python_function('benchmarks/reporting.py', 'save_report', 2, 2, 8).
python_function('benchmarks/test_performance.py', 'save_test_report', 2, 1, 9).
python_function('code2llm/__init__.py', '__getattr__', 1, 3, 2).
python_function('code2llm/analysis/__init__.py', '__getattr__', 1, 2, 3).
python_function('code2llm/analysis/_data_impl.py', '_find_data_pipelines', 4, 7, 4).
python_function('code2llm/analysis/_data_impl.py', '_is_state_func', 1, 2, 1).
python_function('code2llm/analysis/_data_impl.py', '_state_affected_by', 2, 5, 4).
python_function('code2llm/analysis/_data_impl.py', '_find_state_patterns', 1, 7, 6).
python_function('code2llm/analysis/_data_impl.py', '_find_data_dependencies', 1, 9, 6).
python_function('code2llm/analysis/_data_impl.py', '_is_event_func', 1, 4, 2).
python_function('code2llm/analysis/_data_impl.py', '_event_handlers', 2, 5, 5).
python_function('code2llm/analysis/_data_impl.py', '_find_event_flows', 1, 7, 6).
python_function('code2llm/analysis/_data_impl.py', '_detect_types_from_name', 2, 5, 3).
python_function('code2llm/analysis/_data_impl.py', '_create_type_entry', 4, 1, 2).
python_function('code2llm/analysis/_data_impl.py', '_update_type_stats', 4, 4, 3).
python_function('code2llm/analysis/_data_impl.py', '_infer_parameter_types', 1, 9, 2).
python_function('code2llm/analysis/_data_impl.py', '_infer_return_types', 1, 5, 3).
python_function('code2llm/analysis/_data_impl.py', '_analyze_data_types', 1, 8, 12).
python_function('code2llm/analysis/_data_impl.py', '_get_function_data_types', 1, 8, 4).
python_function('code2llm/analysis/_data_impl.py', '_build_data_flow_graph', 1, 9, 9).
python_function('code2llm/analysis/_data_impl.py', '_identify_process_patterns', 1, 9, 6).
python_function('code2llm/analysis/_data_impl.py', '_type_consolidations', 1, 7, 7).
python_function('code2llm/analysis/_data_impl.py', '_process_consolidations', 1, 3, 1).
python_function('code2llm/analysis/_data_impl.py', '_hub_optimizations', 1, 5, 2).
python_function('code2llm/analysis/_data_impl.py', '_analyze_optimization_opportunities', 3, 1, 4).
python_function('code2llm/analysis/data_analysis.py', '_categorize_functions', 1, 8, 4).
python_function('code2llm/analysis/data_analysis.py', '_make_stage', 3, 2, 0).
python_function('code2llm/analysis/utils/ast_helpers.py', 'get_ast', 2, 2, 2).
python_function('code2llm/analysis/utils/ast_helpers.py', 'find_function_node', 3, 8, 2).
python_function('code2llm/analysis/utils/ast_helpers.py', 'ast_unparse', 2, 4, 3).
python_function('code2llm/analysis/utils/ast_helpers.py', 'qualified_name', 3, 2, 2).
python_function('code2llm/analysis/utils/ast_helpers.py', 'expr_to_str', 1, 4, 2).
python_function('code2llm/api.py', 'analyze', 2, 2, 2).
python_function('code2llm/api.py', 'analyze_file', 2, 1, 4).
python_function('code2llm/cli.py', 'main', 0, 7, 9).
python_function('code2llm/cli_analysis.py', '_run_analysis', 3, 5, 4).
python_function('code2llm/cli_analysis.py', '_run_standard_analysis', 3, 5, 8).
python_function('code2llm/cli_analysis.py', '_apply_exclude_patterns', 2, 6, 5).
python_function('code2llm/cli_analysis.py', '_apply_strategy_config', 2, 3, 2).
python_function('code2llm/cli_analysis.py', '_build_config', 2, 4, 7).
python_function('code2llm/cli_analysis.py', '_print_analysis_summary', 1, 1, 2).
python_function('code2llm/cli_analysis.py', '_run_chunked_analysis', 3, 3, 8).
python_function('code2llm/cli_analysis.py', '_print_chunked_plan', 1, 4, 5).
python_function('code2llm/cli_analysis.py', '_filter_subprojects', 2, 10, 4).
python_function('code2llm/cli_analysis.py', '_analyze_all_subprojects', 3, 4, 8).
python_function('code2llm/cli_analysis.py', '_build_filter_config', 1, 6, 6).
python_function('code2llm/cli_analysis.py', '_analyze_subproject', 3, 7, 11).
python_function('code2llm/cli_analysis.py', '_merge_item_dict', 4, 4, 2).
python_function('code2llm/cli_analysis.py', '_merge_chunked_results', 2, 3, 6).
python_function('code2llm/cli_analysis.py', '_run_streaming_analysis', 3, 7, 9).
python_function('code2llm/cli_commands.py', 'handle_special_commands', 0, 9, 5).
python_function('code2llm/cli_commands.py', '_handle_cache_status', 2, 5, 7).
python_function('code2llm/cli_commands.py', '_handle_cache_clear', 3, 2, 5).
python_function('code2llm/cli_commands.py', '_handle_cache_gc', 3, 4, 7).
python_function('code2llm/cli_commands.py', 'handle_cache_command', 1, 4, 6).
python_function('code2llm/cli_commands.py', 'handle_report_command', 1, 4, 9).
python_function('code2llm/cli_commands.py', 'validate_and_setup', 1, 3, 6).
python_function('code2llm/cli_commands.py', 'print_start_info', 3, 2, 1).
python_function('code2llm/cli_commands.py', 'validate_chunked_output', 2, 3, 6).
python_function('code2llm/cli_commands.py', '_get_chunk_dirs', 1, 3, 2).
python_function('code2llm/cli_commands.py', '_validate_chunks', 2, 3, 7).
python_function('code2llm/cli_commands.py', '_validate_single_chunk', 2, 4, 3).
python_function('code2llm/cli_commands.py', '_get_file_sizes', 2, 3, 3).
python_function('code2llm/cli_commands.py', '_print_chunk_errors', 2, 2, 1).
python_function('code2llm/cli_commands.py', '_print_validation_summary', 3, 3, 2).
python_function('code2llm/cli_commands.py', 'generate_llm_context', 1, 3, 12).
python_function('code2llm/cli_exports/code2logic.py', '_export_code2logic', 4, 6, 10).
python_function('code2llm/cli_exports/code2logic.py', '_should_run_code2logic', 1, 2, 0).
python_function('code2llm/cli_exports/code2logic.py', '_check_code2logic_installed', 0, 2, 3).
python_function('code2llm/cli_exports/code2logic.py', '_build_code2logic_cmd', 3, 2, 2).
python_function('code2llm/cli_exports/code2logic.py', '_run_code2logic', 2, 3, 3).
python_function('code2llm/cli_exports/code2logic.py', '_handle_code2logic_error', 2, 6, 3).
python_function('code2llm/cli_exports/code2logic.py', '_find_code2logic_output', 2, 6, 4).
python_function('code2llm/cli_exports/code2logic.py', '_normalize_code2logic_output', 3, 2, 4).
python_function('code2llm/cli_exports/formats.py', '_export_evolution', 3, 6, 8).
python_function('code2llm/cli_exports/formats.py', '_export_data_structures', 3, 3, 4).
python_function('code2llm/cli_exports/formats.py', '_export_context_fallback', 4, 4, 6).
python_function('code2llm/cli_exports/formats.py', '_export_readme', 3, 4, 7).
python_function('code2llm/cli_exports/formats.py', '_export_project_yaml', 3, 2, 7).
python_function('code2llm/cli_exports/formats.py', '_export_project_toon', 3, 2, 10).
python_function('code2llm/cli_exports/formats.py', '_run_report', 3, 6, 11).
python_function('code2llm/cli_exports/formats.py', '_export_simple_formats', 4, 8, 10).
python_function('code2llm/cli_exports/formats.py', '_export_yaml', 3, 6, 6).
python_function('code2llm/cli_exports/formats.py', '_export_project_yaml_bundle', 3, 6, 11).
python_function('code2llm/cli_exports/formats.py', '_try_subprocess_png_fallback', 2, 6, 5).
python_function('code2llm/cli_exports/formats.py', '_export_mermaid_pngs', 2, 6, 3).
python_function('code2llm/cli_exports/formats.py', '_export_calls_format', 4, 4, 5).
python_function('code2llm/cli_exports/formats.py', '_export_calls', 3, 1, 1).
python_function('code2llm/cli_exports/formats.py', '_export_calls_toon', 3, 1, 1).
python_function('code2llm/cli_exports/formats.py', '_export_mermaid', 3, 6, 16).
python_function('code2llm/cli_exports/formats.py', '_export_refactor_prompts', 3, 8, 8).
python_function('code2llm/cli_exports/formats.py', '_export_index_html', 2, 5, 3).
python_function('code2llm/cli_exports/orchestrator.py', '_build_export_config', 2, 1, 2).
python_function('code2llm/cli_exports/orchestrator.py', '_collect_dry_run_files', 2, 3, 2).
python_function('code2llm/cli_exports/orchestrator.py', '_show_dry_run_plan', 4, 4, 7).
python_function('code2llm/cli_exports/orchestrator.py', '_should_skip_export_cache', 2, 4, 1).
python_function('code2llm/cli_exports/orchestrator.py', '_try_serve_from_cache', 4, 3, 6).
python_function('code2llm/cli_exports/orchestrator.py', '_save_to_export_cache', 4, 2, 8).
python_function('code2llm/cli_exports/orchestrator.py', '_run_core_exports', 8, 6, 5).
python_function('code2llm/cli_exports/orchestrator.py', '_run_exports', 4, 8, 9).
python_function('code2llm/cli_exports/orchestrator.py', '_copy_cached_export', 3, 8, 8).
python_function('code2llm/cli_exports/orchestrator.py', '_touch_recursive', 1, 5, 3).
python_function('code2llm/cli_exports/orchestrator.py', '_copy_to_cache', 3, 7, 9).
python_function('code2llm/cli_exports/orchestrator.py', '_expand_all_formats', 2, 2, 0).
python_function('code2llm/cli_exports/orchestrator.py', '_export_single', 6, 10, 13).
python_function('code2llm/cli_exports/orchestrator.py', '_export_registry_formats', 4, 9, 12).
python_function('code2llm/cli_exports/orchestrator.py', '_with_planfile_apply_format', 2, 3, 1).
python_function('code2llm/cli_exports/orchestrator.py', '_get_format_kwargs', 2, 3, 1).
python_function('code2llm/cli_exports/orchestrator.py', '_export_chunked', 6, 1, 1).
python_function('code2llm/cli_exports/orchestrator.py', '_insert_after_first_line', 4, 2, 2).
python_function('code2llm/cli_exports/orchestrator.py', '_inject_generation_time', 2, 7, 8).
python_function('code2llm/cli_exports/orchestrator_chunked.py', '_export_chunked', 6, 6, 9).
python_function('code2llm/cli_exports/orchestrator_chunked.py', '_get_filtered_subprojects', 2, 9, 5).
python_function('code2llm/cli_exports/orchestrator_chunked.py', '_process_subproject', 3, 5, 4).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_mermaid', 3, 5, 17).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_mermaid_pngs', 2, 6, 3).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_calls', 4, 5, 5).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_context_fallback', 3, 3, 5).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_data_structures', 3, 2, 4).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_project_toon', 3, 2, 9).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_readme', 3, 4, 8).
python_function('code2llm/cli_exports/orchestrator_handlers.py', '_export_index_html', 2, 5, 7).
python_function('code2llm/cli_exports/prompt.py', '_export_prompt_txt', 4, 7, 14).
python_function('code2llm/cli_exports/prompt.py', '_export_chunked_prompt_txt', 5, 5, 12).
python_function('code2llm/cli_exports/prompt.py', '_get_prompt_paths', 2, 5, 3).
python_function('code2llm/cli_exports/prompt.py', '_build_prompt_header', 1, 1, 0).
python_function('code2llm/cli_exports/prompt.py', '_find_existing_prompt_file', 2, 3, 1).
python_function('code2llm/cli_exports/prompt.py', '_build_prompt_file_lines', 3, 4, 4).
python_function('code2llm/cli_exports/prompt.py', '_build_main_files_section', 2, 1, 1).
python_function('code2llm/cli_exports/prompt.py', '_build_optional_files_section', 2, 2, 1).
python_function('code2llm/cli_exports/prompt.py', '_format_size', 1, 3, 0).
python_function('code2llm/cli_exports/prompt.py', '_get_missing_files', 1, 3, 2).
python_function('code2llm/cli_exports/prompt.py', '_build_subprojects_section', 3, 6, 7).
python_function('code2llm/cli_exports/prompt.py', '_build_missing_files_section', 2, 6, 2).
python_function('code2llm/cli_exports/prompt.py', '_probe_output_files', 1, 3, 1).
python_function('code2llm/cli_exports/prompt.py', '_analyze_generated_files', 2, 3, 4).
python_function('code2llm/cli_exports/prompt.py', '_build_dynamic_focus_areas', 1, 9, 2).
python_function('code2llm/cli_exports/prompt.py', '_build_dynamic_tasks', 1, 8, 2).
python_function('code2llm/cli_exports/prompt.py', '_build_priority_order', 1, 9, 2).
python_function('code2llm/cli_exports/prompt.py', '_build_strategy_section', 1, 9, 2).
python_function('code2llm/cli_exports/prompt.py', '_build_prompt_footer', 2, 5, 5).
python_function('code2llm/cli_parser.py', 'get_version', 0, 2, 5).
python_function('code2llm/cli_parser.py', 'create_parser', 0, 1, 5).
python_function('code2llm/core/__init__.py', '__getattr__', 1, 6, 3).
python_function('code2llm/core/config.py', '_get_optimal_workers', 2, 3, 5).
python_function('code2llm/core/file_analyzer.py', '_analyze_single_file', 1, 1, 3).
python_function('code2llm/core/file_cache.py', 'make_cache_key', 2, 1, 4).
python_function('code2llm/core/gitignore.py', '_nearest_ignore_files', 2, 7, 2).
python_function('code2llm/core/gitignore.py', 'load_gitignore_patterns', 1, 2, 3).
python_function('code2llm/core/incremental.py', '_file_signature', 1, 2, 1).
python_function('code2llm/core/lang/__init__.py', 'register_language', 0, 1, 5).
python_function('code2llm/core/lang/__init__.py', 'get_parser', 1, 1, 2).
python_function('code2llm/core/lang/__init__.py', 'list_parsers', 0, 1, 1).
python_function('code2llm/core/lang/_c_parser.py', '_update_brace_tracking', 5, 7, 0).
python_function('code2llm/core/lang/_c_parser.py', '_process_decorators', 3, 3, 3).
python_function('code2llm/core/lang/_c_parser.py', '_process_classes', 11, 10, 10).
python_function('code2llm/core/lang/_c_parser.py', '_process_standalone_function', 10, 10, 8).
python_function('code2llm/core/lang/_c_parser.py', '_try_match_named_pattern', 4, 8, 4).
python_function('code2llm/core/lang/_c_parser.py', '_match_method_name', 5, 4, 1).
python_function('code2llm/core/lang/_c_parser.py', '_process_class_method', 12, 2, 6).
python_function('code2llm/core/lang/_c_parser.py', '_process_functions', 13, 9, 2).
python_function('code2llm/core/lang/_c_parser.py', '_clear_orphaned_decorators', 7, 7, 3).
python_function('code2llm/core/lang/_c_parser.py', '_extract_declarations', 6, 9, 15).
python_function('code2llm/core/lang/_calls.py', '_resolve_call', 6, 7, 4).
python_function('code2llm/core/lang/_calls.py', 'extract_calls_regex', 3, 9, 9).
python_function('code2llm/core/lang/_complexity.py', 'extract_function_body', 2, 10, 4).
python_function('code2llm/core/lang/_complexity.py', 'calculate_complexity_regex', 3, 6, 5).
python_function('code2llm/core/lang/base.py', 'analyze_c_family', 8, 5, 6).
python_function('code2llm/core/lang/cpp.py', 'analyze_cpp', 5, 1, 1).
python_function('code2llm/core/lang/csharp.py', 'analyze_csharp', 5, 1, 1).
python_function('code2llm/core/lang/generic.py', '_scan_generic_line', 6, 6, 6).
python_function('code2llm/core/lang/generic.py', 'analyze_generic', 5, 6, 7).
python_function('code2llm/core/lang/go_lang.py', '_analyze_go_regex', 4, 10, 11).
python_function('code2llm/core/lang/go_lang.py', 'analyze_go', 5, 4, 6).
python_function('code2llm/core/lang/java.py', 'analyze_java', 5, 1, 1).
python_function('code2llm/core/lang/php.py', '_parse_php_metadata', 3, 8, 6).
python_function('code2llm/core/lang/php.py', '_adjust_qualified_names', 3, 3, 5).
python_function('code2llm/core/lang/php.py', '_extract_php_traits', 6, 4, 8).
python_function('code2llm/core/lang/php.py', 'analyze_php', 5, 2, 7).
python_function('code2llm/core/lang/ruby.py', '_is_ruby_end', 1, 3, 2).
python_function('code2llm/core/lang/ruby.py', '_scan_ruby_body_lines', 2, 6, 4).
python_function('code2llm/core/lang/ruby.py', '_extract_ruby_body', 2, 6, 5).
python_function('code2llm/core/lang/ruby.py', '_adjust_ruby_module_qualnames', 3, 4, 4).
python_function('code2llm/core/lang/ruby.py', '_track_ruby_module', 1, 9, 6).
python_function('code2llm/core/lang/ruby.py', '_compute_ruby_cc', 2, 4, 4).
python_function('code2llm/core/lang/ruby.py', 'analyze_ruby', 5, 2, 8).
python_function('code2llm/core/lang/rust.py', 'analyze_rust', 5, 9, 14).
python_function('code2llm/core/lang/ts_extractors.py', '_get_node_text', 2, 1, 1).
python_function('code2llm/core/lang/ts_extractors.py', '_find_name_node', 1, 7, 0).
python_function('code2llm/core/lang/ts_extractors.py', '_extract_functions_ts', 5, 1, 5).
python_function('code2llm/core/lang/ts_extractors.py', '_extract_classes_ts', 5, 1, 5).
python_function('code2llm/core/lang/ts_extractors.py', 'extract_declarations_ts', 5, 1, 5).
python_function('code2llm/core/lang/ts_parser.py', '_init_tree_sitter', 0, 2, 1).
python_function('code2llm/core/lang/ts_parser.py', '_get_language', 1, 7, 6).
python_function('code2llm/core/lang/ts_parser.py', '_get_parser', 1, 4, 3).
python_function('code2llm/core/lang/ts_parser.py', 'get_parser', 0, 2, 1).
python_function('code2llm/core/lang/ts_parser.py', 'parse_source', 2, 1, 3).
python_function('code2llm/core/lang/ts_parser.py', 'is_available', 0, 1, 1).
python_function('code2llm/core/lang/typescript.py', 'get_typescript_patterns', 0, 1, 1).
python_function('code2llm/core/lang/typescript.py', 'get_typescript_lang_config', 0, 1, 0).
python_function('code2llm/core/lang/typescript.py', 'analyze_typescript_js', 5, 1, 5).
python_function('code2llm/core/large_repo.py', 'should_use_chunking', 2, 1, 1).
python_function('code2llm/core/large_repo.py', 'get_analysis_plan', 2, 2, 2).
python_function('code2llm/core/persistent_cache.py', '_pack', 1, 1, 1).
python_function('code2llm/core/persistent_cache.py', '_unpack', 1, 1, 1).
python_function('code2llm/core/persistent_cache.py', 'get_all_projects', 1, 6, 7).
python_function('code2llm/core/persistent_cache.py', 'clear_all', 1, 2, 2).
python_function('code2llm/core/repo_files.py', '_get_gitignore_parser', 1, 2, 2).
python_function('code2llm/core/repo_files.py', 'should_skip_file', 3, 8, 5).
python_function('code2llm/core/repo_files.py', 'collect_files_in_dir', 2, 6, 8).
python_function('code2llm/core/repo_files.py', 'collect_root_files', 1, 3, 5).
python_function('code2llm/core/repo_files.py', 'count_py_files', 1, 3, 4).
python_function('code2llm/core/repo_files.py', 'contains_python_files', 1, 3, 4).
python_function('code2llm/core/repo_files.py', 'get_level1_dirs', 1, 8, 8).
python_function('code2llm/core/repo_files.py', 'calculate_priority', 2, 7, 1).
python_function('code2llm/core/source_classifier.py', '_relative_parts', 2, 4, 4).
python_function('code2llm/core/source_classifier.py', '_looks_like_generated_content', 1, 3, 3).
python_function('code2llm/core/source_classifier.py', '_has_code2llm_output_manifest', 1, 3, 1).
python_function('code2llm/core/source_classifier.py', '_is_generated_by_name', 2, 6, 3).
python_function('code2llm/core/source_classifier.py', 'is_generated_artifact', 2, 7, 8).
python_function('code2llm/core/source_classifier.py', 'classify_source_path', 2, 9, 5).
python_function('code2llm/core/source_classifier.py', 'is_structural_only_file', 1, 1, 2).
python_function('code2llm/core/toon_size_manager.py', 'get_file_size_kb', 1, 1, 1).
python_function('code2llm/core/toon_size_manager.py', 'should_split_toon', 2, 1, 1).
python_function('code2llm/core/toon_size_manager.py', 'split_toon_file', 4, 3, 6).
python_function('code2llm/core/toon_size_manager.py', '_parse_modules', 1, 6, 6).
python_function('code2llm/core/toon_size_manager.py', '_split_by_modules', 5, 10, 10).
python_function('code2llm/core/toon_size_manager.py', '_split_by_lines', 4, 8, 9).
python_function('code2llm/core/toon_size_manager.py', '_write_chunk', 4, 2, 1).
python_function('code2llm/core/toon_size_manager.py', 'manage_toon_size', 5, 8, 6).
python_function('code2llm/exporters/base.py', 'export_format', 4, 1, 0).
python_function('code2llm/exporters/base.py', 'get_exporter', 1, 1, 1).
python_function('code2llm/exporters/base.py', 'list_exporters', 0, 2, 1).
python_function('code2llm/exporters/evolution/computation.py', 'compute_func_data', 1, 3, 8).
python_function('code2llm/exporters/evolution/computation.py', '_scan_from_result', 1, 8, 4).
python_function('code2llm/exporters/evolution/computation.py', '_scan_from_filesystem', 1, 8, 6).
python_function('code2llm/exporters/evolution/computation.py', 'scan_file_sizes', 2, 6, 3).
python_function('code2llm/exporters/evolution/computation.py', 'aggregate_file_stats', 2, 7, 7).
python_function('code2llm/exporters/evolution/computation.py', 'make_relative_path', 2, 3, 3).
python_function('code2llm/exporters/evolution/computation.py', 'filter_god_modules', 2, 3, 5).
python_function('code2llm/exporters/evolution/computation.py', 'compute_god_modules', 1, 2, 4).
python_function('code2llm/exporters/evolution/computation.py', 'compute_hub_types', 1, 7, 4).
python_function('code2llm/exporters/evolution/computation.py', 'build_context', 1, 10, 8).
python_function('code2llm/exporters/evolution/exclusion.py', 'is_excluded', 1, 2, 6).
python_function('code2llm/exporters/evolution/render.py', 'render_header', 1, 1, 2).
python_function('code2llm/exporters/evolution/render.py', 'render_next', 1, 10, 4).
python_function('code2llm/exporters/evolution/render.py', 'render_risks', 1, 6, 2).
python_function('code2llm/exporters/evolution/render.py', 'render_metrics_target', 1, 1, 4).
python_function('code2llm/exporters/evolution/render.py', 'render_patterns', 1, 1, 0).
python_function('code2llm/exporters/evolution/render.py', 'render_history', 2, 6, 8).
python_function('code2llm/exporters/evolution/yaml_export.py', '_build_refactoring_actions', 1, 8, 3).
python_function('code2llm/exporters/evolution/yaml_export.py', '_build_risks', 1, 4, 1).
python_function('code2llm/exporters/evolution/yaml_export.py', 'export_to_yaml', 2, 1, 13).
python_function('code2llm/exporters/flow_constants.py', 'is_excluded_path', 1, 2, 6).
python_function('code2llm/exporters/index_generator/__init__.py', 'generate_index_html', 1, 1, 2).
python_function('code2llm/exporters/index_generator/scanner.py', 'get_file_types', 0, 1, 1).
python_function('code2llm/exporters/index_generator/scanner.py', 'get_default_file_info', 1, 2, 1).
python_function('code2llm/exporters/map/alerts.py', 'build_alerts', 1, 8, 5).
python_function('code2llm/exporters/map/alerts.py', 'build_hotspots', 1, 5, 4).
python_function('code2llm/exporters/map/alerts.py', 'load_evolution_trend', 2, 5, 2).
python_function('code2llm/exporters/map/alerts.py', '_read_previous_cc_avg', 1, 6, 6).
python_function('code2llm/exporters/map/details.py', 'render_details', 2, 2, 2).
python_function('code2llm/exporters/map/details.py', '_rank_modules', 2, 5, 6).
python_function('code2llm/exporters/map/details.py', '_collect_module_exports', 2, 6, 0).
python_function('code2llm/exporters/map/details.py', '_render_map_module', 4, 8, 8).
python_function('code2llm/exporters/map/details.py', '_render_map_class', 3, 7, 5).
python_function('code2llm/exporters/map/details.py', '_function_signature', 1, 5, 2).
python_function('code2llm/exporters/map/header.py', 'render_header', 3, 8, 15).
python_function('code2llm/exporters/map/header.py', '_render_stats_line', 4, 5, 4).
python_function('code2llm/exporters/map/header.py', '_render_alerts_line', 1, 2, 3).
python_function('code2llm/exporters/map/header.py', '_render_hotspots_line', 1, 2, 3).
python_function('code2llm/exporters/map/module_list.py', 'render_module_list', 2, 4, 7).
python_function('code2llm/exporters/map/utils.py', 'rel_path', 2, 6, 5).
python_function('code2llm/exporters/map/utils.py', 'file_line_count', 1, 2, 5).
python_function('code2llm/exporters/map/utils.py', 'count_total_lines', 2, 5, 5).
python_function('code2llm/exporters/map/utils.py', 'detect_languages', 2, 8, 10).
python_function('code2llm/exporters/map/yaml_export.py', 'export_to_yaml', 3, 8, 14).
python_function('code2llm/exporters/map/yaml_export.py', '_build_module_entry', 3, 2, 6).
python_function('code2llm/exporters/map/yaml_export.py', '_build_module_exports', 2, 6, 2).
python_function('code2llm/exporters/map/yaml_export.py', '_build_module_classes_data', 2, 6, 3).
python_function('code2llm/exporters/map/yaml_export.py', '_build_module_functions_data', 2, 7, 2).
python_function('code2llm/exporters/mermaid/calls.py', '_collect_call_edges', 2, 6, 6).
python_function('code2llm/exporters/mermaid/calls.py', 'export_calls', 2, 7, 13).
python_function('code2llm/exporters/mermaid/classic.py', 'export_classic', 2, 1, 5).
python_function('code2llm/exporters/mermaid/classic.py', '_render_subgraphs', 2, 6, 8).
python_function('code2llm/exporters/mermaid/classic.py', '_render_edges', 4, 8, 7).
python_function('code2llm/exporters/mermaid/classic.py', '_render_cc_styles', 2, 6, 5).
python_function('code2llm/exporters/mermaid/compact.py', '_compute_module_stats', 2, 3, 4).
python_function('code2llm/exporters/mermaid/compact.py', '_compute_cross_edges', 3, 5, 4).
python_function('code2llm/exporters/mermaid/compact.py', 'export_compact', 2, 7, 10).
python_function('code2llm/exporters/mermaid/flow_compact.py', 'should_skip_module', 2, 3, 2).
python_function('code2llm/exporters/mermaid/flow_compact.py', '_get_called_funcs', 1, 3, 4).
python_function('code2llm/exporters/mermaid/flow_compact.py', 'is_entry_point', 3, 9, 4).
python_function('code2llm/exporters/mermaid/flow_compact.py', 'build_callers_graph', 2, 4, 4).
python_function('code2llm/exporters/mermaid/flow_compact.py', 'find_leaves', 2, 4, 5).
python_function('code2llm/exporters/mermaid/flow_compact.py', '_longest_path_dfs', 4, 7, 4).
python_function('code2llm/exporters/mermaid/flow_compact.py', '_select_longest_path', 3, 4, 3).
python_function('code2llm/exporters/mermaid/flow_compact.py', 'find_critical_path', 2, 2, 5).
python_function('code2llm/exporters/mermaid/flow_compact.py', 'export_flow_compact', 3, 1, 6).
python_function('code2llm/exporters/mermaid/flow_detailed.py', 'export_flow_detailed', 3, 1, 9).
python_function('code2llm/exporters/mermaid/flow_full.py', 'export_flow_full', 3, 1, 9).
python_function('code2llm/exporters/mermaid/utils.py', 'readable_id', 1, 1, 1).
python_function('code2llm/exporters/mermaid/utils.py', 'safe_module', 1, 1, 1).
python_function('code2llm/exporters/mermaid/utils.py', '_sanitize_identifier', 2, 4, 3).
python_function('code2llm/exporters/mermaid/utils.py', 'module_of', 1, 4, 3).
python_function('code2llm/exporters/mermaid/utils.py', 'build_name_index', 1, 2, 3).
python_function('code2llm/exporters/mermaid/utils.py', 'resolve_callee', 3, 6, 3).
python_function('code2llm/exporters/mermaid/utils.py', 'write_file', 2, 1, 5).
python_function('code2llm/exporters/mermaid/utils.py', 'get_cc', 1, 3, 2).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_filtered_functions', 4, 4, 4).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_entry_points', 3, 3, 2).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_group_functions_by_module', 2, 2, 4).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_classify_architecture_module', 2, 4, 1).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_group_architecture_functions', 2, 2, 3).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_select_key_functions', 6, 6, 3).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_append_flow_node', 9, 4, 3).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_render_module_subgraphs', 11, 7, 8).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_resolve_callee', 4, 2, 1).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_add_edge_if_new', 5, 4, 3).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_render_flow_edges', 7, 8, 6).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_append_entry_styles', 4, 3, 3).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_render_flow_styles', 10, 6, 6).
python_function('code2llm/exporters/mermaid_flow_helpers.py', '_render_architecture_view', 7, 6, 9).
python_function('code2llm/exporters/planfile_tickets.py', 'collect_planfile_tickets', 1, 5, 9).
python_function('code2llm/exporters/planfile_tickets.py', 'apply_planfile_tickets', 1, 8, 6).
python_function('code2llm/exporters/planfile_tickets.py', '_high_cc_tickets', 1, 4, 5).
python_function('code2llm/exporters/planfile_tickets.py', '_god_module_tickets', 1, 4, 5).
python_function('code2llm/exporters/planfile_tickets.py', '_duplicate_class_tickets', 1, 8, 8).
python_function('code2llm/exporters/planfile_tickets.py', '_smell_tickets', 1, 5, 7).
python_function('code2llm/exporters/planfile_tickets.py', '_function_cc', 1, 2, 2).
python_function('code2llm/exporters/planfile_tickets.py', '_method_names', 1, 2, 1).
python_function('code2llm/exporters/planfile_tickets.py', '_rel_path', 2, 4, 5).
python_function('code2llm/exporters/planfile_tickets.py', '_project_root', 2, 3, 4).
python_function('code2llm/exporters/planfile_tickets.py', '_description_with_dedupe', 1, 2, 0).
python_function('code2llm/exporters/planfile_tickets.py', '_default_runner', 2, 1, 2).
python_function('code2llm/exporters/planfile_tickets.py', '_parse_ticket_title', 1, 7, 4).
python_function('code2llm/exporters/planfile_tickets.py', '_existing_planfile_titles', 1, 8, 5).
python_function('code2llm/exporters/project_yaml/evolution.py', 'build_evolution', 3, 3, 4).
python_function('code2llm/exporters/project_yaml/evolution.py', 'load_previous_evolution', 1, 6, 4).
python_function('code2llm/exporters/project_yaml/health.py', 'build_health', 2, 7, 9).
python_function('code2llm/exporters/project_yaml/health.py', '_severity_for', 3, 3, 0).
python_function('code2llm/exporters/project_yaml/health.py', '_display_name', 1, 2, 0).
python_function('code2llm/exporters/project_yaml/health.py', 'build_alerts', 1, 7, 9).
python_function('code2llm/exporters/project_yaml/health.py', 'count_duplicates', 1, 5, 8).
python_function('code2llm/exporters/project_yaml/hotspots.py', 'build_hotspots', 1, 5, 7).
python_function('code2llm/exporters/project_yaml/hotspots.py', 'hotspot_note', 2, 7, 1).
python_function('code2llm/exporters/project_yaml/hotspots.py', '_cc_priorities', 1, 6, 6).
python_function('code2llm/exporters/project_yaml/hotspots.py', '_cycle_priorities', 1, 4, 4).
python_function('code2llm/exporters/project_yaml/hotspots.py', '_fanout_priorities', 1, 3, 0).
python_function('code2llm/exporters/project_yaml/hotspots.py', '_godmod_priorities', 1, 3, 0).
python_function('code2llm/exporters/project_yaml/hotspots.py', 'build_refactoring', 3, 1, 6).
python_function('code2llm/exporters/project_yaml/modules.py', 'build_modules', 2, 5, 9).
python_function('code2llm/exporters/project_yaml/modules.py', 'group_by_file', 1, 5, 4).
python_function('code2llm/exporters/project_yaml/modules.py', 'compute_module_entry', 5, 4, 6).
python_function('code2llm/exporters/project_yaml/modules.py', 'compute_inbound_deps', 3, 5, 3).
python_function('code2llm/exporters/project_yaml/modules.py', 'build_exports', 3, 2, 3).
python_function('code2llm/exporters/project_yaml/modules.py', '_build_notable_method_entry', 1, 5, 3).
python_function('code2llm/exporters/project_yaml/modules.py', 'build_class_export', 2, 9, 5).
python_function('code2llm/exporters/project_yaml/modules.py', 'build_function_exports', 2, 7, 5).
python_function('code2llm/exporters/readme/content.py', 'generate_readme_content', 9, 1, 2).
python_function('code2llm/exporters/readme/files.py', 'get_existing_files', 1, 2, 1).
python_function('code2llm/exporters/readme/insights.py', '_parse_toon_metrics', 1, 7, 4).
python_function('code2llm/exporters/readme/insights.py', '_parse_evolution_actions', 1, 3, 4).
python_function('code2llm/exporters/readme/insights.py', 'extract_insights', 1, 6, 5).
python_function('code2llm/exporters/readme/sections.py', 'build_core_files_section', 2, 4, 3).
python_function('code2llm/exporters/readme/sections.py', 'build_llm_files_section', 1, 5, 3).
python_function('code2llm/exporters/readme/sections.py', 'build_viz_files_section', 1, 7, 3).
python_function('code2llm/exporters/report_generators.py', '_read_yaml_content', 1, 4, 4).
python_function('code2llm/exporters/report_generators.py', '_parse_yaml_content', 2, 7, 2).
python_function('code2llm/exporters/report_generators.py', '_validate_yaml_data', 2, 4, 5).
python_function('code2llm/exporters/report_generators.py', 'load_project_yaml', 1, 1, 3).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_select_top_packages', 2, 6, 3).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_render_coupling_header', 1, 4, 3).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_build_coupling_row', 4, 6, 3).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_coupling_row_tag', 2, 3, 1).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_render_coupling_summary', 3, 6, 4).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_render_layer_package', 5, 5, 4).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_format_layer_file_row', 2, 7, 2).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_render_zero_line_files', 2, 5, 3).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_format_function_row', 2, 7, 1).
python_function('code2llm/exporters/toon/_render_coupling_helpers.py', '_render_cc_summary', 3, 7, 2).
python_function('code2llm/exporters/toon/_render_section_helpers.py', '_detect_language_label', 1, 10, 11).
python_function('code2llm/exporters/toon/_render_section_helpers.py', 'render_health_section', 1, 4, 2).
python_function('code2llm/exporters/toon/_render_section_helpers.py', '_build_refactor_steps', 1, 9, 4).
python_function('code2llm/exporters/toon/_render_section_helpers.py', 'render_refactor_section', 1, 3, 4).
python_function('code2llm/exporters/toon/_render_section_helpers.py', 'render_hotspots_section', 1, 3, 2).
python_function('code2llm/exporters/toon/_render_section_helpers.py', 'render_classes_section', 1, 10, 4).
python_function('code2llm/exporters/toon/_render_section_helpers.py', 'render_external_section', 1, 1, 0).
python_function('code2llm/exporters/toon/_render_section_helpers.py', '_trace_pipeline', 3, 8, 6).
python_function('code2llm/exporters/toon/_render_section_helpers.py', '_calculate_purity', 2, 8, 5).
python_function('code2llm/exporters/toon/_render_section_helpers.py', 'render_pipelines_section', 1, 8, 9).
python_function('code2llm/exporters/toon/helpers.py', '_is_excluded', 1, 1, 1).
python_function('code2llm/exporters/toon/helpers.py', '_rel_path', 2, 6, 5).
python_function('code2llm/exporters/toon/helpers.py', '_package_of', 1, 2, 2).
python_function('code2llm/exporters/toon/helpers.py', '_package_of_module', 1, 4, 3).
python_function('code2llm/exporters/toon/helpers.py', '_traits_from_cfg', 2, 7, 5).
python_function('code2llm/exporters/toon/helpers.py', '_dup_file_set', 1, 2, 2).
python_function('code2llm/exporters/toon/helpers.py', '_hotspot_description', 2, 8, 1).
python_function('code2llm/exporters/toon/helpers.py', '_fast_line_counts', 2, 4, 8).
python_function('code2llm/exporters/toon/helpers.py', '_slow_line_counts', 1, 8, 10).
python_function('code2llm/exporters/toon/helpers.py', '_scan_line_counts', 2, 4, 4).
python_function('code2llm/exporters/toon/helpers.py', '_walk_compat', 1, 2, 2).
python_function('code2llm/exporters/validate_project.py', '_log_validation_result', 2, 4, 2).
python_function('code2llm/exporters/validate_project.py', 'validate_project_yaml', 2, 6, 9).
python_function('code2llm/exporters/validate_project.py', '_check_required_keys', 1, 9, 2).
python_function('code2llm/exporters/validate_project.py', '_cross_check_toon', 2, 7, 7).
python_function('code2llm/generators/_utils.py', 'dump_yaml', 1, 1, 1).
python_function('code2llm/generators/llm_flow/analysis.py', '_node_counts_by_function', 1, 4, 4).
python_function('code2llm/generators/llm_flow/analysis.py', '_pick_relevant_functions', 0, 8, 8).
python_function('code2llm/generators/llm_flow/analysis.py', '_classify_node_into', 4, 5, 5).
python_function('code2llm/generators/llm_flow/analysis.py', '_collect_node_data', 1, 7, 5).
python_function('code2llm/generators/llm_flow/analysis.py', '_summarize_functions', 3, 4, 7).
python_function('code2llm/generators/llm_flow/analysis.py', '_build_call_graph', 2, 4, 3).
python_function('code2llm/generators/llm_flow/analysis.py', '_reachable', 3, 8, 9).
python_function('code2llm/generators/llm_flow/cli.py', 'create_parser', 0, 1, 2).
python_function('code2llm/generators/llm_flow/cli.py', 'main', 1, 3, 12).
python_function('code2llm/generators/llm_flow/generator.py', 'generate_llm_flow', 4, 5, 10).
python_function('code2llm/generators/llm_flow/generator.py', 'render_llm_flow_md', 1, 10, 8).
python_function('code2llm/generators/llm_flow/nodes.py', '_collect_nodes', 1, 5, 4).
python_function('code2llm/generators/llm_flow/nodes.py', '_group_nodes_by_file', 1, 3, 5).
python_function('code2llm/generators/llm_flow/nodes.py', '_is_entrypoint_file', 1, 2, 1).
python_function('code2llm/generators/llm_flow/nodes.py', '_extract_entrypoint_info', 2, 4, 3).
python_function('code2llm/generators/llm_flow/nodes.py', '_deduplicate_entrypoints', 1, 5, 4).
python_function('code2llm/generators/llm_flow/nodes.py', '_collect_entrypoints', 1, 5, 6).
python_function('code2llm/generators/llm_flow/nodes.py', '_collect_functions', 1, 7, 7).
python_function('code2llm/generators/llm_flow/parsing.py', '_parse_call_label', 1, 5, 6).
python_function('code2llm/generators/llm_flow/parsing.py', '_parse_func_label', 1, 4, 3).
python_function('code2llm/generators/llm_flow/utils.py', '_strip_bom', 1, 2, 1).
python_function('code2llm/generators/llm_flow/utils.py', '_read_yaml_raw', 1, 4, 4).
python_function('code2llm/generators/llm_flow/utils.py', '_parse_yaml_safe', 2, 7, 2).
python_function('code2llm/generators/llm_flow/utils.py', '_validate_yaml_mapping', 2, 3, 3).
python_function('code2llm/generators/llm_flow/utils.py', '_safe_read_yaml', 1, 1, 3).
python_function('code2llm/generators/llm_flow/utils.py', '_as_dict', 1, 2, 1).
python_function('code2llm/generators/llm_flow/utils.py', '_as_list', 1, 2, 1).
python_function('code2llm/generators/llm_flow/utils.py', '_shorten', 2, 3, 4).
python_function('code2llm/generators/llm_task.py', '_strip_bom', 1, 2, 1).
python_function('code2llm/generators/llm_task.py', '_ensure_list', 1, 3, 1).
python_function('code2llm/generators/llm_task.py', '_deep_get', 2, 4, 1).
python_function('code2llm/generators/llm_task.py', '_sec', 2, 2, 2).
python_function('code2llm/generators/llm_task.py', '_sget', 3, 3, 2).
python_function('code2llm/generators/llm_task.py', 'normalize_llm_task', 1, 1, 4).
python_function('code2llm/generators/llm_task.py', '_parse_bullets', 1, 4, 3).
python_function('code2llm/generators/llm_task.py', '_parse_sections', 1, 7, 6).
python_function('code2llm/generators/llm_task.py', '_create_empty_task_data', 0, 1, 0).
python_function('code2llm/generators/llm_task.py', '_apply_simple_sections', 2, 5, 4).
python_function('code2llm/generators/llm_task.py', '_apply_bullet_sections', 2, 6, 2).
python_function('code2llm/generators/llm_task.py', '_parse_acceptance_tests', 1, 3, 4).
python_function('code2llm/generators/llm_task.py', 'parse_llm_task_text', 1, 2, 10).
python_function('code2llm/generators/llm_task.py', '_load_yaml', 2, 9, 4).
python_function('code2llm/generators/llm_task.py', '_load_json', 2, 2, 3).
python_function('code2llm/generators/llm_task.py', 'load_input', 1, 6, 8).
python_function('code2llm/generators/llm_task.py', 'create_parser', 0, 1, 2).
python_function('code2llm/generators/llm_task.py', 'main', 1, 4, 11).
python_function('code2llm/generators/mermaid/fix.py', '_sanitize_label_text', 1, 1, 1).
python_function('code2llm/generators/mermaid/fix.py', '_sanitize_node_id', 1, 3, 3).
python_function('code2llm/generators/mermaid/fix.py', 'fix_mermaid_file', 1, 5, 10).
python_function('code2llm/generators/mermaid/fix.py', '_fix_edge_line', 1, 5, 7).
python_function('code2llm/generators/mermaid/fix.py', '_fix_edge_label_pipes', 1, 8, 5).
python_function('code2llm/generators/mermaid/fix.py', '_fix_subgraph_line', 1, 3, 5).
python_function('code2llm/generators/mermaid/fix.py', '_fix_class_line', 1, 6, 8).
python_function('code2llm/generators/mermaid/png.py', '_is_png_fresh', 2, 2, 2).
python_function('code2llm/generators/mermaid/png.py', '_prepare_and_render', 3, 4, 6).
python_function('code2llm/generators/mermaid/png.py', 'generate_pngs', 4, 7, 9).
python_function('code2llm/generators/mermaid/png.py', '_setup_puppeteer_config', 0, 5, 6).
python_function('code2llm/generators/mermaid/png.py', '_build_renderers', 4, 3, 2).
python_function('code2llm/generators/mermaid/png.py', '_run_mmdc_subprocess', 6, 8, 4).
python_function('code2llm/generators/mermaid/png.py', 'generate_single_png', 3, 4, 5).
python_function('code2llm/generators/mermaid/png.py', 'generate_with_puppeteer', 5, 2, 7).
python_function('code2llm/generators/mermaid/validation.py', 'validate_mermaid_file', 1, 6, 9).
python_function('code2llm/generators/mermaid/validation.py', '_strip_label_segments', 1, 1, 1).
python_function('code2llm/generators/mermaid/validation.py', '_is_balanced_node_line', 1, 6, 0).
python_function('code2llm/generators/mermaid/validation.py', '_check_bracket_balance', 2, 7, 7).
python_function('code2llm/generators/mermaid/validation.py', '_scan_brackets', 5, 10, 2).
python_function('code2llm/generators/mermaid/validation.py', '_check_single_node_line', 4, 6, 4).
python_function('code2llm/generators/mermaid/validation.py', '_check_node_ids', 2, 7, 6).
python_function('code2llm/generators/mermaid.py', 'run_cli', 0, 1, 6).
python_function('code2llm/parsers/toon_parser.py', '_parse_header_line', 2, 2, 2).
python_function('code2llm/parsers/toon_parser.py', '_parse_stats_line', 2, 5, 2).
python_function('code2llm/parsers/toon_parser.py', '_parse_health_line', 2, 3, 2).
python_function('code2llm/parsers/toon_parser.py', '_parse_functions_line', 2, 4, 7).
python_function('code2llm/parsers/toon_parser.py', '_parse_classes_line', 2, 3, 3).
python_function('code2llm/parsers/toon_parser.py', '_parse_hotspots_line', 2, 3, 4).
python_function('code2llm/parsers/toon_parser.py', '_detect_section', 1, 3, 2).
python_function('code2llm/parsers/toon_parser.py', 'parse_toon_content', 1, 8, 8).
python_function('code2llm/parsers/toon_parser.py', 'is_toon_file', 1, 4, 4).
python_function('code2llm/parsers/toon_parser.py', 'load_toon', 1, 2, 4).
python_function('demo_langs/valid/sample.py', 'main', 0, 2, 5).
python_function('examples/docker-doql-example/worker/worker.py', 'process_message', 4, 1, 3).
python_function('examples/docker-doql-example/worker/worker.py', 'main', 0, 1, 8).
python_function('examples/functional_refactoring/cli.py', 'generate', 4, 6, 12).
python_function('examples/litellm/run.py', 'run_analysis', 1, 4, 7).
python_function('examples/litellm/run.py', 'get_refactoring_advice', 2, 2, 4).
python_function('examples/litellm/run.py', 'main', 0, 1, 8).
python_function('examples/streaming-analyzer/demo.py', 'demo_quick_strategy', 0, 2, 7).
python_function('examples/streaming-analyzer/demo.py', 'demo_standard_strategy', 0, 5, 4).
python_function('examples/streaming-analyzer/demo.py', 'demo_deep_strategy', 0, 5, 4).
python_function('examples/streaming-analyzer/demo.py', 'demo_incremental_analysis', 0, 5, 6).
python_function('examples/streaming-analyzer/demo.py', 'demo_memory_limited', 0, 4, 5).
python_function('examples/streaming-analyzer/demo.py', 'demo_custom_progress', 0, 3, 7).
python_function('examples/streaming-analyzer/demo.py', 'main', 0, 3, 4).
python_function('examples/streaming-analyzer/sample_project/main.py', 'main', 0, 3, 4).
python_function('examples/streaming-analyzer/sample_project/utils.py', 'validate_input', 1, 4, 1).
python_function('examples/streaming-analyzer/sample_project/utils.py', 'format_output', 1, 3, 3).
python_function('examples/streaming-analyzer/sample_project/utils.py', 'calculate_metrics', 1, 4, 3).
python_function('examples/streaming-analyzer/sample_project/utils.py', 'filter_data', 2, 5, 3).
python_function('examples/streaming-analyzer/sample_project/utils.py', 'transform_data', 2, 7, 6).
python_function('examples/streaming-analyzer/test_example.py', 'test_imports', 0, 2, 1).
python_function('examples/streaming-analyzer/test_example.py', 'test_basic_analysis', 0, 4, 4).
python_function('examples/streaming-analyzer/test_example.py', 'main', 0, 4, 5).
python_function('pipeline.py', '_detect_primary_language', 1, 8, 5).
python_function('pipeline.py', 'run_pipeline', 2, 9, 14).
python_function('scripts/benchmark_badges.py', 'get_shield_url', 3, 1, 2).
python_function('scripts/benchmark_badges.py', 'parse_evolution_metrics', 1, 6, 5).
python_function('scripts/benchmark_badges.py', 'parse_format_quality_report', 1, 3, 4).
python_function('scripts/benchmark_badges.py', 'parse_performance_report', 1, 3, 3).
python_function('scripts/benchmark_badges.py', 'generate_badges', 1, 7, 1).
python_function('scripts/benchmark_badges.py', 'generate_format_quality_badges', 1, 6, 8).
python_function('scripts/benchmark_badges.py', 'generate_performance_badges', 1, 6, 2).
python_function('scripts/benchmark_badges.py', 'create_html', 2, 4, 3).
python_function('scripts/benchmark_badges.py', 'main', 0, 5, 15).
python_function('scripts/bump_version.py', 'get_current_version', 0, 3, 7).
python_function('scripts/bump_version.py', 'parse_version', 1, 2, 3).
python_function('scripts/bump_version.py', 'format_version', 3, 1, 0).
python_function('scripts/bump_version.py', 'bump_version', 1, 4, 5).
python_function('scripts/bump_version.py', 'update_pyproject_toml', 1, 1, 5).
python_function('scripts/bump_version.py', 'update_version_file', 1, 1, 3).
python_function('scripts/bump_version.py', 'main', 0, 3, 8).
python_function('setup.py', 'read_version', 0, 1, 5).
python_function('setup.py', 'read_readme', 0, 2, 5).
python_function('test_langs/valid/sample.py', 'main', 0, 2, 5).
python_function('test_python_only/valid/sample.py', 'main', 0, 2, 5).
python_function('tests/test_advanced_analysis.py', 'test_radon_complexity', 0, 6, 5).
python_function('tests/test_advanced_analysis.py', 'test_graph_metrics', 0, 4, 6).
python_function('tests/test_advanced_analysis.py', 'test_circular_dependency', 0, 6, 9).
python_function('tests/test_cache_invalidation_e2e.py', 'project', 2, 1, 5).
python_function('tests/test_cache_invalidation_e2e.py', '_cache_for', 2, 1, 2).
python_function('tests/test_cache_invalidation_e2e.py', '_run_full_analysis', 2, 1, 6).
python_function('tests/test_cache_invalidation_e2e.py', 'test_first_run_populates_manifest', 1, 3, 2).
python_function('tests/test_cache_invalidation_e2e.py', 'test_run_hash_changes_when_file_modified', 1, 2, 4).
python_function('tests/test_cache_invalidation_e2e.py', 'test_run_hash_changes_when_file_deleted', 1, 3, 4).
python_function('tests/test_cache_invalidation_e2e.py', 'test_run_hash_stable_when_nothing_changes', 1, 2, 3).
python_function('tests/test_calls_toon_export.py', 'test_export_calls_toon_generates_file', 1, 6, 6).
python_function('tests/test_calls_toon_export.py', 'test_export_calls_toon_hubs_section', 1, 3, 5).
python_function('tests/test_calls_toon_export.py', 'test_export_calls_toon_modules_section', 1, 5, 5).
python_function('tests/test_calls_toon_export.py', 'test_export_calls_toon_edges_section', 1, 5, 5).
python_function('tests/test_calls_toon_export.py', 'test_export_calls_toon_header_stats', 1, 6, 7).
python_function('tests/test_declarative_collection.py', 'iac_project', 1, 1, 4).
python_function('tests/test_declarative_collection.py', 'test_all_extensions_includes_declarative', 0, 6, 0).
python_function('tests/test_declarative_collection.py', 'test_all_filenames_includes_dockerfile_and_makefile', 0, 4, 0).
python_function('tests/test_declarative_collection.py', 'test_collect_files_discovers_iac', 1, 4, 4).
python_function('tests/test_declarative_collection.py', 'test_modifying_declarative_file_invalidates_cache', 2, 3, 9).
python_function('tests/test_declarative_collection.py', 'test_dockerfile_edit_invalidates_cache', 2, 3, 9).
python_function('tests/test_declarative_collection.py', 'test_dockerfile_variants_matched_by_prefix', 1, 7, 6).
python_function('tests/test_declarative_collection.py', 'test_lockfiles_excluded_by_default', 2, 6, 5).
python_function('tests/test_declarative_collection.py', 'test_generated_analysis_artifacts_are_excluded_by_default', 1, 10, 8).
python_function('tests/test_declarative_collection.py', 'test_code2llmignore_is_applied', 1, 4, 6).
python_function('tests/test_declarative_collection.py', 'test_markdown_and_config_do_not_emit_fake_symbols', 1, 7, 4).
python_function('tests/test_deep_analysis.py', 'test_astroid_resolution_mock', 1, 6, 14).
python_function('tests/test_deep_analysis.py', 'test_vulture_dead_code', 1, 9, 9).
python_function('tests/test_export_cache_flags.py', 'test_force_skips_export_cache', 0, 2, 2).
python_function('tests/test_export_cache_flags.py', 'test_no_cache_skips_export_cache', 0, 2, 2).
python_function('tests/test_export_cache_flags.py', 'test_chunked_skips_export_cache', 0, 2, 2).
python_function('tests/test_export_cache_flags.py', 'test_standard_run_can_use_export_cache', 0, 2, 2).
python_function('tests/test_file_analyzer_tagging.py', 'analyzer', 0, 1, 3).
python_function('tests/test_file_analyzer_tagging.py', 'test_analyze_file_tags_result_with_path', 4, 3, 5).
python_function('tests/test_file_analyzer_tagging.py', 'test_nonexistent_file_returns_empty', 2, 2, 2).
python_function('tests/test_file_analyzer_tagging.py', 'test_cached_result_also_tagged', 1, 3, 7).
python_function('tests/test_flow_exporter.py', 'typed_source', 1, 1, 3).
python_function('tests/test_flow_exporter.py', 'untyped_source', 1, 1, 3).
python_function('tests/test_flow_exporter.py', '_make_fi', 9, 5, 1).
python_function('tests/test_format_quality.py', 'ground_truth_project', 1, 1, 4).
python_function('tests/test_format_quality.py', 'analysis_result', 1, 1, 5).
python_function('tests/test_orchestrator_cache_mtime.py', '_write', 3, 1, 3).
python_function('tests/test_orchestrator_cache_mtime.py', 'test_copy_cached_export_refreshes_mtime', 1, 4, 5).
python_function('tests/test_orchestrator_cache_mtime.py', 'test_copy_cached_export_preserves_contents', 1, 2, 4).
python_function('tests/test_persistent_cache.py', 'tmp_project', 1, 1, 2).
python_function('tests/test_persistent_cache.py', 'cache', 2, 1, 3).
python_function('tests/test_pipeline_detector.py', '_fi', 8, 4, 1).
python_function('tests/test_pipeline_detector.py', '_build_chain_funcs', 3, 4, 3).
python_function('tests/test_planfile_tickets_exporter.py', '_sample_result', 1, 1, 7).
python_function('tests/test_planfile_tickets_exporter.py', 'test_all_format_includes_planfile_manifest', 0, 2, 1).
python_function('tests/test_planfile_tickets_exporter.py', 'test_planfile_apply_adds_planfile_export_even_when_not_requested', 1, 3, 5).
python_function('tests/test_planfile_tickets_exporter.py', 'test_collect_planfile_tickets_surfaces_actionable_findings', 1, 5, 5).
python_function('tests/test_planfile_tickets_exporter.py', 'test_planfile_exporter_writes_manifest', 1, 5, 7).
python_function('tests/test_planfile_tickets_exporter.py', 'test_apply_planfile_tickets_skips_active_duplicates', 1, 7, 8).
python_function('tests/test_project_toon_export.py', 'test_export_project_toon_writes_file', 1, 6, 7).
python_function('tests/test_project_toon_export.py', 'test_export_single_project_all_triggers_project_toon', 1, 1, 6).
python_function('tests/test_prompt_engine.py', 'test_tiktoken_truncation', 0, 5, 8).
python_function('tests/test_prompt_engine.py', 'test_template_rendering_with_metrics', 0, 5, 7).
python_function('tests/test_prompt_engine.py', 'test_tree_sitter_init', 0, 2, 3).
python_function('tests/test_refactoring_engine.py', 'test_metrics_calculation', 0, 3, 6).
python_function('tests/test_refactoring_engine.py', 'test_mutation_tracking', 0, 5, 4).
python_function('tests/test_refactoring_engine.py', 'test_smell_detection', 0, 2, 5).
python_function('tests/test_toon_v2.py', 'sample_result', 0, 1, 4).
python_function('validate_toon.py', 'load_yaml', 1, 2, 3).
python_function('validate_toon.py', 'load_file', 1, 2, 3).
python_function('validate_toon.py', 'extract_functions_from_yaml', 1, 3, 4).
python_function('validate_toon.py', '_extract_names_from_toon', 2, 3, 3).
python_function('validate_toon.py', 'extract_functions_from_toon', 1, 1, 1).
python_function('validate_toon.py', '_extract_keys_from_yaml', 2, 1, 2).
python_function('validate_toon.py', 'extract_classes_from_yaml', 1, 1, 1).
python_function('validate_toon.py', 'extract_classes_from_toon', 1, 1, 1).
python_function('validate_toon.py', 'analyze_class_differences', 2, 6, 10).
python_function('validate_toon.py', 'extract_modules_from_yaml', 1, 1, 1).
python_function('validate_toon.py', 'extract_modules_from_toon', 1, 3, 4).
python_function('validate_toon.py', 'compare_basic_stats', 2, 4, 3).
python_function('validate_toon.py', 'compare_functions', 2, 6, 6).
python_function('validate_toon.py', 'compare_classes', 2, 1, 5).
python_function('validate_toon.py', 'compare_modules', 2, 5, 6).
python_function('validate_toon.py', 'validate_toon_completeness', 1, 7, 4).
python_function('validate_toon.py', '_run_single_file_mode', 1, 6, 4).
python_function('validate_toon.py', '_run_comparison_mode', 2, 7, 7).
python_function('validate_toon.py', '_compare_all_aspects', 2, 1, 5).
python_function('validate_toon.py', '_print_comparison_summary', 1, 5, 1).
python_function('validate_toon.py', 'main', 0, 3, 5).

% ── Python Classes ───────────────────────────────────────
python_class('benchmarks/format_evaluator.py', 'FormatScore').
python_class('benchmarks/test_performance.py', 'TestPerformanceBenchmarks').
python_method('TestPerformanceBenchmarks', 'large_project', 0, 2, 5).
python_method('TestPerformanceBenchmarks', 'test_fast_mode_performance', 1, 3, 9).
python_method('TestPerformanceBenchmarks', 'test_caching_performance', 1, 3, 6).
python_method('TestPerformanceBenchmarks', 'test_parallel_vs_sequential', 1, 2, 5).
python_method('TestPerformanceBenchmarks', 'test_scaling_with_project_size', 1, 6, 13).
python_class('benchmarks/test_performance.py', 'TestMemoryBenchmarks').
python_method('TestMemoryBenchmarks', 'test_memory_usage_stays_bounded', 1, 3, 12).
python_class('code2llm/analysis/call_graph.py', 'CallGraphExtractor').
python_method('CallGraphExtractor', '__init__', 1, 1, 1).
python_method('CallGraphExtractor', 'extract', 3, 2, 4).
python_method('CallGraphExtractor', '_calculate_metrics', 0, 5, 5).
python_method('CallGraphExtractor', 'visit_Import', 1, 3, 0).
python_method('CallGraphExtractor', 'visit_ImportFrom', 1, 5, 0).
python_method('CallGraphExtractor', 'visit_ClassDef', 1, 5, 5).
python_method('CallGraphExtractor', 'visit_FunctionDef', 1, 2, 4).
python_method('CallGraphExtractor', 'visit_AsyncFunctionDef', 1, 1, 1).
python_method('CallGraphExtractor', 'visit_Call', 1, 8, 5).
python_method('CallGraphExtractor', '_resolve_call', 1, 9, 4).
python_method('CallGraphExtractor', '_resolve_with_astroid', 1, 8, 4).
python_method('CallGraphExtractor', '_expr_to_str', 1, 1, 1).
python_class('code2llm/analysis/cfg.py', 'CFGExtractor').
python_method('CFGExtractor', '__init__', 1, 1, 1).
python_method('CFGExtractor', 'extract', 3, 1, 2).
python_method('CFGExtractor', 'new_node', 2, 2, 2).
python_method('CFGExtractor', 'connect', 4, 3, 2).
python_method('CFGExtractor', 'visit_FunctionDef', 1, 5, 7).
python_method('CFGExtractor', 'visit_AsyncFunctionDef', 1, 1, 1).
python_method('CFGExtractor', 'visit_If', 1, 5, 5).
python_method('CFGExtractor', 'visit_For', 1, 3, 5).
python_method('CFGExtractor', 'visit_While', 1, 3, 5).
python_method('CFGExtractor', 'visit_Try', 1, 4, 4).
python_method('CFGExtractor', 'visit_Assign', 1, 2, 4).
python_method('CFGExtractor', 'visit_Return', 1, 2, 3).
python_method('CFGExtractor', 'visit_Expr', 1, 5, 7).
python_method('CFGExtractor', '_extract_condition', 1, 3, 3).
python_method('CFGExtractor', '_expr_to_str', 1, 1, 1).
python_method('CFGExtractor', '_format_except', 1, 3, 1).
python_class('code2llm/analysis/coupling.py', 'CouplingAnalyzer').
python_method('CouplingAnalyzer', '__init__', 1, 1, 0).
python_method('CouplingAnalyzer', 'analyze', 0, 1, 3).
python_method('CouplingAnalyzer', '_analyze_module_interactions', 0, 7, 5).
python_method('CouplingAnalyzer', '_detect_data_leakage', 0, 5, 2).
python_method('CouplingAnalyzer', '_detect_shared_state', 0, 5, 7).
python_class('code2llm/analysis/data_analysis.py', 'DataAnalyzer').
python_method('DataAnalyzer', 'analyze_data_flow', 1, 1, 4).
python_method('DataAnalyzer', 'analyze_data_structures', 1, 1, 4).
python_class('code2llm/analysis/data_analysis.py', 'DataFlowAnalyzer').
python_method('DataFlowAnalyzer', 'analyze', 1, 1, 4).
python_method('DataFlowAnalyzer', 'find_data_pipelines', 1, 1, 1).
python_method('DataFlowAnalyzer', 'find_state_patterns', 1, 1, 1).
python_method('DataFlowAnalyzer', 'find_data_dependencies', 1, 1, 1).
python_method('DataFlowAnalyzer', 'find_event_flows', 1, 1, 1).
python_class('code2llm/analysis/data_analysis.py', 'OptimizationAdvisor').
python_method('OptimizationAdvisor', 'analyze', 1, 1, 4).
python_method('OptimizationAdvisor', 'analyze_data_types', 1, 1, 1).
python_method('OptimizationAdvisor', 'build_data_flow_graph', 1, 1, 1).
python_method('OptimizationAdvisor', 'identify_process_patterns', 1, 1, 1).
python_method('OptimizationAdvisor', 'analyze_optimization_opportunities', 3, 1, 1).
python_class('code2llm/analysis/dfg.py', 'DFGExtractor').
python_method('DFGExtractor', '__init__', 1, 1, 2).
python_method('DFGExtractor', 'extract', 3, 1, 4).
python_method('DFGExtractor', 'visit_FunctionDef', 1, 3, 3).
python_method('DFGExtractor', 'visit_Assign', 1, 7, 9).
python_method('DFGExtractor', 'visit_AugAssign', 1, 2, 9).
python_method('DFGExtractor', 'visit_For', 1, 3, 6).
python_method('DFGExtractor', 'visit_Call', 1, 7, 11).
python_method('DFGExtractor', '_extract_targets', 1, 2, 2).
python_method('DFGExtractor', '_get_names', 1, 6, 5).
python_method('DFGExtractor', '_extract_names', 1, 5, 4).
python_method('DFGExtractor', '_expr_to_str', 1, 1, 1).
python_method('DFGExtractor', '_build_data_flow_edges', 0, 2, 1).
python_class('code2llm/analysis/pipeline_classifier.py', 'PipelineClassifier').
python_method('PipelineClassifier', '__init__', 1, 2, 1).
python_method('PipelineClassifier', 'classify_domain', 2, 7, 5).
python_method('PipelineClassifier', 'derive_pipeline_name', 3, 8, 5).
python_method('PipelineClassifier', 'get_entry_type', 1, 5, 2).
python_method('PipelineClassifier', 'get_exit_type', 1, 3, 1).
python_class('code2llm/analysis/pipeline_detector.py', 'PipelineStage').
python_class('code2llm/analysis/pipeline_detector.py', 'Pipeline').
python_method('Pipeline', 'purity_ratio', 0, 2, 0).
python_method('Pipeline', 'to_dict', 0, 3, 0).
python_class('code2llm/analysis/pipeline_detector.py', 'PipelineDetector').
python_method('PipelineDetector', '__init__', 2, 3, 4).
python_method('PipelineDetector', 'detect', 2, 3, 6).
python_method('PipelineDetector', '_build_graph', 1, 6, 5).
python_method('PipelineDetector', '_process_components', 3, 8, 7).
python_method('PipelineDetector', '_find_pipeline_paths', 1, 6, 9).
python_method('PipelineDetector', '_longest_path_from', 3, 6, 4).
python_method('PipelineDetector', '_longest_path_in_dag', 1, 7, 7).
python_method('PipelineDetector', '_build_pipelines', 3, 6, 11).
python_method('PipelineDetector', '_build_stages', 3, 5, 4).
python_class('code2llm/analysis/pipeline_resolver.py', 'PipelineResolver').
python_method('PipelineResolver', 'resolve', 3, 4, 5).
python_method('PipelineResolver', '_strip_self_prefix', 1, 2, 1).
python_method('PipelineResolver', '_try_same_class_resolution', 3, 4, 0).
python_method('PipelineResolver', '_get_suffix_candidates', 2, 3, 1).
python_method('PipelineResolver', '_select_same_class_candidate', 3, 10, 1).
python_class('code2llm/analysis/side_effects.py', 'SideEffectInfo').
python_method('SideEffectInfo', '__init__', 2, 2, 0).
python_method('SideEffectInfo', 'is_pure', 0, 1, 0).
python_method('SideEffectInfo', 'side_effect_summary', 0, 7, 2).
python_method('SideEffectInfo', 'to_dict', 0, 1, 0).
python_class('code2llm/analysis/side_effects.py', 'SideEffectDetector').
python_method('SideEffectDetector', '__init__', 1, 2, 1).
python_method('SideEffectDetector', 'analyze_function', 1, 3, 6).
python_method('SideEffectDetector', 'analyze_all', 1, 2, 2).
python_method('SideEffectDetector', 'get_purity_score', 1, 1, 1).
python_method('SideEffectDetector', '_scan_node', 2, 2, 6).
python_method('SideEffectDetector', '_check_io_call', 4, 6, 3).
python_method('SideEffectDetector', '_check_cache_call', 3, 4, 2).
python_method('SideEffectDetector', '_check_calls', 2, 5, 7).
python_method('SideEffectDetector', '_check_assignments', 2, 8, 2).
python_method('SideEffectDetector', '_check_globals', 2, 3, 2).
python_method('SideEffectDetector', '_check_yield', 2, 2, 1).
python_method('SideEffectDetector', '_check_delete', 2, 6, 2).
python_method('SideEffectDetector', '_classify', 1, 6, 0).
python_method('SideEffectDetector', '_heuristic_classify', 2, 8, 4).
python_method('SideEffectDetector', '_get_call_name', 1, 4, 2).
python_class('code2llm/analysis/smells.py', 'SmellDetector').
python_method('SmellDetector', '__init__', 1, 2, 2).
python_method('SmellDetector', 'detect', 0, 1, 8).
python_method('SmellDetector', '_detect_god_functions', 0, 5, 6).
python_method('SmellDetector', '_detect_god_modules', 0, 4, 5).
python_method('SmellDetector', '_detect_feature_envy', 0, 6, 9).
python_method('SmellDetector', '_detect_data_clumps', 0, 7, 7).
python_method('SmellDetector', '_detect_shotgun_surgery', 0, 6, 8).
python_method('SmellDetector', '_detect_bottlenecks', 0, 3, 5).
python_method('SmellDetector', '_detect_circular_dependencies', 0, 4, 5).
python_class('code2llm/analysis/type_inference.py', 'TypeInferenceEngine').
python_method('TypeInferenceEngine', '__init__', 1, 2, 1).
python_method('TypeInferenceEngine', 'enrich_function', 1, 3, 4).
python_method('TypeInferenceEngine', 'get_arg_types', 1, 1, 2).
python_method('TypeInferenceEngine', 'get_return_type', 1, 1, 2).
python_method('TypeInferenceEngine', 'get_typed_signature', 1, 5, 4).
python_method('TypeInferenceEngine', 'extract_all_types', 1, 2, 2).
python_method('TypeInferenceEngine', '_extract_from_node', 2, 8, 4).
python_method('TypeInferenceEngine', '_extract_args', 1, 7, 4).
python_method('TypeInferenceEngine', '_annotation_to_str', 1, 6, 6).
python_method('TypeInferenceEngine', '_ann_constant', 1, 1, 1).
python_method('TypeInferenceEngine', '_ann_name', 1, 1, 0).
python_method('TypeInferenceEngine', '_ann_attribute', 1, 2, 1).
python_method('TypeInferenceEngine', '_ann_subscript', 1, 3, 1).
python_method('TypeInferenceEngine', '_ann_tuple', 1, 4, 2).
python_method('TypeInferenceEngine', '_ann_binop', 1, 3, 1).
python_method('TypeInferenceEngine', '_infer_from_name', 1, 9, 4).
python_method('TypeInferenceEngine', '_infer_arg_type', 2, 5, 1).
python_class('code2llm/core/analyzer.py', 'ProjectAnalyzer').
python_method('ProjectAnalyzer', '__init__', 2, 3, 3).
python_method('ProjectAnalyzer', 'analyze_project', 1, 6, 14).
python_method('ProjectAnalyzer', '_resolve_project_path', 1, 3, 5).
python_method('ProjectAnalyzer', '_log_cache_stats', 3, 5, 2).
python_method('ProjectAnalyzer', '_load_from_persistent_cache', 2, 7, 10).
python_method('ProjectAnalyzer', '_run_analysis', 1, 4, 3).
python_method('ProjectAnalyzer', '_store_to_persistent_cache', 3, 9, 4).
python_method('ProjectAnalyzer', '_build_stats', 4, 2, 5).
python_method('ProjectAnalyzer', '_print_summary', 1, 1, 3).
python_method('ProjectAnalyzer', '_post_process', 4, 5, 6).
python_method('ProjectAnalyzer', '_should_collect_file', 4, 3, 3).
python_method('ProjectAnalyzer', '_compute_module_name', 3, 4, 5).
python_method('ProjectAnalyzer', '_collect_files', 1, 10, 14).
python_method('ProjectAnalyzer', '_wrap_tqdm', 3, 4, 1).
python_method('ProjectAnalyzer', '_log_verbose_progress', 2, 4, 1).
python_method('ProjectAnalyzer', '_analyze_parallel', 1, 6, 11).
python_method('ProjectAnalyzer', '_analyze_sequential', 1, 5, 9).
python_method('ProjectAnalyzer', '_merge_results', 2, 8, 5).
python_method('ProjectAnalyzer', '_build_simple_name_map', 1, 3, 2).
python_method('ProjectAnalyzer', '_resolve_call', 4, 5, 1).
python_method('ProjectAnalyzer', '_collect_call_edges', 2, 4, 4).
python_method('ProjectAnalyzer', '_find_entry_points', 1, 3, 2).
python_method('ProjectAnalyzer', '_build_call_graph', 1, 3, 5).
python_method('ProjectAnalyzer', 'analyze_files', 2, 2, 6).
python_method('ProjectAnalyzer', '_detect_patterns', 1, 8, 6).
python_class('code2llm/core/ast_registry.py', 'ASTRegistry').
python_method('ASTRegistry', '__init__', 0, 1, 0).
python_method('ASTRegistry', 'get_global', 1, 2, 1).
python_method('ASTRegistry', 'reset_global', 1, 1, 0).
python_method('ASTRegistry', 'get_ast', 1, 5, 3).
python_method('ASTRegistry', 'get_source', 1, 4, 4).
python_method('ASTRegistry', 'invalidate', 1, 1, 1).
python_method('ASTRegistry', 'clear', 0, 1, 1).
python_method('ASTRegistry', '__len__', 0, 1, 1).
python_method('ASTRegistry', '__repr__', 0, 1, 1).
python_class('code2llm/core/config.py', 'AnalysisMode').
python_class('code2llm/core/config.py', 'PerformanceConfig').
python_method('PerformanceConfig', 'get_workers', 0, 2, 1).
python_method('PerformanceConfig', 'apply_fast_mode', 0, 2, 0).
python_class('code2llm/core/config.py', 'FilterConfig').
python_class('code2llm/core/config.py', 'DepthConfig').
python_class('code2llm/core/config.py', 'OutputConfig').
python_class('code2llm/core/config.py', 'Config').
python_class('code2llm/core/export_pipeline.py', 'SharedExportContext').
python_method('SharedExportContext', '__init__', 1, 1, 0).
python_method('SharedExportContext', 'result', 0, 1, 0).
python_method('SharedExportContext', 'functions', 0, 1, 0).
python_method('SharedExportContext', 'classes', 0, 1, 0).
python_method('SharedExportContext', 'modules', 0, 1, 0).
python_method('SharedExportContext', 'entry_points', 0, 1, 0).
python_method('SharedExportContext', 'metrics_summary', 0, 2, 1).
python_method('SharedExportContext', 'complexity_distribution', 0, 2, 1).
python_method('SharedExportContext', 'call_graph_edges', 0, 4, 2).
python_method('SharedExportContext', 'high_complexity_functions', 0, 5, 4).
python_method('SharedExportContext', '_compute_metrics_summary', 0, 4, 5).
python_method('SharedExportContext', '_compute_cc_distribution', 0, 3, 3).
python_class('code2llm/core/export_pipeline.py', 'ExportPipeline').
python_method('ExportPipeline', '__init__', 1, 1, 1).
python_method('ExportPipeline', 'context', 0, 1, 0).
python_method('ExportPipeline', 'run', 2, 4, 4).
python_class('code2llm/core/file_analyzer.py', 'FileAnalyzer').
python_method('FileAnalyzer', '__init__', 2, 1, 1).
python_method('FileAnalyzer', '_route_to_language_analyzer', 4, 10, 10).
python_method('FileAnalyzer', '_cache_get', 1, 5, 1).
python_method('FileAnalyzer', '_cache_put', 2, 4, 1).
python_method('FileAnalyzer', 'analyze_file', 2, 7, 11).
python_method('FileAnalyzer', '_analyze_python', 3, 2, 2).
python_method('FileAnalyzer', '_analyze_ast', 4, 5, 7).
python_method('FileAnalyzer', '_calculate_complexity', 3, 8, 4).
python_method('FileAnalyzer', '_perform_deep_analysis', 4, 7, 8).
python_method('FileAnalyzer', '_process_class', 4, 5, 6).
python_method('FileAnalyzer', '_extract_func_calls', 2, 4, 4).
python_method('FileAnalyzer', '_process_function', 5, 9, 11).
python_method('FileAnalyzer', '_build_cfg', 4, 1, 4).
python_method('FileAnalyzer', '_process_cfg_block', 8, 7, 6).
python_method('FileAnalyzer', '_process_if_stmt', 8, 3, 4).
python_method('FileAnalyzer', '_process_loop_stmt', 7, 2, 6).
python_method('FileAnalyzer', '_process_return_stmt', 6, 1, 3).
python_method('FileAnalyzer', '_get_base_name', 1, 3, 3).
python_method('FileAnalyzer', '_get_decorator_name', 1, 4, 1).
python_method('FileAnalyzer', '_get_call_name', 1, 3, 2).
python_class('code2llm/core/file_cache.py', 'FileCache').
python_method('FileCache', '__init__', 2, 1, 2).
python_method('FileCache', '_get_cache_key_stat', 1, 2, 2).
python_method('FileCache', '_get_cache_key', 2, 1, 1).
python_method('FileCache', '_get_cache_path', 1, 1, 0).
python_method('FileCache', 'get', 2, 4, 8).
python_method('FileCache', 'put', 3, 2, 4).
python_method('FileCache', 'get_fast', 1, 5, 8).
python_method('FileCache', 'put_fast', 2, 2, 4).
python_method('FileCache', 'clear', 0, 2, 2).
python_class('code2llm/core/file_filter.py', 'FastFileFilter').
python_method('FastFileFilter', '__init__', 2, 9, 6).
python_method('FastFileFilter', 'should_skip_dir', 1, 2, 2).
python_method('FastFileFilter', '_passes_gitignore', 1, 3, 2).
python_method('FastFileFilter', '_passes_excludes', 2, 6, 1).
python_method('FastFileFilter', '_passes_includes', 1, 6, 2).
python_method('FastFileFilter', 'should_process', 1, 4, 6).
python_method('FastFileFilter', '_passes_line_count', 1, 1, 0).
python_method('FastFileFilter', '_passes_visibility', 3, 7, 0).
python_method('FastFileFilter', 'should_skip_function', 4, 2, 2).
python_class('code2llm/core/gitignore.py', '_GitIgnoreEntry').
python_method('_GitIgnoreEntry', '__init__', 3, 3, 0).
python_class('code2llm/core/gitignore.py', 'GitIgnoreParser').
python_method('GitIgnoreParser', '__init__', 1, 3, 2).
python_method('GitIgnoreParser', '_load_gitignore', 1, 7, 5).
python_method('GitIgnoreParser', '_parse_entry', 1, 5, 5).
python_method('GitIgnoreParser', '_pattern_to_regex', 2, 3, 7).
python_method('GitIgnoreParser', 'is_ignored', 2, 4, 4).
python_class('code2llm/core/incremental.py', 'IncrementalAnalyzer').
python_method('IncrementalAnalyzer', '__init__', 1, 1, 3).
python_method('IncrementalAnalyzer', 'needs_analysis', 1, 2, 3).
python_method('IncrementalAnalyzer', 'get_cached_result', 1, 2, 2).
python_method('IncrementalAnalyzer', 'update', 2, 1, 2).
python_method('IncrementalAnalyzer', 'invalidate', 1, 2, 1).
python_method('IncrementalAnalyzer', 'save', 0, 3, 7).
python_method('IncrementalAnalyzer', 'clear', 0, 3, 3).
python_method('IncrementalAnalyzer', 'cached_count', 0, 1, 1).
python_method('IncrementalAnalyzer', '_load_cache', 0, 4, 5).
python_method('IncrementalAnalyzer', '_normalize_key', 1, 2, 4).
python_class('code2llm/core/lang/__init__.py', 'LanguageParser').
python_method('LanguageParser', 'analyze', 4, 1, 0).
python_method('LanguageParser', 'can_parse', 1, 1, 2).
python_class('code2llm/core/lang/ruby.py', 'RubyParser').
python_method('RubyParser', 'analyze', 4, 1, 1).
python_class('code2llm/core/lang/ts_parser.py', 'TreeSitterParser').
python_method('TreeSitterParser', '__init__', 0, 1, 1).
python_method('TreeSitterParser', 'available', 0, 1, 0).
python_method('TreeSitterParser', 'parse', 2, 3, 3).
python_method('TreeSitterParser', 'supports', 1, 2, 1).
python_class('code2llm/core/large_repo.py', 'SubProject').
python_method('SubProject', 'estimated_size_kb', 0, 1, 2).
python_method('SubProject', 'file_count', 0, 1, 1).
python_class('code2llm/core/large_repo.py', 'HierarchicalRepoSplitter').
python_method('HierarchicalRepoSplitter', '__init__', 2, 1, 0).
python_method('HierarchicalRepoSplitter', 'get_analysis_plan', 1, 2, 4).
python_method('HierarchicalRepoSplitter', '_split_hierarchically', 1, 8, 11).
python_method('HierarchicalRepoSplitter', '_merge_small_l1_dirs', 2, 7, 10).
python_method('HierarchicalRepoSplitter', '_split_level2_consolidated', 3, 9, 9).
python_method('HierarchicalRepoSplitter', '_categorize_subdirs', 2, 7, 8).
python_method('HierarchicalRepoSplitter', '_process_large_dirs', 3, 2, 2).
python_method('HierarchicalRepoSplitter', '_process_level1_files', 2, 5, 11).
python_method('HierarchicalRepoSplitter', '_merge_small_dirs', 3, 7, 9).
python_method('HierarchicalRepoSplitter', '_chunk_by_files', 5, 2, 5).
python_method('HierarchicalRepoSplitter', '_collect_files_in_dir', 2, 1, 1).
python_method('HierarchicalRepoSplitter', '_collect_files_recursive', 2, 1, 1).
python_method('HierarchicalRepoSplitter', '_collect_root_files', 1, 1, 1).
python_method('HierarchicalRepoSplitter', '_count_py_files', 1, 1, 1).
python_method('HierarchicalRepoSplitter', '_contains_python_files', 1, 1, 1).
python_method('HierarchicalRepoSplitter', '_should_skip_file', 1, 1, 1).
python_method('HierarchicalRepoSplitter', '_calculate_priority', 2, 1, 1).
python_method('HierarchicalRepoSplitter', '_get_level1_dirs', 1, 1, 1).
python_class('code2llm/core/models.py', 'BaseModel').
python_method('BaseModel', 'to_dict', 1, 2, 2).
python_method('BaseModel', '_filter_compact', 1, 8, 4).
python_class('code2llm/core/models.py', 'FlowNode').
python_class('code2llm/core/models.py', 'FlowEdge').
python_class('code2llm/core/models.py', 'FunctionInfo').
python_class('code2llm/core/models.py', 'ClassInfo').
python_class('code2llm/core/models.py', 'ModuleInfo').
python_class('code2llm/core/models.py', 'Pattern').
python_class('code2llm/core/models.py', 'CodeSmell').
python_class('code2llm/core/models.py', 'Mutation').
python_class('code2llm/core/models.py', 'DataFlow').
python_class('code2llm/core/models.py', 'AnalysisResult').
python_method('AnalysisResult', 'get_function_count', 0, 1, 1).
python_method('AnalysisResult', 'get_class_count', 0, 1, 1).
python_method('AnalysisResult', 'get_node_count', 0, 1, 1).
python_method('AnalysisResult', 'get_edge_count', 0, 1, 1).
python_class('code2llm/core/persistent_cache.py', 'PersistentCache').
python_method('PersistentCache', '__init__', 4, 7, 11).
python_method('PersistentCache', 'content_hash', 1, 1, 4).
python_method('PersistentCache', 'get_file_result', 1, 4, 5).
python_method('PersistentCache', 'put_file_result', 2, 3, 7).
python_method('PersistentCache', 'get_changed_files', 1, 7, 5).
python_method('PersistentCache', 'prune_missing', 1, 6, 2).
python_method('PersistentCache', 'get_export_cache_dir', 1, 4, 3).
python_method('PersistentCache', 'create_export_cache_dir', 1, 1, 2).
python_method('PersistentCache', 'mark_export_complete', 1, 1, 3).
python_method('PersistentCache', 'save', 0, 5, 11).
python_method('PersistentCache', 'cache_size_mb', 0, 4, 4).
python_method('PersistentCache', '_cleanup_stale_exports', 1, 7, 8).
python_method('PersistentCache', '_cleanup_orphaned_files', 2, 7, 6).
python_method('PersistentCache', 'auto_cleanup', 1, 4, 6).
python_method('PersistentCache', 'gc', 2, 10, 10).
python_method('PersistentCache', 'clear', 0, 1, 2).
python_method('PersistentCache', '_load_manifest', 0, 4, 4).
python_method('PersistentCache', '_compute_run_hash', 1, 1, 4).
python_class('code2llm/core/refactoring.py', 'RefactoringAnalyzer').
python_method('RefactoringAnalyzer', '__init__', 2, 1, 0).
python_method('RefactoringAnalyzer', 'perform_refactoring_analysis', 1, 8, 11).
python_method('RefactoringAnalyzer', '_build_call_graph', 1, 3, 4).
python_method('RefactoringAnalyzer', '_calculate_centrality', 2, 9, 6).
python_method('RefactoringAnalyzer', '_detect_cycles', 2, 6, 5).
python_method('RefactoringAnalyzer', '_detect_communities', 2, 7, 7).
python_method('RefactoringAnalyzer', '_analyze_coupling', 1, 1, 2).
python_method('RefactoringAnalyzer', '_detect_smells', 1, 1, 2).
python_method('RefactoringAnalyzer', '_detect_dead_code', 1, 8, 12).
python_method('RefactoringAnalyzer', '_map_dead_code_to_items', 2, 9, 5).
python_method('RefactoringAnalyzer', '_mark_reachable_items', 1, 5, 1).
python_class('code2llm/core/streaming/cache.py', 'StreamingFileCache').
python_method('StreamingFileCache', '__init__', 2, 1, 2).
python_method('StreamingFileCache', '_get_cache_key', 2, 1, 1).
python_method('StreamingFileCache', '_evict_if_needed', 0, 4, 2).
python_method('StreamingFileCache', 'get', 2, 3, 3).
python_method('StreamingFileCache', 'put', 3, 1, 3).
python_class('code2llm/core/streaming/incremental.py', 'StreamingIncrementalAnalyzer').
python_method('StreamingIncrementalAnalyzer', '__init__', 1, 2, 2).
python_method('StreamingIncrementalAnalyzer', '_load_state', 0, 3, 4).
python_method('StreamingIncrementalAnalyzer', '_save_state', 1, 1, 3).
python_method('StreamingIncrementalAnalyzer', 'get_changed_files', 1, 5, 8).
python_method('StreamingIncrementalAnalyzer', '_get_module_name', 2, 3, 3).
python_class('code2llm/core/streaming/prioritizer.py', 'FilePriority').
python_class('code2llm/core/streaming/prioritizer.py', 'SmartPrioritizer').
python_method('SmartPrioritizer', '__init__', 1, 1, 0).
python_method('SmartPrioritizer', 'prioritize_files', 2, 9, 12).
python_method('SmartPrioritizer', '_build_import_graph', 1, 8, 8).
python_method('SmartPrioritizer', '_check_has_main', 1, 3, 2).
python_class('code2llm/core/streaming/scanner.py', 'StreamingScanner').
python_method('StreamingScanner', '__init__', 2, 1, 0).
python_method('StreamingScanner', '_parse_tree', 2, 5, 3).
python_method('StreamingScanner', '_scan_ast_nodes', 3, 9, 7).
python_method('StreamingScanner', 'quick_scan_file', 1, 3, 8).
python_method('StreamingScanner', 'deep_analyze_file', 1, 5, 4).
python_method('StreamingScanner', 'build_call_graph_streaming', 1, 8, 5).
python_method('StreamingScanner', 'select_important_files', 2, 8, 3).
python_method('StreamingScanner', 'collect_files', 1, 10, 9).
python_class('code2llm/core/streaming/strategies.py', 'ScanStrategy').
python_class('code2llm/core/streaming_analyzer.py', 'StreamingAnalyzer').
python_method('StreamingAnalyzer', '__init__', 2, 4, 3).
python_method('StreamingAnalyzer', 'set_progress_callback', 1, 1, 0).
python_method('StreamingAnalyzer', 'cancel', 0, 1, 0).
python_method('StreamingAnalyzer', '_phase_quick_scan', 4, 4, 6).
python_method('StreamingAnalyzer', '_phase_deep_scan', 2, 4, 4).
python_method('StreamingAnalyzer', 'analyze_streaming', 2, 8, 12).
python_method('StreamingAnalyzer', '_estimate_eta', 3, 3, 1).
python_method('StreamingAnalyzer', '_report_progress', 4, 3, 1).
python_class('code2llm/exporters/article_view.py', 'ArticleViewGenerator').
python_method('ArticleViewGenerator', '_render', 1, 1, 9).
python_method('ArticleViewGenerator', '_render_frontmatter', 1, 1, 3).
python_method('ArticleViewGenerator', '_render_health_summary', 2, 5, 1).
python_method('ArticleViewGenerator', '_render_alerts', 1, 3, 2).
python_method('ArticleViewGenerator', '_render_hotspots', 1, 3, 2).
python_method('ArticleViewGenerator', '_render_roadmap', 1, 3, 3).
python_method('ArticleViewGenerator', '_render_evolution', 1, 7, 4).
python_method('ArticleViewGenerator', '_render_footer', 0, 1, 2).
python_class('code2llm/exporters/base.py', 'BaseExporter').
python_method('BaseExporter', 'export', 2, 1, 0).
python_method('BaseExporter', 'generate', 2, 1, 1).
python_method('BaseExporter', '_ensure_dir', 1, 1, 2).
python_method('BaseExporter', '_write_text', 2, 1, 2).
python_class('code2llm/exporters/base.py', 'ViewGeneratorMixin').
python_method('ViewGeneratorMixin', 'generate', 2, 1, 6).
python_class('code2llm/exporters/context_exporter.py', 'ContextExporter').
python_method('ContextExporter', 'export', 2, 1, 15).
python_method('ContextExporter', '_get_overview', 1, 3, 3).
python_method('ContextExporter', '_detect_languages', 1, 7, 9).
python_method('ContextExporter', '_get_architecture_by_module', 1, 7, 5).
python_method('ContextExporter', '_get_important_entries', 1, 3, 4).
python_method('ContextExporter', '_get_key_entry_points', 1, 4, 2).
python_method('ContextExporter', '_get_process_flows', 2, 6, 5).
python_method('ContextExporter', '_get_key_classes', 1, 6, 5).
python_method('ContextExporter', '_get_data_transformations', 1, 7, 5).
python_method('ContextExporter', '_get_behavioral_patterns', 1, 4, 2).
python_method('ContextExporter', '_get_api_surface', 1, 5, 5).
python_method('ContextExporter', '_get_system_interactions', 1, 5, 6).
python_method('ContextExporter', '_group_calls_by_module', 2, 5, 2).
python_method('ContextExporter', '_format_sub_flow', 3, 3, 2).
python_method('ContextExporter', '_trace_flow', 5, 10, 13).
python_class('code2llm/exporters/context_view.py', 'ContextViewGenerator').
python_method('ContextViewGenerator', '_render', 1, 1, 8).
python_method('ContextViewGenerator', '_render_overview', 2, 1, 1).
python_method('ContextViewGenerator', '_render_architecture', 1, 9, 8).
python_method('ContextViewGenerator', '_render_class_export_entry', 2, 6, 2).
python_method('ContextViewGenerator', '_render_exports', 1, 6, 3).
python_method('ContextViewGenerator', '_render_hotspots', 1, 3, 2).
python_method('ContextViewGenerator', '_render_refactoring', 1, 3, 3).
python_method('ContextViewGenerator', '_render_guidelines', 0, 1, 0).
python_class('code2llm/exporters/dashboard_data.py', 'DashboardDataBuilder').
python_method('DashboardDataBuilder', 'health_verdict', 1, 3, 1).
python_method('DashboardDataBuilder', 'build_evolution_section', 1, 4, 2).
python_method('DashboardDataBuilder', 'build_language_breakdown', 1, 7, 8).
python_method('DashboardDataBuilder', 'build_module_lines_chart', 1, 3, 3).
python_method('DashboardDataBuilder', 'build_module_funcs_chart', 1, 3, 3).
python_method('DashboardDataBuilder', 'build_top_modules_html', 1, 3, 6).
python_method('DashboardDataBuilder', 'build_alerts_html', 1, 3, 1).
python_method('DashboardDataBuilder', 'build_hotspots_html', 1, 2, 1).
python_method('DashboardDataBuilder', 'build_refactoring_html', 1, 2, 2).
python_class('code2llm/exporters/dashboard_renderer.py', 'DashboardRenderer').
python_method('DashboardRenderer', 'render', 17, 2, 5).
python_method('DashboardRenderer', '_assemble_html', 0, 5, 4).
python_method('DashboardRenderer', '_render_evolution_section', 1, 6, 3).
python_method('DashboardRenderer', '_render_evolution_script', 1, 2, 0).
python_class('code2llm/exporters/evolution_exporter.py', 'EvolutionExporter').
python_method('EvolutionExporter', '_is_excluded', 1, 1, 1).
python_method('EvolutionExporter', 'export', 2, 1, 13).
python_method('EvolutionExporter', 'export_to_yaml', 2, 1, 1).
python_class('code2llm/exporters/flow_exporter.py', 'FlowExporter').
python_method('FlowExporter', '__init__', 0, 1, 4).
python_method('FlowExporter', 'export', 2, 1, 13).
python_method('FlowExporter', '_build_context', 1, 4, 12).
python_method('FlowExporter', '_pipeline_to_dict', 1, 3, 1).
python_method('FlowExporter', '_compute_transforms', 1, 3, 7).
python_method('FlowExporter', '_transform_label', 2, 6, 0).
python_method('FlowExporter', '_compute_type_usage', 2, 9, 9).
python_method('FlowExporter', '_normalize_type', 1, 6, 4).
python_method('FlowExporter', '_type_label', 3, 9, 0).
python_method('FlowExporter', '_classify_side_effects', 2, 7, 3).
python_method('FlowExporter', '_compute_contracts', 4, 4, 3).
python_method('FlowExporter', '_build_stage_contract', 4, 9, 4).
python_method('FlowExporter', '_infer_invariant', 2, 10, 2).
python_method('FlowExporter', '_is_excluded', 1, 1, 1).
python_class('code2llm/exporters/flow_renderer.py', 'FlowRenderer').
python_method('FlowRenderer', 'render_header', 1, 4, 3).
python_method('FlowRenderer', 'render_pipelines', 1, 10, 8).
python_method('FlowRenderer', 'render_transforms', 1, 3, 1).
python_method('FlowRenderer', 'render_contracts', 1, 7, 2).
python_method('FlowRenderer', '_render_hub_types', 2, 4, 2).
python_method('FlowRenderer', '_count_type_sources', 1, 5, 3).
python_method('FlowRenderer', '_render_type_rows', 2, 3, 1).
python_method('FlowRenderer', 'render_data_types', 1, 5, 5).
python_method('FlowRenderer', 'render_side_effects', 1, 6, 4).
python_class('code2llm/exporters/html_dashboard.py', 'HTMLDashboardGenerator').
python_method('HTMLDashboardGenerator', '__init__', 0, 1, 2).
python_method('HTMLDashboardGenerator', 'generate', 2, 1, 5).
python_method('HTMLDashboardGenerator', '_render', 1, 1, 11).
python_class('code2llm/exporters/index_generator/__init__.py', 'IndexHTMLGenerator').
python_method('IndexHTMLGenerator', '__init__', 1, 1, 4).
python_method('IndexHTMLGenerator', 'generate', 0, 1, 4).
python_method('IndexHTMLGenerator', 'scan_files', 0, 1, 1).
python_method('IndexHTMLGenerator', 'render_html', 1, 1, 1).
python_class('code2llm/exporters/index_generator/renderer.py', 'HTMLRenderer').
python_method('HTMLRenderer', 'render', 1, 1, 2).
python_class('code2llm/exporters/index_generator/scanner.py', 'FileScanner').
python_method('FileScanner', '__init__', 1, 1, 1).
python_method('FileScanner', 'scan', 0, 5, 13).
python_method('FileScanner', '_read_file_content', 2, 5, 4).
python_method('FileScanner', '_escape_html', 1, 1, 1).
python_method('FileScanner', '_format_size', 1, 3, 0).
python_class('code2llm/exporters/json_exporter.py', 'JSONExporter').
python_method('JSONExporter', 'export', 4, 3, 4).
python_class('code2llm/exporters/map_exporter.py', 'MapExporter').
python_method('MapExporter', 'export', 2, 1, 8).
python_method('MapExporter', 'export_to_yaml', 2, 1, 1).
python_class('code2llm/exporters/mermaid_exporter.py', 'MermaidExporter').
python_class('code2llm/exporters/planfile_tickets.py', 'PlanfileTicketSuggestion').
python_method('PlanfileTicketSuggestion', 'to_dict', 0, 1, 1).
python_class('code2llm/exporters/planfile_tickets.py', 'PlanfileTicketsExporter').
python_method('PlanfileTicketsExporter', 'export', 2, 6, 10).
python_class('code2llm/exporters/project_yaml/core.py', 'ProjectYAMLExporter').
python_method('ProjectYAMLExporter', 'export', 2, 1, 6).
python_method('ProjectYAMLExporter', '_build_project_stats', 2, 8, 4).
python_method('ProjectYAMLExporter', '_build_project_yaml', 2, 5, 15).
python_method('ProjectYAMLExporter', '_detect_primary_language', 1, 9, 10).
python_class('code2llm/exporters/readme_exporter.py', 'READMEExporter').
python_method('READMEExporter', 'export', 2, 5, 12).
python_class('code2llm/exporters/toon/__init__.py', 'ToonExporter').
python_method('ToonExporter', '__init__', 0, 1, 2).
python_method('ToonExporter', 'export', 2, 1, 14).
python_method('ToonExporter', 'export_to_yaml', 2, 1, 13).
python_method('ToonExporter', '_build_header_dict', 1, 6, 4).
python_method('ToonExporter', '_build_health_dict', 1, 3, 1).
python_method('ToonExporter', '_build_refactor_dict', 1, 9, 4).
python_method('ToonExporter', '_build_pipelines_dict', 1, 2, 2).
python_method('ToonExporter', '_build_layers_dict', 1, 2, 2).
python_method('ToonExporter', '_build_coupling_dict', 1, 2, 2).
python_method('ToonExporter', '_build_external_dict', 1, 2, 2).
python_method('ToonExporter', '_is_excluded', 1, 1, 1).
python_class('code2llm/exporters/toon/metrics.py', 'MetricsComputer').
python_method('MetricsComputer', '__init__', 0, 1, 0).
python_method('MetricsComputer', 'compute_all_metrics', 1, 1, 15).
python_method('MetricsComputer', '_compute_hotspots', 1, 5, 7).
python_method('MetricsComputer', '_get_cycles', 1, 1, 1).
python_class('code2llm/exporters/toon/metrics_core.py', 'CoreMetricsComputer').
python_method('CoreMetricsComputer', '__init__', 2, 1, 0).
python_method('CoreMetricsComputer', '_ensure_file_record', 3, 2, 3).
python_method('CoreMetricsComputer', 'compute_file_metrics', 1, 9, 9).
python_method('CoreMetricsComputer', '_new_file_record', 2, 1, 1).
python_method('CoreMetricsComputer', '_build_suffix_index', 1, 2, 4).
python_method('CoreMetricsComputer', '_update_importers_from_called_by', 4, 4, 2).
python_method('CoreMetricsComputer', '_update_importers_from_calls', 5, 7, 2).
python_method('CoreMetricsComputer', '_compute_fan_in', 2, 3, 8).
python_method('CoreMetricsComputer', 'compute_package_metrics', 2, 5, 7).
python_method('CoreMetricsComputer', 'compute_function_metrics', 1, 8, 10).
python_method('CoreMetricsComputer', 'compute_class_metrics', 1, 7, 10).
python_method('CoreMetricsComputer', 'compute_coupling_matrix', 1, 1, 4).
python_method('CoreMetricsComputer', '_build_function_to_module_map', 1, 3, 2).
python_method('CoreMetricsComputer', '_build_coupling_matrix', 2, 9, 7).
python_method('CoreMetricsComputer', '_resolve_callee_module', 4, 6, 3).
python_method('CoreMetricsComputer', '_compute_package_fan', 1, 7, 4).
python_class('code2llm/exporters/toon/metrics_duplicates.py', 'DuplicatesMetricsComputer').
python_method('DuplicatesMetricsComputer', '__init__', 1, 1, 0).
python_method('DuplicatesMetricsComputer', 'detect_duplicates', 1, 4, 5).
python_method('DuplicatesMetricsComputer', '_check_class_for_duplicates', 5, 8, 5).
python_method('DuplicatesMetricsComputer', '_calculate_duplicate_info', 7, 6, 4).
python_class('code2llm/exporters/toon/metrics_health.py', 'HealthMetricsComputer').
python_method('HealthMetricsComputer', '__init__', 0, 1, 0).
python_method('HealthMetricsComputer', 'compute_health', 1, 1, 6).
python_method('HealthMetricsComputer', '_check_duplicates_health', 2, 4, 4).
python_method('HealthMetricsComputer', '_check_god_modules_health', 2, 4, 2).
python_method('HealthMetricsComputer', '_check_smells_health', 2, 7, 3).
python_method('HealthMetricsComputer', '_check_high_cc_health', 2, 7, 1).
python_class('code2llm/exporters/toon/module_detail.py', 'ModuleDetailRenderer').
python_method('ModuleDetailRenderer', 'render_details', 1, 3, 2).
python_method('ModuleDetailRenderer', '_rank_modules_by_cc', 1, 4, 5).
python_method('ModuleDetailRenderer', '_render_module_detail', 4, 3, 7).
python_method('ModuleDetailRenderer', '_get_module_exports', 2, 6, 2).
python_method('ModuleDetailRenderer', '_render_module_classes', 4, 6, 5).
python_method('ModuleDetailRenderer', '_get_method_items', 2, 4, 3).
python_method('ModuleDetailRenderer', '_find_root_method', 1, 5, 0).
python_method('ModuleDetailRenderer', '_render_standalone_funcs', 3, 7, 3).
python_method('ModuleDetailRenderer', '_render_call_chain', 5, 2, 7).
python_class('code2llm/exporters/toon/renderer.py', 'ToonRenderer').
python_method('ToonRenderer', 'render_header', 1, 6, 5).
python_method('ToonRenderer', 'render_health', 1, 1, 1).
python_method('ToonRenderer', 'render_refactor', 1, 1, 1).
python_method('ToonRenderer', 'render_coupling', 1, 3, 4).
python_method('ToonRenderer', '_render_coupling_rows', 4, 4, 6).
python_method('ToonRenderer', 'render_layers', 1, 2, 8).
python_method('ToonRenderer', '_render_layer_files', 4, 6, 5).
python_method('ToonRenderer', 'render_duplicates', 1, 6, 4).
python_method('ToonRenderer', 'render_functions', 1, 6, 4).
python_method('ToonRenderer', 'render_hotspots', 1, 1, 1).
python_method('ToonRenderer', 'render_classes', 1, 1, 1).
python_method('ToonRenderer', 'render_pipelines', 1, 1, 1).
python_method('ToonRenderer', 'render_external', 1, 1, 1).
python_class('code2llm/exporters/toon_view.py', 'ToonViewGenerator').
python_method('ToonViewGenerator', '_render', 1, 1, 9).
python_method('ToonViewGenerator', '_render_header', 1, 1, 1).
python_method('ToonViewGenerator', '_render_health', 1, 1, 1).
python_method('ToonViewGenerator', '_render_alerts', 1, 5, 3).
python_method('ToonViewGenerator', '_render_modules', 1, 6, 10).
python_method('ToonViewGenerator', '_render_hotspots', 1, 3, 3).
python_method('ToonViewGenerator', '_render_refactoring', 1, 3, 5).
python_method('ToonViewGenerator', '_render_evolution', 1, 3, 2).
python_class('code2llm/exporters/yaml_exporter.py', 'YAMLExporter').
python_method('YAMLExporter', '__init__', 0, 1, 1).
python_method('YAMLExporter', '_get_name_index', 1, 3, 3).
python_method('YAMLExporter', 'export', 4, 2, 4).
python_method('YAMLExporter', 'export_grouped', 2, 8, 12).
python_method('YAMLExporter', 'export_data_flow', 3, 1, 6).
python_method('YAMLExporter', 'export_data_structures', 3, 1, 6).
python_method('YAMLExporter', 'export_separated', 3, 4, 6).
python_method('YAMLExporter', 'export_split', 3, 5, 8).
python_method('YAMLExporter', 'export_calls', 4, 1, 8).
python_method('YAMLExporter', '_collect_edges', 3, 3, 4).
python_method('YAMLExporter', '_process_function_calls', 8, 4, 6).
python_method('YAMLExporter', '_should_add_edge', 3, 3, 0).
python_method('YAMLExporter', '_create_edge', 3, 2, 1).
python_method('YAMLExporter', '_build_nodes', 2, 3, 3).
python_method('YAMLExporter', '_create_node', 3, 1, 2).
python_method('YAMLExporter', '_compute_calls_in_counts', 1, 7, 5).
python_method('YAMLExporter', '_group_by_module', 2, 4, 5).
python_method('YAMLExporter', '_build_calls_data', 4, 2, 2).
python_method('YAMLExporter', '_resolve_callee', 2, 3, 3).
python_method('YAMLExporter', '_get_cc', 1, 3, 2).
python_method('YAMLExporter', 'export_calls_toon', 4, 1, 14).
python_method('YAMLExporter', '_render_calls_header', 4, 3, 5).
python_method('YAMLExporter', '_render_hubs', 1, 3, 3).
python_method('YAMLExporter', '_render_modules', 3, 4, 4).
python_method('YAMLExporter', '_render_edges', 1, 2, 1).
python_class('code2llm/generators/llm_flow/analysis.py', 'FuncSummary').
python_class('code2llm/nlp/config.py', 'NormalizationConfig').
python_class('code2llm/nlp/config.py', 'IntentMatchingConfig').
python_class('code2llm/nlp/config.py', 'EntityResolutionConfig').
python_class('code2llm/nlp/config.py', 'MultilingualConfig').
python_class('code2llm/nlp/config.py', 'NLPConfig').
python_method('NLPConfig', 'from_yaml', 2, 1, 8).
python_method('NLPConfig', 'to_yaml', 1, 1, 4).
python_class('code2llm/nlp/entity_resolution.py', 'Entity').
python_class('code2llm/nlp/entity_resolution.py', 'EntityResolutionResult').
python_method('EntityResolutionResult', 'get_by_type', 1, 3, 0).
python_method('EntityResolutionResult', 'get_best_match', 0, 2, 1).
python_class('code2llm/nlp/entity_resolution.py', 'EntityResolver').
python_method('EntityResolver', '__init__', 2, 3, 1).
python_method('EntityResolver', '_apply_resolution_steps', 2, 5, 3).
python_method('EntityResolver', 'resolve', 3, 9, 6).
python_method('EntityResolver', '_extract_candidates', 2, 3, 6).
python_method('EntityResolver', '_extract_from_patterns', 2, 6, 4).
python_method('EntityResolver', '_disambiguate', 2, 6, 4).
python_method('EntityResolver', '_resolve_hierarchical', 1, 3, 3).
python_method('EntityResolver', '_resolve_aliases', 1, 4, 2).
python_method('EntityResolver', '_name_similarity', 2, 3, 3).
python_method('EntityResolver', 'load_from_analysis', 1, 4, 3).
python_method('EntityResolver', 'step_3a_extract_entities', 2, 1, 1).
python_method('EntityResolver', 'step_3b_match_threshold', 1, 3, 0).
python_method('EntityResolver', 'step_3c_disambiguate', 2, 1, 1).
python_method('EntityResolver', 'step_3d_hierarchical_resolve', 1, 1, 1).
python_method('EntityResolver', 'step_3e_alias_resolve', 1, 1, 1).
python_class('code2llm/nlp/intent_matching.py', 'IntentMatch').
python_class('code2llm/nlp/intent_matching.py', 'IntentMatchingResult').
python_method('IntentMatchingResult', 'get_best_intent', 0, 2, 0).
python_method('IntentMatchingResult', 'get_confidence', 0, 2, 0).
python_class('code2llm/nlp/intent_matching.py', 'IntentMatcher').
python_method('IntentMatcher', '__init__', 2, 3, 1).
python_method('IntentMatcher', 'match', 2, 2, 6).
python_method('IntentMatcher', '_fuzzy_match', 1, 4, 4).
python_method('IntentMatcher', '_keyword_match', 1, 6, 7).
python_method('IntentMatcher', '_apply_context', 3, 5, 5).
python_method('IntentMatcher', '_combine_matches', 1, 4, 2).
python_method('IntentMatcher', '_resolve_multi_intent', 1, 7, 2).
python_method('IntentMatcher', '_calculate_similarity', 2, 6, 6).
python_method('IntentMatcher', 'step_2a_fuzzy_match', 2, 1, 1).
python_method('IntentMatcher', 'step_2b_semantic_match', 2, 1, 1).
python_method('IntentMatcher', 'step_2c_keyword_match', 2, 2, 4).
python_method('IntentMatcher', 'step_2d_context_score', 2, 3, 4).
python_method('IntentMatcher', 'step_2e_resolve_intents', 1, 1, 1).
python_class('code2llm/nlp/normalization.py', 'NormalizationResult').
python_class('code2llm/nlp/normalization.py', 'QueryNormalizer').
python_method('QueryNormalizer', '__init__', 1, 2, 1).
python_method('QueryNormalizer', 'normalize', 2, 6, 8).
python_method('QueryNormalizer', '_unicode_normalize', 1, 1, 1).
python_method('QueryNormalizer', '_lowercase', 1, 1, 1).
python_method('QueryNormalizer', '_remove_punctuation', 1, 1, 1).
python_method('QueryNormalizer', '_normalize_whitespace', 1, 1, 2).
python_method('QueryNormalizer', '_remove_stopwords', 2, 3, 3).
python_method('QueryNormalizer', '_tokenize', 1, 1, 1).
python_method('QueryNormalizer', 'step_1a_lowercase', 1, 1, 1).
python_method('QueryNormalizer', 'step_1b_remove_punctuation', 1, 1, 1).
python_method('QueryNormalizer', 'step_1c_normalize_whitespace', 1, 1, 2).
python_method('QueryNormalizer', 'step_1d_unicode_normalize', 1, 1, 1).
python_method('QueryNormalizer', 'step_1e_remove_stopwords', 2, 3, 3).
python_class('code2llm/nlp/pipeline.py', 'NlpPipelineStage').
python_class('code2llm/nlp/pipeline.py', 'NLPPipelineResult').
python_method('NLPPipelineResult', 'is_successful', 0, 3, 0).
python_method('NLPPipelineResult', 'get_intent', 0, 2, 0).
python_method('NLPPipelineResult', 'get_entities', 0, 1, 0).
python_method('NLPPipelineResult', 'to_dict', 0, 2, 2).
python_class('code2llm/nlp/pipeline.py', 'NLPPipeline').
python_method('NLPPipeline', '__init__', 1, 2, 3).
python_method('NLPPipeline', 'process', 2, 3, 16).
python_method('NLPPipeline', '_step_normalize', 2, 2, 3).
python_method('NLPPipeline', '_step_match_intent', 1, 3, 2).
python_method('NLPPipeline', '_step_resolve_entities', 3, 2, 2).
python_method('NLPPipeline', '_infer_entity_types', 1, 2, 1).
python_method('NLPPipeline', '_calculate_overall_confidence', 1, 1, 3).
python_method('NLPPipeline', '_calculate_entity_confidence', 1, 3, 1).
python_method('NLPPipeline', '_apply_fallback', 1, 4, 3).
python_method('NLPPipeline', '_format_action', 1, 10, 2).
python_method('NLPPipeline', '_format_response', 1, 5, 3).
python_method('NLPPipeline', 'step_4a_orchestrate', 1, 1, 1).
python_method('NLPPipeline', 'step_4b_aggregate', 1, 1, 0).
python_method('NLPPipeline', 'step_4c_confidence', 1, 1, 1).
python_method('NLPPipeline', 'step_4d_fallback', 1, 1, 1).
python_method('NLPPipeline', 'step_4e_format', 1, 1, 1).
python_class('code2llm/patterns/detector.py', 'PatternDetector').
python_method('PatternDetector', '__init__', 1, 1, 0).
python_method('PatternDetector', 'detect_patterns', 1, 3, 6).
python_method('PatternDetector', '_detect_recursion', 1, 3, 2).
python_method('PatternDetector', '_detect_state_machines', 1, 9, 5).
python_method('PatternDetector', '_detect_factory_pattern', 1, 6, 5).
python_method('PatternDetector', '_detect_singleton', 1, 5, 5).
python_method('PatternDetector', '_detect_strategy_pattern', 1, 9, 6).
python_method('PatternDetector', '_check_returns_classes', 2, 1, 1).
python_class('code2llm/refactor/prompt_engine.py', 'PromptEngine').
python_method('PromptEngine', '__init__', 2, 4, 8).
python_method('PromptEngine', 'generate_prompts', 0, 5, 7).
python_method('PromptEngine', '_generate_prompt_for_smell', 1, 3, 5).
python_method('PromptEngine', '_get_template_for_type', 1, 1, 1).
python_method('PromptEngine', '_get_smell_metrics', 1, 3, 2).
python_method('PromptEngine', '_get_smell_mutations', 1, 4, 5).
python_method('PromptEngine', '_get_target_module', 1, 2, 2).
python_method('PromptEngine', '_get_reachability', 1, 2, 2).
python_method('PromptEngine', '_build_context_for_smell', 1, 5, 11).
python_method('PromptEngine', '_get_source_context', 3, 5, 10).
python_method('PromptEngine', '_get_instruction_for_smell', 1, 5, 1).
python_class('demo_langs/valid/sample.py', 'User').
python_class('demo_langs/valid/sample.py', 'UserService').
python_method('UserService', '__init__', 0, 1, 0).
python_method('UserService', 'add_user', 1, 1, 1).
python_method('UserService', 'get_user', 1, 3, 0).
python_method('UserService', 'process_users', 0, 2, 1).
python_method('UserService', 'list_users', 0, 1, 1).
python_method('UserService', 'remove_user', 1, 3, 1).
python_method('UserService', 'count', 0, 1, 1).
python_class('examples/docker-doql-example/app/main.py', 'CustomHandler').
python_method('CustomHandler', 'do_GET', 0, 2, 6).
python_method('CustomHandler', 'log_message', 1, 1, 2).
python_class('examples/functional_refactoring/cache.py', 'CacheEntry').
python_class('examples/functional_refactoring/cache.py', 'EvolutionaryCache').
python_method('EvolutionaryCache', '__init__', 2, 1, 1).
python_method('EvolutionaryCache', '_load', 0, 5, 5).
python_method('EvolutionaryCache', '_save', 0, 3, 5).
python_method('EvolutionaryCache', 'get', 2, 2, 3).
python_method('EvolutionaryCache', 'put', 3, 3, 6).
python_method('EvolutionaryCache', 'report_success', 2, 2, 3).
python_method('EvolutionaryCache', 'report_failure', 2, 2, 3).
python_method('EvolutionaryCache', '_make_key', 2, 1, 2).
python_method('EvolutionaryCache', '_calculate_score', 1, 3, 2).
python_method('EvolutionaryCache', '_evict_worst', 0, 2, 2).
python_class('examples/functional_refactoring/entity_preparers.py', 'EntityPreparer').
python_method('EntityPreparer', 'supports', 1, 1, 0).
python_method('EntityPreparer', 'prepare', 3, 3, 0).
python_class('examples/functional_refactoring/entity_preparers.py', 'ShellEntityPreparer').
python_method('ShellEntityPreparer', 'supports', 1, 1, 2).
python_method('ShellEntityPreparer', 'prepare', 3, 3, 4).
python_method('ShellEntityPreparer', '_apply_path_defaults', 4, 2, 1).
python_method('ShellEntityPreparer', '_apply_pattern_defaults', 2, 3, 0).
python_method('ShellEntityPreparer', '_apply_find_flags', 3, 5, 2).
python_class('examples/functional_refactoring/entity_preparers.py', 'DockerEntityPreparer').
python_method('DockerEntityPreparer', 'supports', 1, 1, 1).
python_method('DockerEntityPreparer', 'prepare', 3, 3, 3).
python_method('DockerEntityPreparer', '_resolve_container_name', 1, 1, 0).
python_class('examples/functional_refactoring/entity_preparers.py', 'SQLEntityPreparer').
python_method('SQLEntityPreparer', 'supports', 1, 1, 1).
python_method('SQLEntityPreparer', 'prepare', 3, 3, 3).
python_method('SQLEntityPreparer', '_sanitize_identifier', 1, 4, 2).
python_method('SQLEntityPreparer', '_sanitize_columns', 1, 4, 5).
python_class('examples/functional_refactoring/entity_preparers.py', 'KubernetesEntityPreparer').
python_method('KubernetesEntityPreparer', 'supports', 1, 1, 1).
python_method('KubernetesEntityPreparer', 'prepare', 3, 3, 2).
python_class('examples/functional_refactoring/entity_preparers.py', 'EntityPreparationPipeline').
python_method('EntityPreparationPipeline', '__init__', 0, 1, 4).
python_method('EntityPreparationPipeline', 'prepare', 3, 3, 2).
python_class('examples/functional_refactoring/generator.py', 'CommandGenerator').
python_method('CommandGenerator', '__init__', 3, 4, 4).
python_method('CommandGenerator', 'generate', 3, 3, 4).
python_class('examples/functional_refactoring/models.py', 'CommandContext').
python_class('examples/functional_refactoring/models.py', 'CommandResult').
python_class('examples/functional_refactoring/template_engine.py', 'Template').
python_class('examples/functional_refactoring/template_engine.py', 'TemplateLoader').
python_method('TemplateLoader', '__init__', 1, 2, 1).
python_method('TemplateLoader', 'load', 0, 1, 2).
python_method('TemplateLoader', '_load_templates', 0, 3, 6).
python_method('TemplateLoader', '_load_defaults', 0, 2, 3).
python_method('TemplateLoader', 'get_template', 1, 1, 1).
python_method('TemplateLoader', 'get_default', 2, 1, 1).
python_method('TemplateLoader', 'find_alternative_template', 2, 1, 1).
python_class('examples/functional_refactoring/template_engine.py', 'TemplateRenderer').
python_method('TemplateRenderer', 'render', 2, 2, 3).
python_method('TemplateRenderer', '_manual_render', 2, 3, 3).
python_method('TemplateRenderer', 'render_with_conditionals', 2, 1, 4).
python_class('examples/functional_refactoring_example.py', 'TemplateGenerator').
python_method('TemplateGenerator', '__init__', 0, 1, 2).
python_method('TemplateGenerator', 'generate', 3, 4, 6).
python_method('TemplateGenerator', '_load_templates_from_json', 0, 1, 0).
python_method('TemplateGenerator', '_load_defaults_from_json', 0, 1, 0).
python_method('TemplateGenerator', '_prepare_shell_entities', 0, 1, 0).
python_method('TemplateGenerator', '_prepare_docker_entities', 0, 1, 0).
python_method('TemplateGenerator', '_prepare_sql_entities', 0, 1, 0).
python_method('TemplateGenerator', '_find_alternative_template', 0, 1, 0).
python_method('TemplateGenerator', '_render_template', 0, 1, 0).
python_class('examples/streaming-analyzer/sample_project/api.py', 'APIHandler').
python_method('APIHandler', '__init__', 0, 1, 1).
python_method('APIHandler', 'process_request', 1, 5, 4).
python_method('APIHandler', '_check_rate_limit', 1, 2, 2).
python_method('APIHandler', '_get_stats', 0, 1, 1).
python_method('APIHandler', '_get_user_info', 1, 2, 1).
python_method('APIHandler', '_health_check', 0, 1, 0).
python_method('APIHandler', 'format_response', 1, 1, 1).
python_class('examples/streaming-analyzer/sample_project/auth.py', 'AuthManager').
python_method('AuthManager', '__init__', 0, 1, 1).
python_method('AuthManager', '_hash', 1, 1, 4).
python_method('AuthManager', 'authenticate', 2, 3, 1).
python_method('AuthManager', '_verify_password', 2, 2, 1).
python_method('AuthManager', 'create_session', 1, 1, 1).
python_method('AuthManager', 'validate_session', 1, 1, 1).
python_method('AuthManager', 'revoke_session', 1, 2, 0).
python_method('AuthManager', 'get_user_role', 1, 2, 1).
python_method('AuthManager', 'has_permission', 3, 1, 2).
python_method('AuthManager', 'list_active_sessions', 0, 2, 3).
python_class('examples/streaming-analyzer/sample_project/database.py', 'DatabaseConnection').
python_method('DatabaseConnection', '__init__', 1, 2, 2).
python_method('DatabaseConnection', '_load_data', 0, 3, 3).
python_method('DatabaseConnection', '_save_data', 0, 2, 2).
python_method('DatabaseConnection', 'get_user', 1, 1, 1).
python_method('DatabaseConnection', 'get_user_settings', 1, 2, 2).
python_method('DatabaseConnection', 'get_user_logs', 1, 3, 1).
python_method('DatabaseConnection', 'update_user_settings', 2, 2, 4).
python_method('DatabaseConnection', 'update_user_profile', 2, 4, 3).
python_method('DatabaseConnection', 'delete_user', 1, 2, 2).
python_method('DatabaseConnection', 'clear_user_data', 1, 2, 3).
python_method('DatabaseConnection', 'create_user', 1, 1, 5).
python_method('DatabaseConnection', '_log_action', 3, 5, 4).
python_method('DatabaseConnection', 'get_stats', 0, 1, 3).
python_class('examples/streaming-analyzer/sample_project/main.py', 'UserRequest').
python_class('examples/streaming-analyzer/sample_project/main.py', 'Application').
python_method('Application', '__init__', 0, 1, 3).
python_method('Application', 'start', 0, 4, 3).
python_method('Application', 'get_next_request', 0, 3, 2).
python_method('Application', 'process_request', 1, 6, 8).
python_method('Application', 'handle_get_request', 1, 4, 6).
python_method('Application', 'handle_set_request', 1, 4, 4).
python_method('Application', 'handle_delete_request', 1, 4, 4).
python_method('Application', 'handle_default_request', 1, 2, 2).
python_class('test_langs/valid/sample.py', 'Product').
python_class('test_langs/valid/sample.py', 'ProductRepository').
python_method('ProductRepository', '__init__', 0, 1, 0).
python_method('ProductRepository', 'add', 1, 1, 1).
python_method('ProductRepository', 'find_by_id', 1, 3, 0).
python_method('ProductRepository', 'list_all', 0, 1, 1).
python_class('test_python_only/valid/sample.py', 'User').
python_class('test_python_only/valid/sample.py', 'UserService').
python_method('UserService', '__init__', 0, 1, 0).
python_method('UserService', 'add_user', 1, 1, 1).
python_method('UserService', 'get_user', 1, 3, 0).
python_method('UserService', 'process_users', 0, 2, 1).
python_class('tests/test_analyzer.py', 'TestProjectAnalyzer').
python_method('TestProjectAnalyzer', 'sample_project', 0, 1, 4).
python_method('TestProjectAnalyzer', 'test_analyze_finds_functions', 1, 4, 5).
python_method('TestProjectAnalyzer', 'test_analyze_finds_classes', 1, 3, 5).
python_method('TestProjectAnalyzer', 'test_detects_recursion', 1, 7, 5).
python_method('TestProjectAnalyzer', 'test_detects_state_machine', 1, 5, 5).
python_method('TestProjectAnalyzer', 'test_caching_works', 1, 2, 4).
python_method('TestProjectAnalyzer', 'test_filtering_skips_tests', 1, 3, 7).
python_class('tests/test_analyzer.py', 'TestConfig').
python_method('TestConfig', 'test_fast_config_limits_depth', 0, 4, 0).
python_method('TestConfig', 'test_fast_config_skips_private', 0, 2, 0).
python_class('tests/test_analyzer.py', 'TestExporters').
python_method('TestExporters', 'sample_result', 0, 1, 2).
python_method('TestExporters', 'test_json_export', 2, 4, 5).
python_method('TestExporters', 'test_mermaid_export', 2, 3, 5).
python_method('TestExporters', 'test_mermaid_export_sanitizes_unsafe_identifiers', 1, 6, 6).
python_class('tests/test_edge_cases.py', 'TestEdgeCases').
python_method('TestEdgeCases', 'test_empty_project', 0, 4, 6).
python_method('TestEdgeCases', 'test_nonexistent_path', 0, 1, 3).
python_method('TestEdgeCases', 'test_syntax_error_file', 0, 2, 7).
python_method('TestEdgeCases', 'test_very_large_file', 0, 3, 12).
python_method('TestEdgeCases', 'test_unicode_filenames', 0, 2, 10).
python_method('TestEdgeCases', 'test_nested_classes', 0, 2, 8).
python_method('TestEdgeCases', 'test_decorators', 0, 2, 10).
python_class('tests/test_edge_cases.py', 'TestFileCache').
python_method('TestFileCache', 'test_cache_hit', 0, 2, 6).
python_method('TestFileCache', 'test_cache_ttl_expiration', 0, 2, 6).
python_method('TestFileCache', 'test_cache_clear', 0, 3, 11).
python_class('tests/test_edge_cases.py', 'TestFiltering').
python_method('TestFiltering', 'test_exclude_tests', 0, 4, 3).
python_method('TestFiltering', 'test_exclude_patterns', 0, 4, 3).
python_method('TestFiltering', 'test_skip_private_methods', 0, 3, 3).
python_method('TestFiltering', 'test_skip_properties', 0, 2, 3).
python_class('tests/test_edge_cases.py', 'TestNLPEdgeCases').
python_method('TestNLPEdgeCases', 'test_empty_query', 0, 3, 2).
python_method('TestNLPEdgeCases', 'test_gibberish_query', 0, 3, 3).
python_method('TestNLPEdgeCases', 'test_very_long_query', 0, 2, 2).
python_method('TestNLPEdgeCases', 'test_mixed_languages', 0, 2, 3).
python_method('TestNLPEdgeCases', 'test_special_characters', 0, 3, 2).
python_class('tests/test_edge_cases.py', 'TestIntegration').
python_method('TestIntegration', 'test_codebase_entity_resolution', 0, 2, 11).
python_method('TestIntegration', 'test_nlp_to_analysis_workflow', 0, 4, 11).
python_class('tests/test_edge_cases.py', 'TestBenchmarks').
python_method('TestBenchmarks', 'test_analysis_performance', 0, 4, 13).
python_method('TestBenchmarks', 'test_nlp_performance', 0, 3, 3).
python_class('tests/test_flow_exporter.py', 'TestTypeInferenceEngine').
python_method('TestTypeInferenceEngine', 'test_extracts_return_annotation', 1, 3, 3).
python_method('TestTypeInferenceEngine', 'test_extracts_arg_types', 1, 6, 4).
python_method('TestTypeInferenceEngine', 'test_detects_default_args', 1, 3, 3).
python_method('TestTypeInferenceEngine', 'test_typed_signature_format', 1, 4, 3).
python_method('TestTypeInferenceEngine', 'test_name_based_fallback', 1, 3, 3).
python_method('TestTypeInferenceEngine', 'test_no_annotations_no_pattern', 1, 2, 6).
python_method('TestTypeInferenceEngine', 'test_batch_extract', 1, 4, 4).
python_class('tests/test_flow_exporter.py', 'TestSideEffectDetector').
python_method('TestSideEffectDetector', 'test_detects_io', 1, 3, 4).
python_method('TestSideEffectDetector', 'test_detects_pure', 1, 3, 3).
python_method('TestSideEffectDetector', 'test_detects_mutation', 1, 3, 3).
python_method('TestSideEffectDetector', 'test_detects_write_io', 1, 2, 3).
python_method('TestSideEffectDetector', 'test_side_effect_summary', 1, 2, 3).
python_method('TestSideEffectDetector', 'test_batch_analyze', 1, 3, 3).
python_method('TestSideEffectDetector', 'test_heuristic_fallback', 0, 2, 3).
python_method('TestSideEffectDetector', 'test_to_dict', 1, 4, 4).
python_class('tests/test_flow_exporter.py', 'TestFlowExporterSprint2').
python_method('TestFlowExporterSprint2', 'sample_result', 1, 1, 3).
python_method('TestFlowExporterSprint2', 'test_export_creates_file', 2, 2, 4).
python_method('TestFlowExporterSprint2', 'test_contracts_have_in_out', 2, 5, 4).
python_method('TestFlowExporterSprint2', 'test_data_types_has_source_counts', 2, 4, 4).
python_method('TestFlowExporterSprint2', 'test_side_effects_section', 2, 2, 4).
python_method('TestFlowExporterSprint2', 'test_type_annotations_in_signatures', 2, 2, 4).
python_method('TestFlowExporterSprint2', 'test_hub_type_split_recommendations', 1, 3, 10).
python_method('TestFlowExporterSprint2', 'test_pipeline_purity_uses_ast', 2, 3, 4).
python_class('tests/test_flow_exporter.py', 'TestEdgeCases').
python_method('TestEdgeCases', 'test_empty_result', 1, 3, 5).
python_method('TestEdgeCases', 'test_missing_source_file', 1, 2, 6).
python_method('TestEdgeCases', 'test_type_inference_bad_syntax', 1, 2, 5).
python_method('TestEdgeCases', 'test_side_effect_detector_bad_syntax', 1, 2, 5).
python_class('tests/test_format_quality.py', 'TestAnalysisToon').
python_method('TestAnalysisToon', 'toon_content', 2, 1, 4).
python_method('TestAnalysisToon', 'test_detects_god_function', 1, 3, 0).
python_method('TestAnalysisToon', 'test_detects_high_fan_out', 1, 3, 0).
python_method('TestAnalysisToon', 'test_has_health_section', 1, 2, 0).
python_method('TestAnalysisToon', 'test_has_refactor_section', 1, 2, 0).
python_method('TestAnalysisToon', 'test_has_coupling_section', 1, 2, 0).
python_method('TestAnalysisToon', 'test_has_severity_markers', 1, 2, 0).
python_method('TestAnalysisToon', 'test_has_layers', 1, 2, 0).
python_class('tests/test_format_quality.py', 'TestFlowToon').
python_method('TestFlowToon', 'flow_content', 2, 1, 4).
python_method('TestFlowToon', 'test_has_pipelines_section', 1, 2, 0).
python_method('TestFlowToon', 'test_has_transforms_section', 1, 2, 0).
python_method('TestFlowToon', 'test_has_type_info', 1, 2, 0).
python_method('TestFlowToon', 'test_detects_etl_pipeline_functions', 1, 2, 1).
python_method('TestFlowToon', 'test_has_side_effects_section', 1, 2, 2).
python_method('TestFlowToon', 'test_has_contracts_or_data_types', 1, 2, 1).
python_class('tests/test_format_quality.py', 'TestProjectMap').
python_method('TestProjectMap', 'map_content', 2, 1, 4).
python_method('TestProjectMap', 'test_lists_all_modules', 1, 4, 0).
python_method('TestProjectMap', 'test_has_import_info', 1, 2, 1).
python_method('TestProjectMap', 'test_has_function_signatures', 1, 3, 0).
python_method('TestProjectMap', 'test_has_type_annotations', 1, 2, 0).
python_class('tests/test_format_quality.py', 'TestContextMd').
python_method('TestContextMd', 'context_content', 2, 1, 4).
python_method('TestContextMd', 'test_has_overview', 1, 2, 0).
python_method('TestContextMd', 'test_has_entry_points', 1, 2, 0).
python_method('TestContextMd', 'test_is_markdown', 1, 2, 0).
python_class('tests/test_format_quality.py', 'TestCrossFormat').
python_method('TestCrossFormat', 'all_formats', 2, 4, 7).
python_method('TestCrossFormat', 'test_flow_toon_has_unique_pipeline_info', 1, 4, 3).
python_method('TestCrossFormat', 'test_analysis_toon_has_unique_health_info', 1, 7, 1).
python_method('TestCrossFormat', 'test_project_map_has_unique_structure_info', 1, 2, 2).
python_method('TestCrossFormat', 'test_formats_have_different_sizes', 1, 5, 6).
python_class('tests/test_multilanguage_e2e.py', 'TestMultiLanguageE2E').
python_method('TestMultiLanguageE2E', 'test_typescript_analysis', 0, 5, 7).
python_method('TestMultiLanguageE2E', 'test_javascript_analysis', 0, 3, 6).
python_method('TestMultiLanguageE2E', 'test_go_analysis', 0, 3, 6).
python_method('TestMultiLanguageE2E', 'test_rust_analysis', 0, 3, 6).
python_method('TestMultiLanguageE2E', 'test_java_analysis', 0, 3, 6).
python_method('TestMultiLanguageE2E', 'test_multilanguage_project', 0, 3, 6).
python_method('TestMultiLanguageE2E', 'test_language_detection_in_output', 0, 2, 6).
python_method('TestMultiLanguageE2E', 'test_excluded_directories_not_analyzed', 0, 4, 8).
python_class('tests/test_nlp_pipeline.py', 'TestQueryNormalization').
python_method('TestQueryNormalization', 'test_step_1a_lowercase', 0, 3, 2).
python_method('TestQueryNormalization', 'test_step_1b_remove_punctuation', 0, 3, 2).
python_method('TestQueryNormalization', 'test_step_1c_normalize_whitespace', 0, 3, 2).
python_method('TestQueryNormalization', 'test_step_1d_unicode_normalize', 0, 2, 2).
python_method('TestQueryNormalization', 'test_step_1e_remove_stopwords', 0, 4, 3).
python_method('TestQueryNormalization', 'test_polish_text_normalization', 0, 3, 2).
python_class('tests/test_nlp_pipeline.py', 'TestIntentMatching').
python_method('TestIntentMatching', 'test_step_2a_fuzzy_match', 0, 3, 2).
python_method('TestIntentMatching', 'test_step_2c_keyword_match', 0, 3, 3).
python_method('TestIntentMatching', 'test_step_2d_context_score', 0, 3, 2).
python_method('TestIntentMatching', 'test_step_2e_multi_intent_resolution', 0, 3, 3).
python_method('TestIntentMatching', 'test_polish_intent_matching', 0, 3, 2).
python_class('tests/test_nlp_pipeline.py', 'TestEntityResolution').
python_method('TestEntityResolution', 'mock_entities', 0, 1, 1).
python_method('TestEntityResolution', 'test_step_3a_extract_entities', 1, 3, 4).
python_method('TestEntityResolution', 'test_step_3b_name_match_threshold', 1, 3, 3).
python_method('TestEntityResolution', 'test_step_3c_disambiguation', 1, 5, 2).
python_method('TestEntityResolution', 'test_step_3d_hierarchical_resolution', 1, 3, 5).
python_method('TestEntityResolution', 'test_step_3e_alias_resolution', 1, 4, 4).
python_class('tests/test_nlp_pipeline.py', 'TestNLPPipeline').
python_method('TestNLPPipeline', 'test_step_4a_orchestration', 0, 3, 4).
python_method('TestNLPPipeline', 'test_step_4c_confidence_scoring', 0, 4, 2).
python_method('TestNLPPipeline', 'test_step_4d_fallback_handling', 0, 4, 2).
python_method('TestNLPPipeline', 'test_step_4e_output_formatting', 0, 4, 4).
python_method('TestNLPPipeline', 'test_polish_query_processing', 0, 3, 4).
python_class('tests/test_nlp_pipeline.py', 'TestNLPConfig').
python_method('TestNLPConfig', 'test_config_from_yaml', 1, 5, 3).
python_method('TestNLPConfig', 'test_config_to_yaml', 1, 3, 4).
python_class('tests/test_nlp_pipeline.py', 'TestMultilingualSupport').
python_method('TestMultilingualSupport', 'test_english_queries', 0, 3, 3).
python_method('TestMultilingualSupport', 'test_polish_queries', 0, 3, 3).
python_method('TestMultilingualSupport', 'test_mixed_language_fuzzy_matching', 0, 2, 2).
python_class('tests/test_nonpython_cc_calls.py', 'TestTypeScriptComplexityAndCalls').
python_method('TestTypeScriptComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestTypeScriptComplexityAndCalls', 'test_ts_functions_detected', 0, 8, 2).
python_method('TestTypeScriptComplexityAndCalls', 'test_ts_complexity_not_zero', 0, 6, 3).
python_method('TestTypeScriptComplexityAndCalls', 'test_ts_calls_extracted', 0, 5, 4).
python_method('TestTypeScriptComplexityAndCalls', 'test_ts_cc_avg_not_zero', 0, 4, 5).
python_class('tests/test_nonpython_cc_calls.py', 'TestGoComplexityAndCalls').
python_method('TestGoComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestGoComplexityAndCalls', 'test_go_complexity_not_zero', 0, 4, 3).
python_method('TestGoComplexityAndCalls', 'test_go_calls_extracted', 0, 4, 4).
python_class('tests/test_nonpython_cc_calls.py', 'TestRustComplexityAndCalls').
python_method('TestRustComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestRustComplexityAndCalls', 'test_rust_complexity_not_zero', 0, 4, 3).
python_class('tests/test_nonpython_cc_calls.py', 'TestJavaComplexityAndCalls').
python_method('TestJavaComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestJavaComplexityAndCalls', 'test_java_complexity_not_zero', 0, 5, 3).
python_method('TestJavaComplexityAndCalls', 'test_java_calls_extracted', 0, 3, 4).
python_class('tests/test_nonpython_cc_calls.py', 'TestCppComplexityAndCalls').
python_method('TestCppComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestCppComplexityAndCalls', 'test_cpp_classes_detected', 0, 3, 2).
python_method('TestCppComplexityAndCalls', 'test_cpp_complexity_not_zero', 0, 5, 3).
python_method('TestCppComplexityAndCalls', 'test_cpp_includes_extracted', 0, 3, 4).
python_class('tests/test_nonpython_cc_calls.py', 'TestCSharpComplexityAndCalls').
python_method('TestCSharpComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestCSharpComplexityAndCalls', 'test_cs_classes_detected', 0, 3, 2).
python_method('TestCSharpComplexityAndCalls', 'test_cs_complexity_not_zero', 0, 5, 3).
python_method('TestCSharpComplexityAndCalls', 'test_cs_usings_extracted', 0, 3, 4).
python_class('tests/test_nonpython_cc_calls.py', 'TestPhpComplexityAndCalls').
python_method('TestPhpComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestPhpComplexityAndCalls', 'test_php_classes_detected', 0, 3, 2).
python_method('TestPhpComplexityAndCalls', 'test_php_complexity_not_zero', 0, 5, 3).
python_method('TestPhpComplexityAndCalls', 'test_php_namespace_extracted', 0, 2, 4).
python_class('tests/test_nonpython_cc_calls.py', 'TestRubyComplexityAndCalls').
python_method('TestRubyComplexityAndCalls', '_analyze', 0, 1, 5).
python_method('TestRubyComplexityAndCalls', 'test_ruby_classes_detected', 0, 3, 2).
python_method('TestRubyComplexityAndCalls', 'test_ruby_complexity_not_zero', 0, 5, 3).
python_method('TestRubyComplexityAndCalls', 'test_ruby_requires_extracted', 0, 3, 4).
python_class('tests/test_persistent_cache.py', 'TestContentHash').
python_method('TestContentHash', 'test_same_content_same_hash', 2, 2, 2).
python_method('TestContentHash', 'test_different_content_different_hash', 2, 2, 2).
python_class('tests/test_persistent_cache.py', 'TestFileResultRoundtrip').
python_method('TestFileResultRoundtrip', 'test_put_then_get', 2, 2, 3).
python_method('TestFileResultRoundtrip', 'test_get_missing_returns_none', 2, 2, 2).
python_method('TestFileResultRoundtrip', 'test_manifest_updated_after_put', 2, 2, 3).
python_method('TestFileResultRoundtrip', 'test_put_dataclass_payload', 2, 4, 6).
python_class('tests/test_persistent_cache.py', 'TestAutoCleanup').
python_method('TestAutoCleanup', 'test_fresh_cache_no_removal', 2, 2, 1).
python_method('TestAutoCleanup', 'test_stale_export_removed', 2, 3, 7).
python_method('TestAutoCleanup', 'test_fresh_export_kept', 2, 3, 4).
python_method('TestAutoCleanup', 'test_abandoned_export_removed', 2, 3, 5).
python_method('TestAutoCleanup', 'test_referenced_file_entry_kept_even_if_old', 2, 5, 9).
python_method('TestAutoCleanup', 'test_orphan_file_entry_removed', 2, 3, 5).
python_method('TestAutoCleanup', 'test_orphan_file_entry_kept_if_fresh', 2, 3, 3).
python_method('TestAutoCleanup', 'test_auto_cleanup_triggered_on_init', 2, 2, 7).
python_method('TestAutoCleanup', 'test_env_var_disables_auto_cleanup', 3, 2, 8).
python_method('TestAutoCleanup', 'test_env_var_sets_ttl', 3, 2, 8).
python_class('tests/test_persistent_cache.py', 'TestPruneMissing').
python_method('TestPruneMissing', 'test_no_entries_no_op', 2, 2, 2).
python_method('TestPruneMissing', 'test_removes_vanished_entries', 2, 4, 3).
python_method('TestPruneMissing', 'test_pruning_changes_run_hash', 2, 2, 4).
python_method('TestPruneMissing', 'test_pruning_sets_dirty_flag', 2, 3, 4).
python_class('tests/test_persistent_cache.py', 'TestGetChangedFiles').
python_method('TestGetChangedFiles', 'test_new_files_are_changed', 2, 3, 3).
python_method('TestGetChangedFiles', 'test_cached_file_not_changed', 2, 3, 3).
python_method('TestGetChangedFiles', 'test_modified_file_is_changed', 2, 3, 6).
python_class('tests/test_persistent_cache.py', 'TestExportCache').
python_method('TestExportCache', 'test_missing_export_returns_none', 1, 2, 1).
python_method('TestExportCache', 'test_complete_export_returned', 2, 3, 5).
python_method('TestExportCache', 'test_different_config_different_dir', 1, 2, 1).
python_method('TestExportCache', 'test_empty_manifest_refuses_cache_hit', 1, 3, 3).
python_method('TestExportCache', 'test_populated_manifest_allows_cache_hit', 2, 3, 5).
python_class('tests/test_persistent_cache.py', 'TestSaveAndReload').
python_method('TestSaveAndReload', 'test_save_creates_manifest', 2, 2, 4).
python_method('TestSaveAndReload', 'test_reload_preserves_entries', 2, 2, 5).
python_method('TestSaveAndReload', 'test_version_mismatch_resets_manifest', 2, 3, 11).
python_class('tests/test_persistent_cache.py', 'TestGC').
python_method('TestGC', 'test_gc_removes_old_exports', 2, 3, 6).
python_method('TestGC', 'test_gc_keeps_recent_exports', 2, 3, 4).
python_class('tests/test_persistent_cache.py', 'TestClear').
python_method('TestClear', 'test_clear_empties_manifest', 2, 3, 4).
python_class('tests/test_persistent_cache.py', 'TestModuleLevelHelpers').
python_method('TestModuleLevelHelpers', 'test_get_all_projects_empty', 1, 2, 2).
python_method('TestModuleLevelHelpers', 'test_get_all_projects_after_save', 2, 3, 7).
python_method('TestModuleLevelHelpers', 'test_clear_all', 2, 2, 6).
python_class('tests/test_pipeline_detector.py', 'TestPipelineDetector').
python_method('TestPipelineDetector', 'test_detects_simple_chain', 0, 3, 4).
python_method('TestPipelineDetector', 'test_entry_exit_labeling', 0, 7, 4).
python_method('TestPipelineDetector', 'test_purity_aggregation', 1, 4, 7).
python_method('TestPipelineDetector', 'test_bottleneck_detection', 0, 5, 4).
python_method('TestPipelineDetector', 'test_pipeline_to_dict', 0, 7, 6).
python_method('TestPipelineDetector', 'test_no_pipelines_from_isolated_functions', 0, 2, 4).
python_method('TestPipelineDetector', 'test_empty_input', 0, 2, 2).
python_class('tests/test_pipeline_detector.py', 'TestDomainClassification').
python_method('TestDomainClassification', 'test_nlp_domain', 0, 3, 4).
python_method('TestDomainClassification', 'test_analysis_domain', 0, 3, 4).
python_method('TestDomainClassification', 'test_export_domain', 0, 3, 4).
python_method('TestDomainClassification', 'test_unknown_domain', 0, 3, 3).
python_class('tests/test_pipeline_detector.py', 'TestMultiplePipelines').
python_method('TestMultiplePipelines', 'test_three_independent_pipelines', 0, 4, 5).
python_method('TestMultiplePipelines', 'test_four_pipelines_with_domains', 0, 7, 5).
python_class('tests/test_pipeline_detector.py', 'TestFlowExporterSprint3').
python_method('TestFlowExporterSprint3', 'multi_pipeline_result', 0, 4, 2).
python_method('TestFlowExporterSprint3', 'test_output_has_domain_tags', 2, 3, 4).
python_method('TestFlowExporterSprint3', 'test_output_has_entry_exit_markers', 2, 3, 4).
python_method('TestFlowExporterSprint3', 'test_output_has_pipeline_purity', 2, 3, 4).
python_method('TestFlowExporterSprint3', 'test_output_has_all_sections', 2, 5, 4).
python_method('TestFlowExporterSprint3', 'test_contracts_show_domain_pipeline', 2, 4, 4).
python_class('tests/test_pipeline_detector.py', 'TestPipelineEdgeCases').
python_method('TestPipelineEdgeCases', 'test_cyclic_calls', 0, 2, 4).
python_method('TestPipelineEdgeCases', 'test_self_recursive', 0, 2, 4).
python_method('TestPipelineEdgeCases', 'test_diamond_dependency', 0, 3, 4).
python_method('TestPipelineEdgeCases', 'test_very_long_chain', 0, 4, 5).
python_class('tests/test_prompt_txt.py', 'TestPromptTxtGeneration').
python_method('TestPromptTxtGeneration', 'temp_output_dir', 0, 1, 2).
python_method('TestPromptTxtGeneration', 'mock_args', 0, 1, 1).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_not_generated_without_code2logic_format', 2, 2, 3).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_generated_with_code2logic_format', 2, 2, 4).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_generated_with_all_format', 2, 2, 3).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_lists_existing_files', 2, 10, 4).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_shows_missing_files', 2, 3, 3).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_contains_task_instructions', 2, 7, 3).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_prioritizes_blockers_when_validation_and_duplication_exist', 2, 7, 5).
python_method('TestPromptTxtGeneration', 'test_prompt_txt_content_structure', 2, 10, 6).
python_class('tests/test_prompt_txt.py', 'TestCode2logicExport').
python_method('TestCode2logicExport', 'temp_output_dir', 0, 1, 2).
python_method('TestCode2logicExport', 'test_export_code2logic_adds_quiet_flag_when_not_verbose', 1, 2, 4).
python_method('TestCode2logicExport', 'test_export_code2logic_does_not_add_quiet_flag_when_verbose', 1, 2, 4).
python_method('TestCode2logicExport', 'test_prompt_txt_no_verbose_output', 1, 2, 4).
python_class('tests/test_toon_v2.py', 'TestToonExporterV2').
python_method('TestToonExporterV2', 'test_export_creates_file', 2, 3, 6).
python_method('TestToonExporterV2', 'test_header_format', 2, 4, 6).
python_method('TestToonExporterV2', 'test_health_section', 2, 2, 4).
python_method('TestToonExporterV2', 'test_refactor_section', 2, 2, 4).
python_method('TestToonExporterV2', 'test_layers_section', 2, 3, 4).
python_method('TestToonExporterV2', 'test_functions_section_filters_by_cc', 2, 3, 5).
python_method('TestToonExporterV2', 'test_classes_section_with_bar_chart', 2, 3, 4).
python_method('TestToonExporterV2', 'test_hotspots_section', 2, 2, 4).
python_method('TestToonExporterV2', 'test_details_section', 2, 2, 4).
python_method('TestToonExporterV2', 'test_excluded_paths_venv', 0, 4, 2).
python_method('TestToonExporterV2', 'test_excluded_paths_site_packages', 0, 2, 2).
python_method('TestToonExporterV2', 'test_included_paths', 0, 3, 2).
python_method('TestToonExporterV2', 'test_max_health_issues_limit', 2, 5, 10).
python_method('TestToonExporterV2', 'test_coupling_matrix_limited', 2, 8, 8).
python_method('TestToonExporterV2', 'test_inline_markers', 2, 2, 5).
python_class('tests/test_toon_v2.py', 'TestToonExporterEdgeCases').
python_method('TestToonExporterEdgeCases', 'test_empty_result', 1, 3, 6).
python_method('TestToonExporterEdgeCases', 'test_single_function', 1, 2, 7).

% ── Dependencies ─────────────────────────────────────────
project_dependency('networkx>=3.0', 'requirements.txt').
project_dependency('matplotlib>=3.6.0', 'requirements.txt').
project_dependency('numpy>=1.21.0', 'requirements.txt').
project_dependency('pyyaml>=6.0', 'requirements.txt').
project_dependency('scipy>=1.7.0', 'requirements.txt').
project_dependency('radon>=5.1', 'requirements.txt').
project_dependency('psutil>=5.8.0', 'requirements.txt').
project_dependency('astroid>=3.0', 'requirements.txt').
project_dependency('code2logic', 'requirements.txt').

% ── Makefile Targets ─────────────────────────────────────
makefile_target('PYTHON', '').
makefile_target('help', 'Default target').
makefile_target('install', '').
makefile_target('dev-install', '').
makefile_target('test', '').
makefile_target('test-cov', '').
makefile_target('test-toon', '').
makefile_target('validate-toon', '').
makefile_target('test-all-formats', '').
makefile_target('test-comprehensive', '').
makefile_target('lint', '').
makefile_target('format', '').
makefile_target('typecheck', '').
makefile_target('check', '').
makefile_target('run', '').
makefile_target('analyze', '').
makefile_target('analyze-all', '').
makefile_target('toon-demo', '').
makefile_target('toon-compare', '').
makefile_target('toon-validate', '').
makefile_target('build', '').
makefile_target('publish-test', '').
makefile_target('bump-patch', '').
makefile_target('bump-minor', '').
makefile_target('bump-major', '').
makefile_target('publish', '').
makefile_target('mermaid-png', '').
makefile_target('install-mermaid', '').
makefile_target('check-mermaid', '').
makefile_target('clean', '').
makefile_target('clean-png', '').
makefile_target('quickstart', '').

% ── Taskfile Tasks ───────────────────────────────────────
taskfile_task('', 'Install Python dependencies (editable)').
taskfile_task('', 'Run pytest suite').
taskfile_task('', 'Build wheel + sdist').
taskfile_task('', 'Remove build artefacts').
taskfile_task('', '[imported from Makefile] help').
taskfile_task('', '[imported from Makefile] dev-install').
taskfile_task('', '[imported from Makefile] test-cov').
taskfile_task('', '[imported from Makefile] test-toon').
taskfile_task('', '[imported from Makefile] validate-toon').
taskfile_task('', '[imported from Makefile] test-all-formats').
taskfile_task('', '[imported from Makefile] test-comprehensive').
taskfile_task('', '[imported from Makefile] lint').
taskfile_task('', '[imported from Makefile] format').
taskfile_task('', '[imported from Makefile] typecheck').
taskfile_task('', '[imported from Makefile] check').
taskfile_task('', '[imported from Makefile] run').
taskfile_task('', '[imported from Makefile] analyze').
taskfile_task('', '[imported from Makefile] analyze-all').
taskfile_task('', '[imported from Makefile] toon-demo').
taskfile_task('', '[imported from Makefile] toon-compare').
taskfile_task('', '[imported from Makefile] toon-validate').
taskfile_task('', '[imported from Makefile] publish-test').
taskfile_task('', '[imported from Makefile] bump-patch').
taskfile_task('', '[imported from Makefile] bump-minor').
taskfile_task('', '[imported from Makefile] bump-major').
taskfile_task('', '[imported from Makefile] publish').
taskfile_task('', '[imported from Makefile] mermaid-png').
taskfile_task('', '[imported from Makefile] install-mermaid').
taskfile_task('', '[imported from Makefile] check-mermaid').
taskfile_task('', '[imported from Makefile] clean-png').
taskfile_task('', '[imported from Makefile] quickstart').
taskfile_task('', '[from doql] workflow: health').
taskfile_task('', '[from doql] workflow: import-makefile-hint').
taskfile_task('', 'Run install, lint, test').
taskfile_task('', 'Auto-format with ruff').
taskfile_task('', 'Generate SUMD (Structured Unified Markdown Descriptor) for AI-aware project description').
taskfile_task('', 'Generate SUMR (Summary Report) with project metrics and health status').

% ── Environment Variables ────────────────────────────────
env_variable('CODE2FLOW_CALLS_SPLIT', '1', 'Enable/disable splitting').
env_variable('CODE2FLOW_CALLS_KEEP_MAIN', '0', 'Keep writing the full calls.mmd in addition to parts').
env_variable('CODE2FLOW_CALLS_MIN_NODES', '30', 'Minimum number of functions per part').
env_variable('CODE2FLOW_CALLS_MAX_NODES', '250', 'Maximum number of functions per part').
env_variable('CODE2FLOW_CALLS_MAX_PARTS', '20', 'Maximum number of parts to generate').
env_variable('CODE2FLOW_CALLS_INCLUDE_SINGLETONS', '0', 'Include singleton components (1 function with no edges)').
env_variable('CODE2FLOW_MERMAID_MAX_EDGES', '20000', 'Increase if Mermaid CLI reports edge/text limits.').
env_variable('CODE2FLOW_MERMAID_MAX_TEXT_SIZE', '2000000', '').

% ── TestQL Scenarios ─────────────────────────────────────
testql_scenario('generated-cli-tests.testql.toon.yaml', 'cli').

% ── Semantic Facts from SUMD.md ──────────────────────────
sumd_declared_file('app.doql.less', 'doql').
sumd_declared_file('testql-scenarios/generated-api-smoke.testql.toon.yaml', 'testql').
sumd_declared_file('testql-scenarios/generated-cli-tests.testql.toon.yaml', 'testql').
sumd_declared_file('testql-scenarios/generated-from-pytests.testql.toon.yaml', 'testql').
sumd_declared_file('Taskfile.yml', 'taskfile').
sumd_declared_file('pyqual.yaml', 'pyqual').
sumd_declared_file('project/map.toon.yaml', 'analysis').
sumd_declared_file('project/calls.toon.yaml', 'analysis').
sumd_interface('cli', 'click').
sumd_workflow('install', 'manual').
sumd_workflow_step('install', 1, 'pip install -e .').
sumd_workflow('dev', 'manual').
sumd_workflow_step('dev', 1, 'pip install -e ".[dev]"').
sumd_workflow('build', 'manual').
sumd_workflow_step('build', 1, 'python -m build').
sumd_workflow('test', 'manual').
sumd_workflow_step('test', 1, 'pytest -q').
sumd_workflow('lint', 'manual').
sumd_workflow_step('lint', 1, 'ruff check .').
sumd_workflow('fmt', 'manual').
sumd_workflow_step('fmt', 1, 'ruff format .').
sumd_workflow('clean', 'manual').
sumd_workflow_step('clean', 1, 'rm -rf build/ dist/ *.egg-info').
sumd_workflow('help', 'manual').
sumd_workflow_step('help', 1, 'task --list').

