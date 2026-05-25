# System Architecture Analysis
<!-- generated in 0.01s -->

## Overview

- **Project**: /home/tom/github/semcod/code2llm
- **Primary Language**: python
- **Languages**: python: 348, md: 44, yaml: 12, shell: 4, yml: 3
- **Analysis Mode**: static
- **Total Functions**: 1312
- **Total Classes**: 143
- **Modules**: 427
- **Entry Points**: 0

## Architecture by Module

### code2llm.core.analyzer
- **Functions**: 25
- **Classes**: 1
- **File**: `analyzer.py`

### code2llm.exporters.yaml_exporter
- **Functions**: 25
- **Classes**: 1
- **File**: `yaml_exporter.py`

### core.analyzer
- **Functions**: 25
- **Classes**: 1
- **File**: `analyzer.py`

### exporters.yaml_exporter
- **Functions**: 25
- **Classes**: 1
- **File**: `yaml_exporter.py`

### code2llm.core.persistent_cache
- **Functions**: 22
- **Classes**: 1
- **File**: `persistent_cache.py`

### core.persistent_cache
- **Functions**: 22
- **Classes**: 1
- **File**: `persistent_cache.py`

### root.validate_toon
- **Functions**: 21
- **File**: `validate_toon.py`

### code2llm.analysis._data_impl
- **Functions**: 21
- **File**: `_data_impl.py`

### code2llm.core.file_analyzer
- **Functions**: 21
- **Classes**: 1
- **File**: `file_analyzer.py`

### analysis._data_impl
- **Functions**: 21
- **File**: `_data_impl.py`

### core.file_analyzer
- **Functions**: 21
- **Classes**: 1
- **File**: `file_analyzer.py`

### code2llm.core.large_repo
- **Functions**: 20
- **Classes**: 2
- **File**: `large_repo.py`

### code2llm.nlp.pipeline
- **Functions**: 20
- **Classes**: 3
- **File**: `pipeline.py`

### core.large_repo
- **Functions**: 20
- **Classes**: 2
- **File**: `large_repo.py`

### nlp.pipeline
- **Functions**: 20
- **Classes**: 3
- **File**: `pipeline.py`

### code2llm.cli_exports.prompt
- **Functions**: 19
- **File**: `prompt.py`

### code2llm.cli_exports.orchestrator
- **Functions**: 19
- **File**: `orchestrator.py`

### cli_exports.prompt
- **Functions**: 19
- **File**: `prompt.py`

### cli_exports.orchestrator
- **Functions**: 19
- **File**: `orchestrator.py`

### examples.functional_refactoring.entity_preparers
- **Functions**: 18
- **Classes**: 6
- **File**: `entity_preparers.py`

## Key Entry Points

Main execution flows into the system:

## Process Flows

Key execution flows identified:

## Key Classes

### code2llm.core.analyzer.ProjectAnalyzer
> Main analyzer with parallel processing.
- **Methods**: 25
- **Key Methods**: code2llm.core.analyzer.ProjectAnalyzer.__init__, code2llm.core.analyzer.ProjectAnalyzer.analyze_project, code2llm.core.analyzer.ProjectAnalyzer._resolve_project_path, code2llm.core.analyzer.ProjectAnalyzer._log_cache_stats, code2llm.core.analyzer.ProjectAnalyzer._load_from_persistent_cache, code2llm.core.analyzer.ProjectAnalyzer._run_analysis, code2llm.core.analyzer.ProjectAnalyzer._store_to_persistent_cache, code2llm.core.analyzer.ProjectAnalyzer._build_stats, code2llm.core.analyzer.ProjectAnalyzer._print_summary, code2llm.core.analyzer.ProjectAnalyzer._post_process

### code2llm.exporters.yaml_exporter.YAMLExporter
> Export to YAML format.
- **Methods**: 25
- **Key Methods**: code2llm.exporters.yaml_exporter.YAMLExporter.__init__, code2llm.exporters.yaml_exporter.YAMLExporter._get_name_index, code2llm.exporters.yaml_exporter.YAMLExporter.export, code2llm.exporters.yaml_exporter.YAMLExporter.export_grouped, code2llm.exporters.yaml_exporter.YAMLExporter.export_data_flow, code2llm.exporters.yaml_exporter.YAMLExporter.export_data_structures, code2llm.exporters.yaml_exporter.YAMLExporter.export_separated, code2llm.exporters.yaml_exporter.YAMLExporter.export_split, code2llm.exporters.yaml_exporter.YAMLExporter.export_calls, code2llm.exporters.yaml_exporter.YAMLExporter._collect_edges
- **Inherits**: BaseExporter

### code2llm.core.file_analyzer.FileAnalyzer
> Analyzes a single file.
- **Methods**: 20
- **Key Methods**: code2llm.core.file_analyzer.FileAnalyzer.__init__, code2llm.core.file_analyzer.FileAnalyzer._route_to_language_analyzer, code2llm.core.file_analyzer.FileAnalyzer._cache_get, code2llm.core.file_analyzer.FileAnalyzer._cache_put, code2llm.core.file_analyzer.FileAnalyzer.analyze_file, code2llm.core.file_analyzer.FileAnalyzer._analyze_python, code2llm.core.file_analyzer.FileAnalyzer._analyze_ast, code2llm.core.file_analyzer.FileAnalyzer._calculate_complexity, code2llm.core.file_analyzer.FileAnalyzer._perform_deep_analysis, code2llm.core.file_analyzer.FileAnalyzer._process_class

### code2llm.core.large_repo.HierarchicalRepoSplitter
> Splits large repositories using hierarchical approach.

Strategy:
1. First pass: level 1 folders
2. 
- **Methods**: 18
- **Key Methods**: code2llm.core.large_repo.HierarchicalRepoSplitter.__init__, code2llm.core.large_repo.HierarchicalRepoSplitter.get_analysis_plan, code2llm.core.large_repo.HierarchicalRepoSplitter._split_hierarchically, code2llm.core.large_repo.HierarchicalRepoSplitter._merge_small_l1_dirs, code2llm.core.large_repo.HierarchicalRepoSplitter._split_level2_consolidated, code2llm.core.large_repo.HierarchicalRepoSplitter._categorize_subdirs, code2llm.core.large_repo.HierarchicalRepoSplitter._process_large_dirs, code2llm.core.large_repo.HierarchicalRepoSplitter._process_level1_files, code2llm.core.large_repo.HierarchicalRepoSplitter._merge_small_dirs, code2llm.core.large_repo.HierarchicalRepoSplitter._chunk_by_files

### code2llm.core.persistent_cache.PersistentCache
> Content-addressed persistent cache stored in ~/.code2llm/.

Thread-safety: manifest writes are prote
- **Methods**: 18
- **Key Methods**: code2llm.core.persistent_cache.PersistentCache.__init__, code2llm.core.persistent_cache.PersistentCache.content_hash, code2llm.core.persistent_cache.PersistentCache.get_file_result, code2llm.core.persistent_cache.PersistentCache.put_file_result, code2llm.core.persistent_cache.PersistentCache.get_changed_files, code2llm.core.persistent_cache.PersistentCache.prune_missing, code2llm.core.persistent_cache.PersistentCache.get_export_cache_dir, code2llm.core.persistent_cache.PersistentCache.create_export_cache_dir, code2llm.core.persistent_cache.PersistentCache.mark_export_complete, code2llm.core.persistent_cache.PersistentCache.save

### code2llm.analysis.type_inference.TypeInferenceEngine
> Extract and infer type information from Python source files.

Operates on source files referenced by
- **Methods**: 17
- **Key Methods**: code2llm.analysis.type_inference.TypeInferenceEngine.__init__, code2llm.analysis.type_inference.TypeInferenceEngine.enrich_function, code2llm.analysis.type_inference.TypeInferenceEngine.get_arg_types, code2llm.analysis.type_inference.TypeInferenceEngine.get_return_type, code2llm.analysis.type_inference.TypeInferenceEngine.get_typed_signature, code2llm.analysis.type_inference.TypeInferenceEngine.extract_all_types, code2llm.analysis.type_inference.TypeInferenceEngine._extract_from_node, code2llm.analysis.type_inference.TypeInferenceEngine._extract_args, code2llm.analysis.type_inference.TypeInferenceEngine._annotation_to_str, code2llm.analysis.type_inference.TypeInferenceEngine._ann_constant

### code2llm.analysis.cfg.CFGExtractor
> Extract Control Flow Graph from AST.
- **Methods**: 16
- **Key Methods**: code2llm.analysis.cfg.CFGExtractor.__init__, code2llm.analysis.cfg.CFGExtractor.extract, code2llm.analysis.cfg.CFGExtractor.new_node, code2llm.analysis.cfg.CFGExtractor.connect, code2llm.analysis.cfg.CFGExtractor.visit_FunctionDef, code2llm.analysis.cfg.CFGExtractor.visit_AsyncFunctionDef, code2llm.analysis.cfg.CFGExtractor.visit_If, code2llm.analysis.cfg.CFGExtractor.visit_For, code2llm.analysis.cfg.CFGExtractor.visit_While, code2llm.analysis.cfg.CFGExtractor.visit_Try
- **Inherits**: ast.NodeVisitor

### code2llm.nlp.pipeline.NLPPipeline
> Main NLP processing pipeline (4a-4e).
- **Methods**: 16
- **Key Methods**: code2llm.nlp.pipeline.NLPPipeline.__init__, code2llm.nlp.pipeline.NLPPipeline.process, code2llm.nlp.pipeline.NLPPipeline._step_normalize, code2llm.nlp.pipeline.NLPPipeline._step_match_intent, code2llm.nlp.pipeline.NLPPipeline._step_resolve_entities, code2llm.nlp.pipeline.NLPPipeline._infer_entity_types, code2llm.nlp.pipeline.NLPPipeline._calculate_overall_confidence, code2llm.nlp.pipeline.NLPPipeline._calculate_entity_confidence, code2llm.nlp.pipeline.NLPPipeline._apply_fallback, code2llm.nlp.pipeline.NLPPipeline._format_action

### code2llm.exporters.toon.metrics_core.CoreMetricsComputer
> Computes core structural and complexity metrics.
- **Methods**: 16
- **Key Methods**: code2llm.exporters.toon.metrics_core.CoreMetricsComputer.__init__, code2llm.exporters.toon.metrics_core.CoreMetricsComputer._ensure_file_record, code2llm.exporters.toon.metrics_core.CoreMetricsComputer.compute_file_metrics, code2llm.exporters.toon.metrics_core.CoreMetricsComputer._new_file_record, code2llm.exporters.toon.metrics_core.CoreMetricsComputer._build_suffix_index, code2llm.exporters.toon.metrics_core.CoreMetricsComputer._update_importers_from_called_by, code2llm.exporters.toon.metrics_core.CoreMetricsComputer._update_importers_from_calls, code2llm.exporters.toon.metrics_core.CoreMetricsComputer._compute_fan_in, code2llm.exporters.toon.metrics_core.CoreMetricsComputer.compute_package_metrics, code2llm.exporters.toon.metrics_core.CoreMetricsComputer.compute_function_metrics

### code2llm.analysis.side_effects.SideEffectDetector
> Detect side effects in Python functions via AST analysis.

Scans function bodies for IO operations, 
- **Methods**: 15
- **Key Methods**: code2llm.analysis.side_effects.SideEffectDetector.__init__, code2llm.analysis.side_effects.SideEffectDetector.analyze_function, code2llm.analysis.side_effects.SideEffectDetector.analyze_all, code2llm.analysis.side_effects.SideEffectDetector.get_purity_score, code2llm.analysis.side_effects.SideEffectDetector._scan_node, code2llm.analysis.side_effects.SideEffectDetector._check_io_call, code2llm.analysis.side_effects.SideEffectDetector._check_cache_call, code2llm.analysis.side_effects.SideEffectDetector._check_calls, code2llm.analysis.side_effects.SideEffectDetector._check_assignments, code2llm.analysis.side_effects.SideEffectDetector._check_globals

### code2llm.nlp.entity_resolution.EntityResolver
> Resolve entities (functions, classes, etc.) from queries.
- **Methods**: 15
- **Key Methods**: code2llm.nlp.entity_resolution.EntityResolver.__init__, code2llm.nlp.entity_resolution.EntityResolver._apply_resolution_steps, code2llm.nlp.entity_resolution.EntityResolver.resolve, code2llm.nlp.entity_resolution.EntityResolver._extract_candidates, code2llm.nlp.entity_resolution.EntityResolver._extract_from_patterns, code2llm.nlp.entity_resolution.EntityResolver._disambiguate, code2llm.nlp.entity_resolution.EntityResolver._resolve_hierarchical, code2llm.nlp.entity_resolution.EntityResolver._resolve_aliases, code2llm.nlp.entity_resolution.EntityResolver._name_similarity, code2llm.nlp.entity_resolution.EntityResolver.load_from_analysis

### code2llm.exporters.context_exporter.ContextExporter
> Export LLM-ready analysis summary with architecture and flows.

Output: context.md — architecture na
- **Methods**: 15
- **Key Methods**: code2llm.exporters.context_exporter.ContextExporter.export, code2llm.exporters.context_exporter.ContextExporter._get_overview, code2llm.exporters.context_exporter.ContextExporter._detect_languages, code2llm.exporters.context_exporter.ContextExporter._get_architecture_by_module, code2llm.exporters.context_exporter.ContextExporter._get_important_entries, code2llm.exporters.context_exporter.ContextExporter._get_key_entry_points, code2llm.exporters.context_exporter.ContextExporter._get_process_flows, code2llm.exporters.context_exporter.ContextExporter._get_key_classes, code2llm.exporters.context_exporter.ContextExporter._get_data_transformations, code2llm.exporters.context_exporter.ContextExporter._get_behavioral_patterns
- **Inherits**: BaseExporter

### code2llm.exporters.flow_exporter.FlowExporter
> Export to flow.toon — data-flow focused format.

Sections: PIPELINES, TRANSFORMS, CONTRACTS, DATA_TY
- **Methods**: 14
- **Key Methods**: code2llm.exporters.flow_exporter.FlowExporter.__init__, code2llm.exporters.flow_exporter.FlowExporter.export, code2llm.exporters.flow_exporter.FlowExporter._build_context, code2llm.exporters.flow_exporter.FlowExporter._pipeline_to_dict, code2llm.exporters.flow_exporter.FlowExporter._compute_transforms, code2llm.exporters.flow_exporter.FlowExporter._transform_label, code2llm.exporters.flow_exporter.FlowExporter._compute_type_usage, code2llm.exporters.flow_exporter.FlowExporter._normalize_type, code2llm.exporters.flow_exporter.FlowExporter._type_label, code2llm.exporters.flow_exporter.FlowExporter._classify_side_effects
- **Inherits**: BaseExporter

### examples.streaming-analyzer.sample_project.database.DatabaseConnection
> Simple database connection simulator.
- **Methods**: 13
- **Key Methods**: examples.streaming-analyzer.sample_project.database.DatabaseConnection.__init__, examples.streaming-analyzer.sample_project.database.DatabaseConnection._load_data, examples.streaming-analyzer.sample_project.database.DatabaseConnection._save_data, examples.streaming-analyzer.sample_project.database.DatabaseConnection.get_user, examples.streaming-analyzer.sample_project.database.DatabaseConnection.get_user_settings, examples.streaming-analyzer.sample_project.database.DatabaseConnection.get_user_logs, examples.streaming-analyzer.sample_project.database.DatabaseConnection.update_user_settings, examples.streaming-analyzer.sample_project.database.DatabaseConnection.update_user_profile, examples.streaming-analyzer.sample_project.database.DatabaseConnection.delete_user, examples.streaming-analyzer.sample_project.database.DatabaseConnection.clear_user_data

### code2llm.nlp.intent_matching.IntentMatcher
> Match queries to intents using fuzzy and keyword matching.
- **Methods**: 13
- **Key Methods**: code2llm.nlp.intent_matching.IntentMatcher.__init__, code2llm.nlp.intent_matching.IntentMatcher.match, code2llm.nlp.intent_matching.IntentMatcher._fuzzy_match, code2llm.nlp.intent_matching.IntentMatcher._keyword_match, code2llm.nlp.intent_matching.IntentMatcher._apply_context, code2llm.nlp.intent_matching.IntentMatcher._combine_matches, code2llm.nlp.intent_matching.IntentMatcher._resolve_multi_intent, code2llm.nlp.intent_matching.IntentMatcher._calculate_similarity, code2llm.nlp.intent_matching.IntentMatcher.step_2a_fuzzy_match, code2llm.nlp.intent_matching.IntentMatcher.step_2b_semantic_match

### code2llm.nlp.normalization.QueryNormalizer
> Normalize queries for consistent processing.
- **Methods**: 13
- **Key Methods**: code2llm.nlp.normalization.QueryNormalizer.__init__, code2llm.nlp.normalization.QueryNormalizer.normalize, code2llm.nlp.normalization.QueryNormalizer._unicode_normalize, code2llm.nlp.normalization.QueryNormalizer._lowercase, code2llm.nlp.normalization.QueryNormalizer._remove_punctuation, code2llm.nlp.normalization.QueryNormalizer._normalize_whitespace, code2llm.nlp.normalization.QueryNormalizer._remove_stopwords, code2llm.nlp.normalization.QueryNormalizer._tokenize, code2llm.nlp.normalization.QueryNormalizer.step_1a_lowercase, code2llm.nlp.normalization.QueryNormalizer.step_1b_remove_punctuation

### code2llm.exporters.toon.renderer.ToonRenderer
> Renders all sections for TOON export.
- **Methods**: 13
- **Key Methods**: code2llm.exporters.toon.renderer.ToonRenderer.render_header, code2llm.exporters.toon.renderer.ToonRenderer.render_health, code2llm.exporters.toon.renderer.ToonRenderer.render_refactor, code2llm.exporters.toon.renderer.ToonRenderer.render_coupling, code2llm.exporters.toon.renderer.ToonRenderer._render_coupling_rows, code2llm.exporters.toon.renderer.ToonRenderer.render_layers, code2llm.exporters.toon.renderer.ToonRenderer._render_layer_files, code2llm.exporters.toon.renderer.ToonRenderer.render_duplicates, code2llm.exporters.toon.renderer.ToonRenderer.render_functions, code2llm.exporters.toon.renderer.ToonRenderer.render_hotspots

### code2llm.analysis.dfg.DFGExtractor
> Extract Data Flow Graph from AST.
- **Methods**: 12
- **Key Methods**: code2llm.analysis.dfg.DFGExtractor.__init__, code2llm.analysis.dfg.DFGExtractor.extract, code2llm.analysis.dfg.DFGExtractor.visit_FunctionDef, code2llm.analysis.dfg.DFGExtractor.visit_Assign, code2llm.analysis.dfg.DFGExtractor.visit_AugAssign, code2llm.analysis.dfg.DFGExtractor.visit_For, code2llm.analysis.dfg.DFGExtractor.visit_Call, code2llm.analysis.dfg.DFGExtractor._extract_targets, code2llm.analysis.dfg.DFGExtractor._get_names, code2llm.analysis.dfg.DFGExtractor._extract_names
- **Inherits**: ast.NodeVisitor

### code2llm.analysis.call_graph.CallGraphExtractor
> Extract call graph from AST.
- **Methods**: 12
- **Key Methods**: code2llm.analysis.call_graph.CallGraphExtractor.__init__, code2llm.analysis.call_graph.CallGraphExtractor.extract, code2llm.analysis.call_graph.CallGraphExtractor._calculate_metrics, code2llm.analysis.call_graph.CallGraphExtractor.visit_Import, code2llm.analysis.call_graph.CallGraphExtractor.visit_ImportFrom, code2llm.analysis.call_graph.CallGraphExtractor.visit_ClassDef, code2llm.analysis.call_graph.CallGraphExtractor.visit_FunctionDef, code2llm.analysis.call_graph.CallGraphExtractor.visit_AsyncFunctionDef, code2llm.analysis.call_graph.CallGraphExtractor.visit_Call, code2llm.analysis.call_graph.CallGraphExtractor._resolve_call
- **Inherits**: ast.NodeVisitor

### code2llm.core.export_pipeline.SharedExportContext
> Pre-computed context shared across all exporters.

Lazy-computes expensive aggregations on first acc
- **Methods**: 12
- **Key Methods**: code2llm.core.export_pipeline.SharedExportContext.__init__, code2llm.core.export_pipeline.SharedExportContext.result, code2llm.core.export_pipeline.SharedExportContext.functions, code2llm.core.export_pipeline.SharedExportContext.classes, code2llm.core.export_pipeline.SharedExportContext.modules, code2llm.core.export_pipeline.SharedExportContext.entry_points, code2llm.core.export_pipeline.SharedExportContext.metrics_summary, code2llm.core.export_pipeline.SharedExportContext.complexity_distribution, code2llm.core.export_pipeline.SharedExportContext.call_graph_edges, code2llm.core.export_pipeline.SharedExportContext.high_complexity_functions

## Data Transformation Functions

Key functions that process and transform data:

### validate_toon.validate_toon_completeness
> Validate toon format structure.
- **Output to**: print, print, bool, bool, bool

### test_langs.valid.sample.ProcessUsers
- **Output to**: test_langs.valid.sample.func, test_langs.valid.sample.Printf

### test_langs.valid.sample.UserService.processUsers
- **Output to**: test_langs.valid.sample.foreach

### test_langs.valid.sample.process_users

### examples.docker-doql-example.worker.worker.process_message
- **Output to**: print, time.sleep, print, ch.basic_ack

### examples.streaming-analyzer.sample_project.auth.AuthManager.validate_session
> Validate session and return user ID.
- **Output to**: self.sessions.get

### examples.streaming-analyzer.sample_project.api.APIHandler.process_request
> Process API request.
- **Output to**: self._check_rate_limit, self._get_stats, self._get_user_info, self._health_check

### examples.streaming-analyzer.sample_project.api.APIHandler.format_response
> Format API response.
- **Output to**: json.dumps

### examples.streaming-analyzer.sample_project.utils.validate_input
> Validate input data.
- **Output to**: isinstance, isinstance

### examples.streaming-analyzer.sample_project.utils.format_output
> Format output data.
- **Output to**: isinstance, json.dumps, isinstance, json.dumps, str

### examples.streaming-analyzer.sample_project.utils.transform_data
> Transform data fields.
- **Output to**: item.copy, transformations.items, transformed.append, None.upper, None.lower

### examples.streaming-analyzer.sample_project.main.Application.process_request
> Process a user request with complex logic.
- **Output to**: request.action.startswith, examples.streaming-analyzer.sample_project.utils.validate_input, print, self.auth.authenticate, print

### benchmarks.benchmark_evolution.parse_evolution_metrics
> Extract metrics from evolution.toon content.
- **Output to**: toon_content.splitlines, re.search, line.strip, line.startswith, int

### benchmarks.format_evaluator.evaluate_format
> Oceń pojedynczy format względem ground truth.
- **Output to**: FormatScore, benchmarks.format_evaluator._detect_problems, sum, benchmarks.format_evaluator._detect_pipelines, sum

### benchmarks.benchmark_format_quality._generate_format_outputs
> Generate all format outputs and evaluate them.
- **Output to**: format_configs.items, __import__, getattr, exporter_cls, time.time

### scripts.benchmark_badges.parse_evolution_metrics
> Extract metrics from evolution.toon content.
- **Output to**: toon_content.splitlines, re.search, line.strip, m.group, line.startswith

### scripts.benchmark_badges.parse_format_quality_report
> Parse format quality JSON report.
- **Output to**: report_path.exists, json.loads, data.get, report_path.read_text

### scripts.benchmark_badges.parse_performance_report
> Parse performance JSON report.
- **Output to**: report_path.exists, json.loads, report_path.read_text

### scripts.benchmark_badges.generate_format_quality_badges
> Generate badges from format quality scores.
- **Output to**: enumerate, badges.append, sorted, badges.append, format_scores.items

### scripts.bump_version.parse_version
> Parse version string into tuple of (major, minor, patch)
- **Output to**: version_str.split, tuple, int

### scripts.bump_version.format_version
> Format version tuple as string

### test_python_only.valid.sample.UserService.process_users
- **Output to**: print

### code2llm.cli_parser.create_parser
> Create CLI argument parser.
- **Output to**: argparse.ArgumentParser, parser.add_argument, parser.add_argument, parser.add_argument, parser.add_argument

### code2llm.cli_commands.validate_and_setup
> Validate source path and setup output directory.
- **Output to**: None.resolve, Path, output_dir.mkdir, print, print

### code2llm.cli_commands.validate_chunked_output
> Validate generated chunked output.

Checks:
1. All chunks have required files (analysis.toon, contex
- **Output to**: code2llm.cli_commands._get_chunk_dirs, code2llm.cli_commands._validate_chunks, code2llm.cli_commands._print_validation_summary, output_dir.exists, print

## Public API Surface

Functions exposed as public API (no underscore prefix):

- `pipeline.run_pipeline` - 68 calls
- `code2llm.cli_parser.create_parser` - 51 calls
- `code2llm.generators.llm_task.normalize_llm_task` - 43 calls
- `code2llm.generators.llm_flow.generator.render_llm_flow_md` - 42 calls
- `benchmarks.benchmark_performance.main` - 41 calls
- `validate_toon.analyze_class_differences` - 39 calls
- `benchmarks.benchmark_evolution.run_benchmark` - 34 calls
- `code2llm.core.lang.rust.analyze_rust` - 31 calls
- `benchmarks.benchmark_optimizations.benchmark_cold_vs_warm` - 30 calls
- `benchmarks.benchmark_performance.create_test_project` - 29 calls
- `code2llm.nlp.pipeline.NLPPipeline.process` - 29 calls
- `validate_toon.compare_modules` - 26 calls
- `benchmarks.benchmark_evolution.parse_evolution_metrics` - 25 calls
- `code2llm.exporters.toon.ToonExporter.export` - 25 calls
- `validate_toon.compare_functions` - 24 calls
- `code2llm.exporters.context_exporter.ContextExporter.export` - 24 calls
- `scripts.benchmark_badges.main` - 23 calls
- `benchmarks.format_evaluator.evaluate_format` - 22 calls
- `benchmarks.benchmark_format_quality.run_benchmark` - 22 calls
- `code2llm.core.analyzer.ProjectAnalyzer.analyze_project` - 22 calls
- `code2llm.exporters.evolution_exporter.EvolutionExporter.export` - 22 calls
- `code2llm.exporters.flow_exporter.FlowExporter.export` - 22 calls
- `code2llm.cli_commands.generate_llm_context` - 21 calls
- `validate_toon.compare_classes` - 19 calls
- `examples.streaming-analyzer.demo.demo_incremental_analysis` - 19 calls
- `code2llm.core.streaming.prioritizer.SmartPrioritizer.prioritize_files` - 19 calls
- `code2llm.exporters.yaml_exporter.YAMLExporter.export_grouped` - 19 calls
- `code2llm.exporters.yaml_exporter.YAMLExporter.export_calls_toon` - 19 calls
- `code2llm.exporters.evolution.yaml_export.export_to_yaml` - 19 calls
- `code2llm.exporters.map.yaml_export.export_to_yaml` - 19 calls
- `code2llm.exporters.mermaid.calls.export_calls` - 19 calls
- `benchmarks.benchmark_optimizations.print_summary` - 18 calls
- `code2llm.exporters.flow_renderer.FlowRenderer.render_pipelines` - 18 calls
- `code2llm.exporters.map.header.render_header` - 18 calls
- `code2llm.generators.llm_flow.cli.main` - 18 calls
- `validate_toon.validate_toon_completeness` - 17 calls
- `examples.litellm.run.main` - 17 calls
- `examples.streaming-analyzer.demo.main` - 17 calls
- `code2llm.cli_commands.handle_report_command` - 17 calls
- `code2llm.exporters.readme_exporter.READMEExporter.export` - 17 calls

## System Interactions

How components interact:

```mermaid
graph TD
```

## Reverse Engineering Guidelines

1. **Entry Points**: Start analysis from the entry points listed above
2. **Core Logic**: Focus on classes with many methods
3. **Data Flow**: Follow data transformation functions
4. **Process Flows**: Use the flow diagrams for execution paths
5. **API Surface**: Public API functions reveal the interface

## Context for LLM

Maintain the identified architectural patterns and public API surface when suggesting changes.