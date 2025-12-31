# AI Chatbot Agents with LangChain, FastAPI & Streamlit

This project is a modular framework for building conversational AI agents using:

- **FastAPI** (Backend API)
- **Streamlit** (Frontend chat UI)
- **LangChain** (Agent orchestration)
- **Groq / OpenAI models**
- **Tavily Web Search Tool (optional)**

It allows users to configure an AI agent, select a model provider, choose a model, enable web search, and interact with the agent in real time.

---

## 🚀 Features

### ✔ Streamlit UI  
- Choose provider (Groq / OpenAI)  
- Select models (LLaMA / Mixtral / GPT-4o-mini)  
- Define system prompt  
- Enable/disable web search  
- Submit queries & view responses  

### ✔ FastAPI Backend  
- Validates model names  
- Calls `get_response_from_ai_agent()`  
- Handles system prompts, search toggle & conversation state  

### ✔ AI Agent (LangChain)  
- Supports multiple LLM providers  
- Optional Tavily search tool  
- Uses LangChain’s new `create_agent()` API  

---

## 📂 Project Structure
├── Backend.py
├── frontend.py
├── ai_agents.py

---

## 🔧 Installation

```bash
pip install fastapi uvicorn streamlit langchain langchain-openai langchain-groq langchain-tavily python-dotenv
```
Make sure your .env file contains:
```ini
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```
---
## ▶ Running the Backend (FastAPI)
```bash
python Backend.py
```

FastAPI will open on:
```cpp
http://127.0.0.1:9999
```
Swagger docs:
```arduino
http://127.0.0.1:9999/docs
```
---
## 💻 Running the Frontend (Streamlit)
```bash
streamlit run frontend.py
```
Then open the local URL shown in the terminal.
---
## 🧠 How the Agent Works

AI agent is created dynamically based on:

* **Provider** (Groq or OpenAI)
* **Model name**
* **System prompt**
* **Web search toggle**
* **User query**
Example call from backend:
```python
response = get_response_from_ai_agent(
    llm_id,
    query,
    allow_search,
    system_prompt,
    provider
)
```
## 🏗 Architecture Diagram
```scss
User → Streamlit UI → FastAPI Backend → AI Agent (LangChain)
                                       ↳ LLM (Groq / OpenAI)
                                       ↳ Tavily Search (optional)
```
---
## 📜 License
MIT License.
---
## ⭐ Contribute
Feel free to open issues or submit PRs!
