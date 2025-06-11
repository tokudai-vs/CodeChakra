from src.agent.language_detector import LanguageDetector


def test_detect_python():
    code = """\
import os

def foo():
    return 42

if __name__ == '__main__':
    print(foo())
"""
    detector = LanguageDetector()
    language = detector.detect_language(code)
    assert language != "Unknown"
    assert "python" in language.lower()
