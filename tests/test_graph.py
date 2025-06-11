from src.agent.graph import create_review_graph


def test_full_review_graph():
    graph = create_review_graph()
    pr = {"code": "def foo():\n    return 1"}
    result = graph.invoke({"pr": pr})
    assert "review" in result
    assert "risk" in result
    assert "language" in result
    assert "metrics" in result
