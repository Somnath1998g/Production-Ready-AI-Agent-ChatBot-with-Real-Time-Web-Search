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

# Create the agent (new API)
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Pick LLM
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    else:
        llm = ChatOpenAI(model=llm_id)

    # Tools (only if search enabled)
    tools = [TavilySearch(max_results=2)] if allow_search else []

    # Create agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
    )

    # Convert list[str] -> list[HumanMessage]
    # Backend sends: ["hello"] so we wrap each into HumanMessage
    messages = [HumanMessage(content=m) for m in query]
    state = {"messages": messages}

    response = agent.invoke(state)

    # Return last assistant message text
    return response["messages"][-1].content
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
