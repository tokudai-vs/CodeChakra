from fastapi import APIRouter
from agent import ReviewAgent, RiskAnalyzer, LanguageDetector, StaticAnalyzer
from agent.graph import create_review_graph

router = APIRouter()

review_agent = ReviewAgent()
risk_analyzer = RiskAnalyzer()
language_detector = LanguageDetector()
static_analyzer = StaticAnalyzer()
review_graph = create_review_graph()


@router.post("/review")
async def review_pr(pr: dict):
    return review_agent.review_pr(pr)


@router.post("/analyze-risk")
async def analyze_risk(pr: dict):
    return risk_analyzer.analyze_risk(pr)


@router.post("/static-analysis")
async def perform_static_analysis(pr: dict):
    code = pr.get("code", "")
    language = language_detector.detect_language(code)
    metrics = static_analyzer.analyze_code(code, language)
    metrics["language"] = language
    return metrics


@router.post("/full-review")
async def perform_full_review(pr: dict):
    return review_graph.invoke({"pr": pr})


def setup_routes(app):
    app.include_router(router)
