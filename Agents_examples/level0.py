from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",api_key = groq_api_key),
    # model= OpenAIChat(id='gpt-3.5-turbo',api_key= openai_api_key, base_url = "https://api.aimlapi.com"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

