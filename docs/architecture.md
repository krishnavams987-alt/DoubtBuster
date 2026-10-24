# Architecture

DoubtBuster uses a single Streamlit deployment. `app.py` is the entry point; UI pages call reusable backend functions. The backend validates input, constructs a teaching prompt, calls the hosted LLM service, and returns text to the UI.

See `system_design.md` for the Mermaid architecture diagram and request flow.
