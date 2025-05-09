import unittest
from src.agent.review import ReviewAgent
from src.models.pr_review import PRReview

class TestReviewAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ReviewAgent()
        self.sample_pr = PRReview(pr_id="123", review_comments=[])

    def test_review_pr_performance(self):
        # Simulate a PR with performance issues
        self.sample_pr.code = "def slow_function(): time.sleep(5)"
        result = self.agent.review_pr(self.sample_pr)
        self.assertIn("performance issue", result)

    def test_review_pr_logic(self):
        # Simulate a PR with logic issues
        self.sample_pr.code = "if a = 5: print(a)"
        result = self.agent.review_pr(self.sample_pr)
        self.assertIn("logic error", result)

    def test_review_pr_security(self):
        # Simulate a PR with security issues
        self.sample_pr.code = "eval(user_input)"
        result = self.agent.review_pr(self.sample_pr)
        self.assertIn("security risk", result)

if __name__ == '__main__':
    unittest.main()