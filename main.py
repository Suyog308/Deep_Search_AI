## deep-research-ai/main.py

from dotenv import load_dotenv
load_dotenv()

from graph.langgraph_flow import run_graph

if __name__ == "__main__":
    query = input("Enter your research query: ")
    response = run_graph(query)
    print("\nFinal Response:\n", response)


