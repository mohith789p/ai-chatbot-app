# 🤖 AI Chatbot App

A conversational AI chatbot built with **LangGraph**, **Google Gemini**, and **Streamlit**. It supports multi-turn conversations with in-memory checkpointing via LangGraph's `InMemorySaver`.

---

## ✨ Features

- 💬 Multi-turn chat with persistent message history per session
- 🧠 Powered by Google Gemini (`gemini-3.6-flash`)
- 🔗 LangGraph state machine backend for structured conversation flow
- 🖥️ Clean Streamlit frontend with chat UI

---

## 🗂️ Project Structure

```
ai-chatbot-app/
├── langgraph_backend.py   # LangGraph graph definition & Gemini LLM setup
├── streamlit_frontend.py  # Streamlit chat UI
├── requirements.txt       # Python dependencies
├── .env                   # Your local secrets (not committed)
├── .env.example           # Template — copy this to .env
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-chatbot-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env   # macOS/Linux
copy .env.example .env  # Windows
```

Open `.env` and replace the placeholder with your real API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Run the app

```bash
streamlit run streamlit_frontend.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🔧 Configuration

| Variable         | Description                        | Required |
|------------------|------------------------------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key              | ✅ Yes   |

---

## 📦 Dependencies

| Package                   | Purpose                              |
|---------------------------|--------------------------------------|
| `langgraph`               | Graph-based conversation state machine |
| `langchain-google-genai`  | Google Gemini LLM integration        |
| `python-dotenv`           | Load `.env` environment variables    |
| `streamlit`               | Web UI framework                     |

---

## 🛠️ How It Works

1. **Backend** (`langgraph_backend.py`) — defines a `StateGraph` with a single `chat_node` that calls the Gemini LLM. `InMemorySaver` checkpoints conversation state by `thread_id`.
2. **Frontend** (`streamlit_frontend.py`) — renders the chat history and sends each user message to the LangGraph `chatbot` with a fixed `thread_id`, enabling multi-turn memory.

---

## 📄 License

MIT
