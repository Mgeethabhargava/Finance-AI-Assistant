#CHATGPT
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # or use Groq if configured
    tools=[ReasoningTools()],
    instructions="You are a helpful banking assistant. Explain financial and banking concepts clearly with practical examples."
)
