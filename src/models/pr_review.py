class PRReview:
    def __init__(self, pr_id, review_comments=None):
        self.pr_id = pr_id
        self.review_comments = review_comments if review_comments is not None else []

    def add_comment(self, comment):
        self.review_comments.append(comment)

    def get_review_summary(self):
        return {
            "pr_id": self.pr_id,
            "comments": self.review_comments
        }