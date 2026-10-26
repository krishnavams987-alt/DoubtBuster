
import streamlit as st
from backend.config import get_setting
from backend.core.pipeline import answer_doubt
from backend.utils.validators import validate_question

# Use the model ID recommended by your error message.
DEFAULT_MODEL = "gemini-3.8-flash"

st.set_page_config(
    page_title="DoubtBuster | GMRIT AI Tutor",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main-header {
    padding: 1.2rem 1.4rem;
    border-radius: 18px;
    background: linear-gradient(120deg,#173b72,#5b55c7);
    color: white;
    margin-bottom: 1rem;
}
.main-header h1 {color:white; margin:0;}
.main-header p {color:#e9edff; margin:.35rem 0 0 0;}
.small-note {color:#6b7280; font-size:.9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-header">'
    '<h1>🎓 DoubtBuster</h1>'
    '<p>Your GMRIT learning companion — understand the steps, '
    'not just the answer.</p></div>',
    unsafe_allow_html=True
)

# Read the model setting once.
MODEL_NAME = get_setting("GEMINI_MODEL", DEFAULT_MODEL)

with st.sidebar:
    st.header("Learning preferences")

    subject = st.selectbox(
        "Subject",
        [
            "Programming", "Mathematics", "Machine Learning",
            "Deep Learning", "NLP", "Data Science", "Other"
        ]
    )

    topic = st.text_input(
        "Topic (optional)",
        placeholder="e.g., recursion, derivatives, tokenization"
    )

    level = st.select_slider(
        "Your level",
        options=["Beginner", "Intermediate", "Advanced"],
        value="Beginner"
    )

    mode = st.radio(
        "Help mode",
        ["Hint first", "Step-by-step explanation", "Verify my answer"]
    )

    language = st.selectbox(
        "Explanation language",
        ["English", "Simple English"]
    )

    st.divider()
    st.caption("Tip: Try solving each step before revealing the next one.")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("Ask your doubt")

    question = st.text_area(
        "Question or problem",
        height=160,
        placeholder="Paste a question, code snippet, or maths problem here..."
    )

    uploaded = st.file_uploader(
        "Optional: upload a problem statement",
        type=["txt", "py", "csv", "md"],
        help="Text-based files are supported."
    )

    user_attempt = st.text_area(
        "Your attempt (optional)",
        height=90,
        placeholder="What have you tried? Paste your answer or code here."
    )

    ask = st.button(
        "✨ Help me understand",
        type="primary",
        use_container_width=True
    )

with col2:
    st.subheader("How DoubtBuster helps")

    st.info(
        "1. Starts with a hint when requested\n\n"
        "2. Breaks difficult ideas into steps\n\n"
        "3. Helps debug code and check reasoning\n\n"
        "4. Creates practice questions"
    )

    st.warning(
        "AI can make mistakes. Independently verify important "
        "calculations and code outputs."
    )

# Main doubt-solving feature
if ask:
    uploaded_text = ""

    if uploaded:
        uploaded_text = uploaded.getvalue().decode(
            "utf-8",
            errors="replace"
        )

    combined_question = question.strip()

    if uploaded_text:
        combined_question = (
            combined_question
            + "\n\nUploaded problem:\n"
            + uploaded_text[:12000]
        ).strip()

    try:
        validate_question(combined_question)

        with st.spinner("Working through your doubt..."):
            result = answer_doubt(
                question=combined_question,
                subject=subject,
                topic=topic.strip(),
                level=level,
                mode=mode,
                language=language,
                attempt=user_attempt.strip(),
                api_key=get_setting("GEMINI_API_KEY"),
                model=MODEL_NAME,
            )

        st.session_state["last_question"] = combined_question
        st.session_state["last_result"] = result
        st.session_state["last_subject"] = subject

    except ValueError as exc:
        st.warning(str(exc))

    except Exception as exc:
        st.error(f"Unable to answer right now: {exc}")

# Display the latest explanation
if st.session_state.get("last_result"):
    st.divider()
    st.subheader("Your learning guide")
    st.markdown(st.session_state["last_result"])

    st.caption(
        "Use this explanation as a learning aid, not as an "
        "unquestioned source of truth."
    )

    with st.expander("Generate a similar practice question"):
        if st.button("Create practice question"):
            try:
                with st.spinner("Creating a practice question..."):
                    practice = answer_doubt(
                        question=(
                            "Create one similar practice problem based "
                            "on this question. Include the problem first, "
                            "then a separate answer key with a worked "
                            "solution. Original question:\n"
                            + st.session_state.get("last_question", "")
                        ),
                        subject=st.session_state.get(
                            "last_subject", subject
                        ),
                        topic=topic.strip(),
                        level=level,
                        mode="Practice question with answer key",
                        language=language,
                        attempt="",
                        api_key=get_setting("GEMINI_API_KEY"),
                        model=MODEL_NAME,
                    )

                st.markdown(practice)

            except Exception as exc:
                st.error(
                    f"Could not generate practice question: {exc}"
                )

st.markdown("---")
st.markdown(
    '<p class="small-note">DoubtBuster • GMRIT Student Project '
    '• Streamlit starter MVP</p>',
    unsafe_allow_html=True
)
