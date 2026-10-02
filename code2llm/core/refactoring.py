"""Refactoring analysis for code2llm."""

from pathlib import Path

from .config import Config
from .models import AnalysisResult
from .file_filter import FastFileFilter


class RefactoringAnalyzer:
    """Performs refactoring analysis on code."""

    def __init__(self, config: Config, file_filter: FastFileFilter):
        """Initialise with project config and file filter."""
        self.config = config
        self.file_filter = file_filter

    def perform_refactoring_analysis(self, result: AnalysisResult) -> None:
        """Perform deep analysis and detect code smells.

        Expensive operations (centrality, cycles, communities, vulture)
        are skipped when the corresponding config flags are set.  The
        ``fast_mode`` shortcut disables all of them at once via
        ``PerformanceConfig.apply_fast_mode()``.
        """
        perf = self.config.performance
        if perf.skip_refactoring_analysis:
            return

        if self.config.verbose:
            print("Performing refactoring analysis...")

        # 1. Calculate metrics (fan-in/fan-out) — always needed for TOON
        from ..analysis.call_graph import CallGraphExtractor

        cg_ext = CallGraphExtractor(self.config)
        cg_ext.result = result
        cg_ext._calculate_metrics()

        # 2. Build networkx graph for project-level analysis
        G = self._build_call_graph(result)

        # 3. Calculate Betweenness Centrality (Bottlenecks)
        if not perf.skip_centrality:
            self._calculate_centrality(G, result)

        # 4. Detect Circular Dependencies
        if not perf.skip_centrality:
            self._detect_cycles(G, result)

        # 5. Community Detection (Module groups)
        if not perf.skip_community_detection:
            self._detect_communities(G, result)

        # 6. Analyze coupling
        self._analyze_coupling(result)

        # 7. Detect code smells
        self._detect_smells(result)

        # 8. Dead code detection with vulture (slowest step — rescans all files)
        if not perf.skip_dead_code_detection:
            self._detect_dead_code(result)

        if self.config.verbose:
            print(f"  Detected {len(result.smells)} code smells")

    def _build_call_graph(self, result: AnalysisResult):
        """Build networkx call graph."""
        import networkx as nx

        G = nx.DiGraph()
        for func_name, func_info in result.functions.items():
            G.add_node(func_name)
            for callee in func_info.calls:
                G.add_edge(func_name, callee)
        return G

    def _calculate_centrality(self, call_graph, result: AnalysisResult) -> None:
        """Calculate betweenness centrality for bottleneck detection."""
        if len(call_graph) > 0:
            try:
                node_count = len(call_graph)
                k = None
                if node_count > 500:
                    if self.config.verbose:
                        print(
                            f"  Large graph ({node_count} nodes), using sampled centrality..."
                        )
                    ratio = 0.1 if node_count > 2000 else 0.2
                    k = min(int(node_count * ratio), 200)

                # Attempt fast native Rust computation first
                from ..analysis.native_bridge import native_betweenness_centrality

                nodes = [str(n) for n in call_graph.nodes()]
                edges = [(str(u), str(v)) for u, v in call_graph.edges()]
                centrality = native_betweenness_centrality(nodes, edges, k=k, normalized=True)

                if centrality is None:
                    # Fallback to pure NetworkX
                    import networkx as nx

                    if k is not None:
                        centrality = nx.betweenness_centrality(call_graph, k=k)
                    else:
                        centrality = nx.betweenness_centrality(call_graph)

                for func_name, score in centrality.items():
                    if func_name in result.functions:
                        result.functions[func_name].centrality = score
            except Exception as e:
                if self.config.verbose:
                    print(f"Error calculating centrality: {e}")

    def _detect_cycles(self, call_graph, result: AnalysisResult) -> None:
        """Detect circular dependencies."""
        try:
            # 1. Native Rust Tarjan SCC algorithm (linear time O(V + E), no node count limit)
            from ..analysis.native_bridge import native_detect_circular_dependencies

            nodes = [str(n) for n in call_graph.nodes()]
            edges = [(str(u), str(v)) for u, v in call_graph.edges()]
            native_cycles = native_detect_circular_dependencies(nodes, edges)

            if native_cycles is not None:
                if native_cycles:
                    result.metrics["project"] = result.metrics.get("project", {})
                    result.metrics["project"]["circular_dependencies"] = native_cycles
                return

            # 2. Pure Python fallback (NetworkX simple_cycles)
            if len(call_graph) > 1000:
                if self.config.verbose:
                    print(
                        f"  Skipping cycle detection for large graph ({len(call_graph)} nodes)"
                    )
                return
            import networkx as nx

            cycles = list(nx.simple_cycles(call_graph))
            if cycles:
                result.metrics["project"] = result.metrics.get("project", {})
                result.metrics["project"]["circular_dependencies"] = cycles
        except Exception as e:
            if self.config.verbose:
                print(f"Error detecting cycles: {e}")

    def _detect_communities(self, call_graph, result: AnalysisResult) -> None:
        """Detect communities (module groups)."""
        try:
            # Limit community detection for large graphs
            if len(call_graph) > 1000:
                if self.config.verbose:
                    print(
                        f"  Skipping community detection for large graph ({len(call_graph)} nodes)"
                    )
                return
            from networkx.algorithms import community

            # Using Louvain if available, otherwise greedy modularity
            if hasattr(community, "louvain_communities"):
                communities = community.louvain_communities(call_graph.to_undirected())
            else:
                communities = community.greedy_modularity_communities(
                    call_graph.to_undirected()
                )

            result.coupling["communities"] = [list(c) for c in communities]
        except Exception as e:
            if self.config.verbose:
                print(f"Error in community detection: {e}")

    def _analyze_coupling(self, result: AnalysisResult) -> None:
        """Analyze coupling between modules."""
        from ..analysis.coupling import CouplingAnalyzer

        coupling_analyzer = CouplingAnalyzer(result)
        coupling_analyzer.analyze()

    def _detect_smells(self, result: AnalysisResult) -> None:
        """Detect code smells."""
        from ..analysis.smells import SmellDetector

        smell_detector = SmellDetector(result)
        smell_detector.detect()

    def _detect_dead_code(self, result: AnalysisResult) -> None:
        """Use fast native reachability or vulture to find dead code and update reachability."""
        # 1. Fast in-memory graph reachability (O(V + E), zero disk I/O)
        from ..analysis.native_bridge import native_compute_reachability

        nodes = list(result.functions.keys())
        edges = [
            (fn, callee)
            for fn, info in result.functions.items()
            for callee in getattr(info, "calls", [])
        ]
        entry_points = getattr(result, "entry_points", [])
        reach_map = native_compute_reachability(nodes, edges, entry_points)
        if reach_map:
            for fn, status in reach_map.items():
                if fn in result.functions:
                    result.functions[fn].reachability = status

        # 2. Optional Vulture scan (if enabled and not in fast mode)
        if self.config.performance.skip_dead_code_detection:
            return

        if self.config.verbose:
            print("Detecting dead code with vulture...")

        try:
            import vulture

            v = vulture.Vulture(verbose=False)

            for py_file in Path(result.project_path).rglob("*.py"):
                if not self.file_filter.should_process(str(py_file)):
                    continue
                try:
                    content = py_file.read_text(encoding="utf-8", errors="ignore")
                    v.scan(content, filename=str(py_file))
                except Exception:
                    continue

            dead_code = v.get_unused_code()

            if self.config.verbose:
                print(f"  Vulture found {len(dead_code)} unused items")

            # Map unused code to our functions/classes with O(1) indexed lookup
            self._map_dead_code_to_items(dead_code, result)

            # Mark others as reachable if they are NOT orphans
            self._mark_reachable_items(result)

        except Exception as e:
            if self.config.verbose:
                print(f"Error in dead code detection: {e}")

    def _map_dead_code_to_items(self, dead_code, result: AnalysisResult) -> None:
        """Map vulture dead code to our functions/classes using indexed O(1) matching."""
        # Pre-build (resolved_file_path, line) lookup map to avoid O(N * M) scans
        func_lookup = {}
        for func_name, func_info in result.functions.items():
            key = (str(Path(func_info.file).resolve()), func_info.line)
            func_lookup[key] = func_info

        cls_lookup = {}
        for class_name, class_info in result.classes.items():
            key = (str(Path(class_info.file).resolve()), class_info.line)
            cls_lookup[key] = class_info

        for item in dead_code:
            item_path = str(Path(item.filename).resolve())
            item_lineno = getattr(item, "lineno", getattr(item, "first_lineno", 0))
            key = (item_path, item_lineno)

            if key in func_lookup:
                func_lookup[key].reachability = "unreachable"
            if key in cls_lookup:
                cls_lookup[key].reachability = "unreachable"

    def _mark_reachable_items(self, result: AnalysisResult) -> None:
        """Mark items as reachable if they are NOT orphans."""
        for func_name, func_info in result.functions.items():
            if func_info.reachability == "unknown":
                if func_info.called_by or func_name in result.entry_points:
                    func_info.reachability = "reachable"
