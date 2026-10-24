from backend.services.llm_service import ask_llm

def answer_doubt(question: str, subject: str, topic: str, level: str, mode: str,
                 language: str, attempt: str, api_key: str, model: str) -> str:
    if mode == "Hint first":
        mode_instruction = (
            "Give one useful hint and a short explanation of why it helps. Do not reveal "
            "the complete final answer immediately. End with one question inviting the student to try."
        )
    elif mode == "Verify my answer":
        mode_instruction = (
            "Evaluate the student's attempt. Identify what is correct, what is incorrect or missing, "
            "and how to verify it. If no attempt was supplied, ask them to provide one before judging it; "
            "you may still explain the method without pretending to verify an absent answer."
        )
    elif mode == "Practice question with answer key":
        mode_instruction = "Create one relevant practice problem, then provide a clearly separated worked solution and answer key."
    else:
        mode_instruction = (
            "Give a logically ordered step-by-step explanation, define important terms, show intermediate "
            "calculations or code reasoning, and state the final result only after the steps."
        )

    prompt = f"""
Student context:
- Subject: {subject}
- Topic: {topic or "Not specified"}
- Skill level: {level}
- Preferred language: {language}
- Help mode: {mode}

Student question:
{question}

Student's attempt (if provided):
{attempt or "No attempt provided."}

Instructions:
{mode_instruction}

Teaching requirements:
- Use clear, student-friendly language appropriate to the stated skill level.
- For programming, explain relevant lines, likely errors, a correction, and expected output where possible.
- For mathematics, show intermediate steps and check arithmetic where possible.
- For ML/NLP, define terms and use a practical example.
- Ask one brief follow-up question to check understanding when suitable.
- Do not claim that code was run or a calculation was independently verified unless it actually was.
- If the question is ambiguous, state the ambiguity and ask for clarification.
- Clearly mark assumptions and uncertainty. Do not fabricate references.
"""
    return ask_llm(prompt, api_key=api_key, model=model)
