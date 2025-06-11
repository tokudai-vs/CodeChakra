from fastapi import APIRouter, Header, HTTPException
from agent import ReviewAgent, RiskAnalyzer, LanguageDetector, StaticAnalyzer
from agent.graph import create_review_graph
from integrations.github import GitHubClient
from integrations.bitbucket import BitbucketClient

router = APIRouter()

review_agent = ReviewAgent()
risk_analyzer = RiskAnalyzer()
language_detector = LanguageDetector()
static_analyzer = StaticAnalyzer()
review_graph = create_review_graph()
github_client = GitHubClient()
bitbucket_client = BitbucketClient()


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


@router.post("/webhook/github")
async def github_webhook(payload: dict, x_github_event: str = Header(None)):
    if x_github_event != "pull_request" or payload.get("action") != "opened":
        return {"status": "ignored"}
    try:
        repo = payload["repository"]["full_name"]
        pr_number = payload["number"] if "number" in payload else payload["pull_request"]["number"]
        diff = github_client.fetch_pr_diff(repo, pr_number)
        result = review_graph.invoke({"pr": {"code": diff}})
        return result
    except Exception as exc:  # pragma: no cover - network failures
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/webhook/bitbucket")
async def bitbucket_webhook(payload: dict, x_event_key: str = Header(None)):
    if x_event_key != "pullrequest:created":
        return {"status": "ignored"}
    try:
        repo = payload["repository"]["full_name"]
        pr_id = payload["pullrequest"]["id"]
        diff = bitbucket_client.fetch_pr_diff(repo, pr_id)
        result = review_graph.invoke({"pr": {"code": diff}})
        return result
    except Exception as exc:  # pragma: no cover - network failures
        raise HTTPException(status_code=400, detail=str(exc))


def setup_routes(app):
    app.include_router(router)
