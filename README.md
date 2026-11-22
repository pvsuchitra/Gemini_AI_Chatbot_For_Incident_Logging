# Gemini AI Chatbot for Incident Logging

A first-line (L1) AI incident assistant built with **Python**, **Streamlit**, and the **Google Gemini API**. It guides users through structured incident logging—capturing impact, severity, and initial troubleshooting steps—to resolve routine software and system issues quickly and escalate critical cases to human agents with complete context.

## Key Features
- **Structured Incident Intake:** Collects essential triage details including issue description, impact, and severity.
- **Guided L1 Troubleshooting:** Walks users through initial diagnostic steps before routing to support.
- **Factual Response Tuning:** Configured with a low/factual temperature to minimize hallucinations during technical triage.
- **Smart Escalation:** Ensures human support agents receive clean, structured incident summaries for critical issues.
- **Interactive Web UI:** Clean chat interface powered by Streamlit.

## Tech Stack
- **Language:** Python
- **LLM:** Google Gemini API
- **Frontend / UI:** Streamlit
- **Dev Environment:** VS Code Dev Containers (`.devcontainer`)

## Project Structure
```text
Gemini_AI_Chatbot_For_Incident_Logging/
├── .devcontainer/        # Dev container configuration
├── .gitignore            # Git ignore rules
├── gemini_chat_bot.py    # Core Gemini API chatbot logic
├── streamlit_app.py      # Streamlit web application entry point
├── requirements.txt      # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- A Google Gemini API key

### Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/pvsuchitra/Gemini_AI_Chatbot_For_Incident_Logging.git](https://github.com/pvsuchitra/Gemini_AI_Chatbot_For_Incident_Logging.git)
   cd Gemini_AI_Chatbot_For_Incident_Logging
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your Gemini API key (via environment variable or `.streamlit/secrets.toml`, depending on your local setup):
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
   *(On Windows Command Prompt: `set GEMINI_API_KEY=your_api_key_here`)*

5. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Future Improvements
- Export structured incident logs directly to ticketing systems (e.g., ServiceNow, Jira) or JSON/CSV.
- Add RAG (Retrieval-Augmented Generation) over internal SOPs and runbooks for organization-specific troubleshooting.
- Implement human-in-the-loop (HITL) approval guardrails before automated ticket creation.
