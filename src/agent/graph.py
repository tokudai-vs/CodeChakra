from langgraph.graph import Graph, END

from .review import ReviewAgent
from .risk_analysis import RiskAnalyzer
from .language_detector import LanguageDetector
from .static_analyzer import StaticAnalyzer


def create_review_graph() -> callable:
    review_agent = ReviewAgent()
    risk_analyzer = RiskAnalyzer()
    language_detector = LanguageDetector()
    static_analyzer = StaticAnalyzer()

    graph = Graph()

    def review_step(data: dict) -> dict:
        data["review"] = review_agent.review_pr(data.get("pr", {}))
        return data

    def risk_step(data: dict) -> dict:
        data["risk"] = risk_analyzer.analyze_risk(data.get("pr", {}))
        return data

    def language_step(data: dict) -> dict:
        code = data.get("pr", {}).get("code", "")
        data["language"] = language_detector.detect_language(code)
        return data

    def static_step(data: dict) -> dict:
        code = data.get("pr", {}).get("code", "")
        data["metrics"] = static_analyzer.analyze_code(code, data.get("language"))
        return data

    graph.add_node("review", review_step)
    graph.add_node("risk", risk_step)
    graph.add_node("language", language_step)
    graph.add_node("static", static_step)

    graph.set_entry_point("review")

    graph.add_edge("review", "risk")
    graph.add_edge("risk", "language")
    graph.add_edge("language", "static")
    graph.add_edge("static", END)

    return graph.compile()
