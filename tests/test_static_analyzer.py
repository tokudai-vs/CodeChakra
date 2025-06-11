from src.agent.static_analyzer import StaticAnalyzer


def test_analyze_simple_code():
    code = "def foo():\n    return 1"
    analyzer = StaticAnalyzer()
    result = analyzer.analyze_code(code, language="py")
    assert result["function_count"] == 1
    assert result["nloc"] > 0
