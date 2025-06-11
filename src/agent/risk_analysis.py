class RiskAnalyzer:
    """Analyze pull requests for potential risks."""

    def analyze_risk(self, pr):
        code = getattr(pr, "code", "") if not isinstance(pr, dict) else pr.get("code", "")
        risk_assessment = {
            "risk_level": "low",
            "issues": []
        }
        if "eval(" in code:
            risk_assessment["risk_level"] = "medium"
            risk_assessment["issues"].append("Use of eval may be risky")
        return risk_assessment
