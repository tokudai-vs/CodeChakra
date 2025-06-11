import lizard

class StaticAnalyzer:
    """Perform static analysis on source code using lizard."""

    def analyze_code(self, code: str, language: str | None = None) -> dict:
        """Analyze code and return basic metrics."""
        filename = f"code.{language.lower()}" if language else "code.txt"
        analysis = lizard.analyze_file.analyze_source_code(filename, code)
        return {
            "nloc": analysis.nloc,
            "function_count": len(analysis.function_list),
            "average_cyclomatic_complexity": analysis.average_cyclomatic_complexity,
        }
