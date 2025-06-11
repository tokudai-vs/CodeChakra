class ReviewAgent:
    """Simple PR review agent with basic issue detection."""

    def review_pr(self, pr):
        """Analyze the provided pull request object or dict."""
        code = getattr(pr, "code", "") if not isinstance(pr, dict) else pr.get("code", "")
        report = {
            "performance_issues": [],
            "logic_issues": [],
            "security_issues": [],
            "suggestions": [],
        }

        if "time.sleep" in code:
            report["performance_issues"].append("Potential performance issue: time.sleep detected")

        if "if" in code and "=" in code.split("if", 1)[1].split(":")[0] and "==" not in code.split("if", 1)[1].split(":")[0]:
            report["logic_issues"].append("Possible assignment in conditional")

        if "eval(" in code:
            report["security_issues"].append("Use of eval may be unsafe")

        return report
