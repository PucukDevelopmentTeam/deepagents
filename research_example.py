import os
from typing import Literal

from tavily import TavilyClient
from deepagents import create_deep_agent

# Initialize Tavily client (you'll need to set TAVILY_API_KEY environment variable)
tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY", "your-api-key-here"))

# Search tool to use to do research
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

# Prompt prefix to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research, and then write a polished report.

You have access to a few tools.

## `internet_search`

Use this to run an internet search for a given query. You can specify the number of results, the topic, and whether raw content should be included.
"""

# Create the agent
agent = create_deep_agent(
    [internet_search],
    research_instructions,
)

if __name__ == "__main__":
    # Example usage
    result = agent.invoke({"messages": [{"role": "user", "content": "what is langgraph?"}]})
    
    # Print the final response
    print("Research Agent Response:")
    print("=" * 50)
    print(result["messages"][-1].content)