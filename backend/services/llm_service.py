from openai import OpenAI

def ask_llm(prompt: str, api_key: str, model: str = "gpt-4o-mini") -> str:
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your local .env file or "
            "Streamlit Community Cloud app Settings → Secrets. You can still review "
            "the project UI, but AI answers require an API key."
        )
    client = OpenAI(api_key=api_key, timeout=45.0, max_retries=2)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are DoubtBuster, a careful and supportive tutor for GMRIT undergraduate students. Teach reasoning rather than merely giving answers. Be transparent about uncertainty. Never invent citations or claim code was executed when it was not."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    content = response.choices[0].message.content
    return content.strip() if content else "I couldn't generate a response. Please rephrase your question."
