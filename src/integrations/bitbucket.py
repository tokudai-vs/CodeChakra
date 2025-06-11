import os
import requests


class BitbucketClient:
    """Simple Bitbucket API client for fetching pull request data."""

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("BITBUCKET_TOKEN")
        self.base_url = "https://api.bitbucket.org/2.0"

    def _headers(self) -> dict:
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def fetch_pr_diff(self, repo_full_name: str, pr_id: int) -> str:
        """Return the diff for the pull request as text."""
        url = f"{self.base_url}/repositories/{repo_full_name}/pullrequests/{pr_id}/diff"
        response = requests.get(url, headers=self._headers(), timeout=10)
        response.raise_for_status()
        return response.text
