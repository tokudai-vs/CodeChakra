from fastapi.testclient import TestClient
from src.main import create_app


class DummyGitHubClient:
    def fetch_pr_diff(self, repo, pr_number):
        return "diff --git a/foo.py b/foo.py\n+print('hi')"


class DummyBitbucketClient:
    def fetch_pr_diff(self, repo, pr_number):
        return "diff --git a/bar.py b/bar.py\n+print('hi')"


def test_github_webhook(monkeypatch):
    app = create_app()
    from src.api import routes
    monkeypatch.setattr(routes, "github_client", DummyGitHubClient())
    client = TestClient(app)
    payload = {
        "action": "opened",
        "number": 1,
        "repository": {"full_name": "owner/repo"},
        "pull_request": {"number": 1},
    }
    headers = {"X-GitHub-Event": "pull_request"}
    response = client.post("/webhook/github", json=payload, headers=headers)
    assert response.status_code == 200
    assert "review" in response.json()


def test_bitbucket_webhook(monkeypatch):
    app = create_app()
    from src.api import routes
    monkeypatch.setattr(routes, "bitbucket_client", DummyBitbucketClient())
    client = TestClient(app)
    payload = {
        "repository": {"full_name": "owner/repo"},
        "pullrequest": {"id": 1},
    }
    headers = {"X-Event-Key": "pullrequest:created"}
    response = client.post("/webhook/bitbucket", json=payload, headers=headers)
    assert response.status_code == 200
    assert "review" in response.json()
