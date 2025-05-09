## deep-research-ai/agents/researcher_agent.py

from dotenv import load_dotenv
load_dotenv()
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
import os
from utils.tavily_tool import tavily_search_tool

llm = ChatOpenAI(temperature=0.3, 
                 openai_api_key=os.getenv("OPENAI_API_KEY"))


tools = [
    Tool(
        name="Tavily Search",
        func=tavily_search_tool,
        description="Useful for fetching up-to-date online information about any topic."
    )
]

research_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_research_agent(query):
    return research_agent.run(query)