# Step 1: Setup Pydantic Models
from pydantic import BaseModel
from typing import List
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: list[str]
    allow_search: bool
# Step 2: Setup AI agent from Frontend Request
from fastapi import FastAPI
from ai_agents import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it! 
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

# Step 3: Run app & Explore swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)

# {
#   "model_name": "llama3-70b-8192",
#   "model_provider": "Groq",
#   "system_prompt": "Act as an AI helpful assistant",
#   "messages": [
#     "what is the capital of India?"
#   ],
#   "allow_search": false
# }
# {
#   "model_name": "gpt-4o-mini",
#   "model_provider": "OpenAI",
#   "system_prompt": "Act as an AI helpful assistant",
#   "messages": [
#     "what is the capital of India?"
#   ],
#   "allow_search": false
# }