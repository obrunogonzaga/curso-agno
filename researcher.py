from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    tools=[TavilyTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
)

agent.print_response("Qual a temperatura de agora em Curitiba?")