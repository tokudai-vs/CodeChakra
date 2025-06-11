import os
import requests


class GitHubClient:
    """Simple GitHub API client for fetching pull request data."""

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"

    def _headers(self) -> dict:
        headers = {"Accept": "application/vnd.github.v3+json"}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    def fetch_pr_diff(self, repo_full_name: str, pr_number: int) -> str:
        """Return the diff for the pull request as text."""
        url = f"{self.base_url}/repos/{repo_full_name}/pulls/{pr_number}.patch"
        response = requests.get(url, headers=self._headers(), timeout=10)
        response.raise_for_status()
        return response.text
