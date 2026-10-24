import streamlit as st
from backend.config import get_setting
from backend.core.pipeline import answer_doubt

st.set_page_config(page_title="Practice | DoubtBuster", page_icon="🧠")
st.title("🧠 Practice Question Generator")
subject = st.selectbox("Subject", ["Programming", "Mathematics", "Machine Learning", "Deep Learning", "NLP", "Data Science"])
topic = st.text_input("Topic", placeholder="e.g., Python loops")
level = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])
if st.button("Generate practice problem", type="primary"):
    if not topic.strip():
        st.warning("Enter a topic first.")
    else:
        try:
            with st.spinner("Creating a practice problem…"):
                result = answer_doubt(
                    question=f"Create one {level.lower()} practice question about {topic}. Include a worked solution and answer key after the question.",
                    subject=subject, topic=topic, level=level,
                    mode="Practice question with answer key", language="English", attempt="",
                    api_key=get_setting("OPENAI_API_KEY"),
                    model=get_setting("OPENAI_MODEL", "gpt-4o-mini"),
                )
            st.markdown(result)
        except Exception as exc:
            st.error(str(exc))
