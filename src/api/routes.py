from fastapi import APIRouter
from agent import ReviewAgent, RiskAnalyzer, LanguageDetector, StaticAnalyzer

router = APIRouter()

review_agent = ReviewAgent()
risk_analyzer = RiskAnalyzer()
language_detector = LanguageDetector()
static_analyzer = StaticAnalyzer()

@router.post("/review")
async def review_pr(pr: dict):
    review_result = review_agent.review_pr(pr)
    return review_result

@router.post("/analyze-risk")
async def analyze_risk(pr: dict):
    risk_result = risk_analyzer.analyze_risk(pr)
    return risk_result

@router.post("/static-analysis")
async def perform_static_analysis(pr: dict):
    code = pr.get("code", "")
    language = language_detector.detect_language(code)
    metrics = static_analyzer.analyze_code(code, language)
    metrics["language"] = language
    return metrics


def setup_routes(app):
    app.include_router(router)
