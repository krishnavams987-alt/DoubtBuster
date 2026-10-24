import streamlit as st

st.set_page_config(page_title="Learning History | DoubtBuster", page_icon="📚")
st.title("📚 Learning History")
st.info("Starter MVP: conversation history is kept for the current browser session only. Persistent student history is not enabled yet.")
if st.session_state.get("last_question"):
    st.markdown("**Most recent question**")
    st.write(st.session_state["last_question"])
    st.markdown("**Most recent explanation**")
    st.markdown(st.session_state.get("last_result", "No explanation available."))
else:
    st.write("Ask a question on the Home page to see it here during this session.")
