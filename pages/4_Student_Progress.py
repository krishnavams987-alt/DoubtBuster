import streamlit as st

st.set_page_config(page_title="Student Progress | DoubtBuster", page_icon="📈")
st.title("📈 Student Progress")
st.info("Persistent progress analytics are not enabled in this starter build. The current app does not save student records to a database.")
st.metric("Questions asked this session", "1" if st.session_state.get("last_question") else "0")
if st.session_state.get("last_subject"):
    st.write("Most recent subject:", st.session_state["last_subject"])
