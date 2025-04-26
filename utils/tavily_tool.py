## deep-research-ai/utils/tavily_tool.py

import requests
import os

def tavily_search_tool(query):
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    url = "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"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    params = {"query": query, "search_depth": "advanced"}
    response = requests.get(url, headers=headers, params=params)
    results = response.json()
    return "\n".join([r["content"] for r in results.get("results", [])])