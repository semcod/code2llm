"""Engine for generating refactoring prompts using Jinja2 templates."""

import os
import jinja2
import tiktoken
from tree_sitter import Language, Parser
import tree_sitter_python
from typing import Dict, Any, Optional
from code2llm.core.models import AnalysisResult, CodeSmell


class PromptEngine:
    """Generate refactoring prompts from analysis results and detected smells."""

    def __init__(self, result: AnalysisResult, template_dir: Optional[str] = None):
        """Initialise the prompt engine with analysis result and optional template directory."""
        if template_dir is None:
            # Default to templates directory relative to this file
            template_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "templates"
            )

        self.result = result
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

        # Initialize tiktoken for context management
        try:
            self.encoding = tiktoken.get_encoding(
                "cl100k_base"
            )  # GPT-4/3.5-turbo encoding
        except Exception:
            self.encoding = None

        # Initialize tree-sitter for precision extraction
        try:
            self.PY_LANGUAGE = Language(tree_sitter_python.language())
            self.parser = Parser(self.PY_LANGUAGE)
        except Exception:
            self.parser = None

    def generate_prompts(self) -> Dict[str, str]:
        """Generate a prompt for each detected code smell."""
        prompts = {}

        for i, smell in enumerate(self.result.smells):
            prompt = self._generate_prompt_for_smell(smell)
            if prompt:
                # Truncate prompt if it exceeds token limit (e.g., 4000 tokens)
                if self.encoding:
                    tokens = self.encoding.encode(prompt)
                    if len(tokens) > 4000:
                        prompt = (
                            self.encoding.decode(tokens[:3800])
                            + "\n\n... (prompt truncated due to length) ..."
                        )

                # Use a unique name for each prompt
                filename = f"{i + 1:02d}_{smell.type}_{smell.name.lower().replace(' ', '_').replace(':', '')}.md"
                prompts[filename] = prompt
        return prompts

    def _generate_prompt_for_smell(self, smell: CodeSmell) -> Optional[str]:
        """Generate a single prompt from a CodeSmell."""
        template_name = self._get_template_for_type(smell.type)
        if not template_name:
            return None

        try:
            template = self.env.get_template(template_name)
            context = self._build_context_for_smell(smell)
            return template.render(**context)
        except Exception as e:
            print(f"Error generating prompt for {smell.name}: {e}")
            return None

    def _get_template_for_type(self, smell_type: str) -> Optional[str]:
        """Map smell type to Jinja2 template filename."""
        mapping = {
            "god_function": "extract_method.md",
            "feature_envy": "move_method.md",
            "data_clump": "move_method.md",
            "shotgun_surgery": "extract_method.md",
            "bottleneck": "extract_method.md",
            "circular_dependency": "move_method.md",
        }
        return mapping.get(smell_type)

    def _get_smell_metrics(self, smell: CodeSmell) -> dict:
        """Look up metrics for the function identified by smell name."""
        target = smell.name.split(": ")[-1]
        metrics = self.result.metrics.get(target, {})
        if not metrics and "function" in smell.context:
            metrics = self.result.metrics.get(smell.context["function"], {})
        return metrics

    def _get_smell_mutations(self, smell: CodeSmell) -> tuple:
        """Return (mutations list, summary string) for the smell's target function."""
        target = smell.name.split(": ")[-1]
        mutations = [
            m for m in self.result.mutations
            if m.scope in (target, smell.context.get("function"))
        ]
        summary = f"{len(mutations)} modifications recorded: {', '.join(set(m.variable for m in mutations[:5]))}..."
        return mutations, summary

    @staticmethod
    def _get_target_module(smell: CodeSmell) -> str:
        """Return target module name for feature_envy smells."""
        if smell.type == "feature_envy":
            return smell.context.get("foreign_mutations", ["other_module"])[0].split(".")[0]
        return "other_module"

    def _get_reachability(self, target: str) -> str:
        """Return reachability for a function, or 'unknown' if not available."""
        func = self.result.functions.get(target)
        if hasattr(func, "reachability"):
            return func.reachability
        return "unknown"

    def _build_context_for_smell(self, smell: CodeSmell) -> Dict[str, Any]:
        """Prepare context data for the Jinja2 template."""
        source_code = self._get_source_context(smell.file, smell.line)
        metrics = self._get_smell_metrics(smell)
        mutations, mutations_summary = self._get_smell_mutations(smell)
        target = smell.name.split(": ")[-1]
        foreign = smell.context.get("foreign_mutations", [])
        return {
            "target_function": target,
            "reason": smell.description,
            "metrics": metrics,
            "mutations_context": mutations_summary,
            "source_file": smell.file,
            "start_line": smell.line,
            "end_line": smell.line + 20,
            "source_code": source_code,
            "instruction": self._get_instruction_for_smell(smell),
            "source_module": smell.file.split("/")[-1].replace(".py", ""),
            "target_module": self._get_target_module(smell),
            "foreign_mutations": ", ".join(foreign),
            "foreign_mutations_context": f"This code mutates state in {', '.join(set(v.split('.')[0] for v in foreign if '.' in v))}",
            "dependencies": ", ".join(set(m.variable for m in mutations if "." in m.variable)),
            "reachability": self._get_reachability(target),
        }

    def _get_source_context(
        self, file_path: str, start_line: int, max_lines: int = 50
    ) -> str:
        """Read source code lines from a file."""
        if not os.path.exists(file_path):
            return "# Source file not found."

        try:
            with open(file_path, "r") as f:
                content = f.read()

            # If tree-sitter is available, use it to accurately find function boundaries
            if self.parser and "method" not in file_path:  # simplified check
                tree = self.parser.parse(bytes(content, "utf8"))
                root_node = tree.root_node

                # Simple function extraction using tree-sitter
                # (Ideally we'd search for the function node at start_line)
                lines = content.splitlines()
                start = max(0, start_line - 1)
                end = min(len(lines), start + max_lines)
                return "\n".join(lines[start:end])
            else:
                lines = content.splitlines()
                start = max(0, start_line - 1)
                end = min(len(lines), start + max_lines)
                return "\n".join(lines[start:end])
        except Exception as e:
            return f"# Error reading source: {e}"

    def _get_instruction_for_smell(self, smell: CodeSmell) -> str:
        """Generate specific instruction based on smell type."""
        if smell.type == "god_function":
            return f"Wyekstrahuj mniejsze, spójne metody z funkcji {smell.name.split(': ')[-1]}. Skup się na wydzieleniu operacji o największej liczbie mutacji."
        elif smell.type == "feature_envy":
            return f"Przenieś metodę {smell.name.split(': ')[-1]} do modułu, który posiada większość używanych w niej danych. Zmniejsz coupling między modułami."
        elif smell.type == "bottleneck":
            return f"Funkcja {smell.name.split(': ')[-1]} jest wąskim gardłem strukturalnym. Wyekstrahuj z niej niezależne części pomocnicze, aby ułatwić zrozumienie przepływu."
        elif smell.type == "circular_dependency":
            return "Wykryto cykl zależności. Przenieś część logiki do nowego modułu lub użyj interfejsu, aby przerwać cykl."
        return "Zrefaktoryzuj ten fragment kodu, aby poprawić jego strukturę i zmniejszyć złożoność."
