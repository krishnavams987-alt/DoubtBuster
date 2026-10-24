# DoubtBuster — GMRIT Student Doubt-Solving AI Tutor

DoubtBuster is a Streamlit-based educational assistant designed to help undergraduate students understand programming, mathematics, machine learning, deep learning, NLP, and data-science concepts through hints and step-by-step explanations.

## Features in this starter MVP
- Subject, topic, difficulty, and learning-mode selection
- Hint-first, step-by-step, and answer-verification modes
- Conversational AI explanation through the OpenAI API
- Text-based problem upload (`.txt`, `.py`, `.csv`, `.md`)
- Practice-question generation
- Basic validation and readable missing-key errors
- Starter multipage interface for history, practice, materials, and progress

## Technology
Python, Streamlit, OpenAI API, SymPy, Pandas, pytest.

## Project structure
- `app.py`: Streamlit entry point
- `backend/`: configuration, LLM service, tutor pipeline, validation
- `pages/`: optional Streamlit pages
- `tests/`: automated tests
- `docs/`: project documentation

## Prerequisites
- Python 3.11 or 3.12
- Git
- An OpenAI API key for AI responses

## Run locally (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```
Edit `.env` and replace the placeholder with your own API key, then run:
```powershell
streamlit run app.py
```
The app opens at `http://localhost:8501`.

## Run tests
```powershell
pytest -q
```

## Deploy to Streamlit Community Cloud
1. Push this repository to GitHub.
2. Sign in at https://share.streamlit.io and choose **New app**.
3. Select the repository, branch, and `app.py` as the main file.
4. In app settings, add secrets in TOML format:
```toml
OPENAI_API_KEY = "your-real-key"
OPENAI_MODEL = "gpt-4o-mini"
```
5. Deploy and test the live URL.

Never commit `.env`, `.streamlit/secrets.toml`, API keys, student records, or private course materials.

## Known limitations
- AI responses require a valid OpenAI API key and network access.
- Uploaded files are treated as text; this starter does not parse PDF or PowerPoint.
- Learning history is session-only; persistent SQLite tracking is not yet implemented.
- Course-material RAG, source citations, adaptive learning, faculty analytics, and secure code execution are future extensions.
- The application does not actually execute student code and must not claim to have verified runtime output.

## Responsible use
AI can make mistakes. Verify important calculations and code behavior independently. Use approved learning materials only and do not submit unverified AI output as your own work.
