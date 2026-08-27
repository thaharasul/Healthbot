# AI Healthcare Chatbot 🩺

A simple web-based chatbot UI where users can type a general health-related question and get an AI-generated response. Built as a single Flask-rendered HTML page with a clean, card-style interface.

> **Note:** Only the frontend template (`index.html`) was provided for this README. I don't have the Flask backend (routes, model/API calls) — the sections below on setup and "how it works" are inferred from the template's `method="POST"` form and the `{% if answer %}` Jinja block. Update the setup steps once you share `app.py` (or equivalent).

## What it does

- Presents a single text area where a user can type a health-related question (e.g. *"I have a sore throat and mild fever. What should I do?"*)
- Submits the question via a POST form to the Flask backend
- Displays the AI's response in a highlighted answer box below the form, if one is returned

## Requirements (assumed)

- Python 3.9+
- Flask
- Whatever LLM/API client the backend uses (OpenAI, Gemini, Ollama, etc. — not shown in the provided files)

## Setup (assumed — update once backend is shared)

1. Install dependencies:
   ```bash
   pip install flask
   ```
   plus any AI SDK your backend uses (e.g. `openai`, `google-generativeai`, `requests` for Ollama).

2. Place this file in a `templates/` folder as `index.html` — Flask's `render_template` expects templates there by default.

3. Run your Flask app:
   ```bash
   python app.py
   ```

4. Open your browser to **http://127.0.0.1:5000**

## Usage

1. Type a general health question into the text box.
2. Click **Ask AI**.
3. The page reloads and shows the AI's response in the blue-bordered box below the form.

## ⚠️ Important disclaimer

This is a general-information tool, **not a substitute for professional medical advice, diagnosis, or treatment**. It should not be used for emergencies or urgent symptoms. Consider adding a visible disclaimer directly in the UI (and, ideally, some guardrails in the backend) reminding users to consult a licensed healthcare provider and to seek emergency care for serious or worsening symptoms.

## Project structure (assumed)

```
.
├── app.py              # Flask backend — not yet provided
└── templates/
    └── index.html      # Chat UI (this file)
```

## Possible improvements

- Add a loading indicator while waiting for the AI response
- Add conversation history / multi-turn support
- Add input validation or a length limit on the question field
- Add a persistent, visible medical disclaimer in the UI itself
