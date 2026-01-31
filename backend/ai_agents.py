# import os
# from dotenv import load_dotenv
# load_dotenv()
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
# #Step2: Setup LLM & Tools
# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
# from langchain_tavily import TavilySearch

# openai_llm=ChatOpenAI(model="gpt-4o-mini")
# groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

# search_tool=TavilySearch(max_results=2)

# #Step3: Setup AI Agent with Search tool functionality
# from langchain_core.messages.ai import AIMessage 
# from langchain.agents import create_agent
# agent = create_agent(
#     model=groq_llm,
#     tools=[search_tool],
#     system_message=AIMessage(
#         content="Act as an AI chatbot who is smart and friendly. Use the Tavily Search tool to answer user queries that require up-to-date information from the web."
#     ),
# )
# query = "What are the latest advancements in AI technology as of June 2024?"
# state = ("messages", query)
# response = agent.invoke(state)
# messages = response.get("messages")
# ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
# print(ai_message[-1])
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch  # NEW package

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage

# LLMs
openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

# Tool (Tavily)
search_tool = TavilySearch(max_results=2)

def run_agent(llm, messages, system_prompt, allow_search):
    tools = [TavilySearch(max_results=2)] if allow_search else []
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
    )
    state = {"messages": messages}
    response = agent.invoke(state)
    return response["messages"][-1].content

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    messages = [HumanMessage(content=m) for m in query]

    # --- Try OpenAI first ---
    if provider == "OpenAI":
        try:
            llm = ChatOpenAI(model=llm_id)
            return run_agent(llm, messages, system_prompt, allow_search)
        except Exception as e:
            # Auto fallback to Groq
            print("⚠️ OpenAI failed, falling back to Groq:", str(e))

            llm = ChatGroq(model="llama-3.3-70b-versatile")
            return run_agent(llm, messages, system_prompt, allow_search)

    # --- Groq only ---
    llm = ChatGroq(model=llm_id)
    return run_agent(llm, messages, system_prompt, allow_search)
# agent = create_agent(
#     model=groq_llm,   # you can also pass "groq:llama-3.3-70b-versatile" as a string in some setups
#     tools=[search_tool],
#     system_prompt=(
#         "Act as an AI chatbot who is smart and friendly. "
#         "Use the Tavily Search tool to answer user queries that require up-to-date information from the web."
#     ),
# )

# query = "tell me about the trends in stock markets in india"

# inputs = {
#     "messages": [
#         {"role": "user", "content": query}
#     ]
# }

# result = agent.invoke(inputs)

# messages = result["messages"]

# # Last message is AI
# ai_message = messages[-1].content

# print(ai_message)
#print(get_response_from_ai_agent("llama-3.3-70b-versatile", "what is the capital of India?", "false", "Act as an AI helpful assistant", "Groq"))
