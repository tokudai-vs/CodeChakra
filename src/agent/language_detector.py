from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

class LanguageDetector:
    """Detect the programming language of a code snippet."""

    def detect_language(self, code: str) -> str:
        """Return the detected language name or 'Unknown'."""
        try:
            lexer = guess_lexer(code)
            return lexer.name
        except ClassNotFound:
            return "Unknown"
