## deep-research-ai/graph/langgraph_flow.py

from langgraph.graph import END, StateGraph
from langchain_core.runnables import RunnableLambda
from agents.researcher_agent import run_research_agent
from agents.answer_agent import run_answer_agent

class ResearchState(dict):
    pass

def run_graph(query):
    builder = StateGraph(ResearchState)

    def collect(state):
        result = run_research_agent(state["query"])
        return {"query": state["query"], "research": result}

    def draft(state):
        final = run_answer_agent(state["research"], state["query"])
        return {"final_answer": final}

    builder.add_node("researcher", RunnableLambda(collect))
    builder.add_node("drafter", RunnableLambda(draft))

    builder.set_entry_point("researcher")
    builder.add_edge("researcher", "drafter")
    builder.add_edge("drafter", END)

    graph = builder.compile()
    result = graph.invoke({"query": query})
    return result["final_answer"]
