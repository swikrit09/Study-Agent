from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

from agno.models.groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",api_key = groq_api_key),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
