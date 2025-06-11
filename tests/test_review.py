import unittest
from src.agent.review import ReviewAgent
from src.models.pr_review import PRReview


class TestReviewAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ReviewAgent()
        self.sample_pr = PRReview(pr_id="123", review_comments=[])

    def test_review_pr_performance(self):
        self.sample_pr.code = "def slow_function():\n    time.sleep(5)"
        result = self.agent.review_pr(self.sample_pr)
        self.assertGreater(len(result["performance_issues"]), 0)

    def test_review_pr_logic(self):
        self.sample_pr.code = "if a = 5: print(a)"
        result = self.agent.review_pr(self.sample_pr)
        self.assertGreater(len(result["logic_issues"]), 0)

    def test_review_pr_security(self):
        self.sample_pr.code = "eval(user_input)"
        result = self.agent.review_pr(self.sample_pr)
        self.assertGreater(len(result["security_issues"]), 0)


if __name__ == "__main__":
    unittest.main()
