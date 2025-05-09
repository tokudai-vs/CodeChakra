from fastapi import APIRouter
from agent.review import ReviewAgent
from agent.risk_analysis import RiskAnalyzer

router = APIRouter()

review_agent = ReviewAgent()
risk_analyzer = RiskAnalyzer()

@router.post("/review")
async def review_pr(pr: dict):
    review_result = review_agent.review_pr(pr)
    return review_result

@router.post("/analyze-risk")
async def analyze_risk(pr: dict):
    risk_result = risk_analyzer.analyze_risk(pr)
    return risk_result

def setup_routes(app):
    app.include_router(router)