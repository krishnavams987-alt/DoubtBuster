from unittest.mock import patch
from backend.core.pipeline import answer_doubt

@patch("backend.core.pipeline.ask_llm", return_value="A helpful explanation.")
def test_answer_doubt_builds_response(mock_llm):
    result = answer_doubt(
        question="What is a loop?", subject="Programming", topic="Loops",
        level="Beginner", mode="Step-by-step explanation", language="English",
        attempt="", api_key="test-key", model="test-model"
    )
    assert result == "A helpful explanation."
    assert mock_llm.called
