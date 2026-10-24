
from google import genai


def ask_llm(
    prompt: str,
    api_key: str,
    model: str = "gemini-2.5-flash",
) -> str:
    """Generate a tutoring response using the Gemini API."""

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. Add it to your .env file "
            "or Streamlit Cloud Secrets."
        )

    client = genai.Client(api_key=api_key)

    full_prompt = f"""
You are DoubtBuster, an AI tutor for GMRIT undergraduate students.

Your responsibilities:
- Explain concepts in clear, simple English.
- Teach step by step instead of only giving the final answer.
- Help students understand programming, mathematics, and AI topics.
- Explain code errors and suggest corrections.
- Give examples when useful.
- Be honest when you are uncertain.
- Never invent citations or claim code was executed if it was not.

Student's question:
{prompt}
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=full_prompt,
        )

        answer = response.text

        if not answer:
            raise RuntimeError(
                "Gemini returned an empty response. Please try again."
            )

        return answer.strip()

    finally:
        client.close()
