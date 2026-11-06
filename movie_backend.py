
from pathlib import Path

from langchain.mcp import MCPAdapter
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver


# Remember conversations while the backend process is running
memory = InMemorySaver()


async def ask_movie(question: str, thread_id: str) -> str:

    # Locate our existing MCP server
    server_path = Path(__file__).resolve().with_name(
        "movie_mcp_server.py"
    )

    # Connect to the MCP server
    async with MCPAdapter(server_path) as adapter:

        # Discover our two movie tools
        tools = await adapter.list_tools()

        # Initialize the local Ollama model
        model = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
            base_url="http://localhost:11434"
        )

        # Create our AI agent
        agent = create_agent(
            model=model,
            tools=tools,
            system_prompt=(
                "You are a helpful Movie AI Assistant. "
                "Use search_movies to find movie recommendations. "
                "Use get_movie_details to answer questions "
                "about specific movies. "
                "Only recommend movies from the MCP catalog."
            ),
            checkpointer=memory
        )

        # Ask the agent a question
        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": thread_id
                }
            }
        )

        # Return the AI response
        return result["messages"][-1].content
