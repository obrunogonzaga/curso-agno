from agno.agent import Agent
#from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv
load_dotenv()

def celsius_to_fahrenheit(temperatura_celsius: float) -> float:
    """
    Converte uma temperatura em graus Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): A temperatura em graus Celsius.

    Returns:
        float: A temperatura em Fahrenheit.
    """
    return (temperatura_celsius * 9/5) + 32

# Criar instância do TavilyTools
tavily_tools = TavilyTools()

agent = Agent(
    tools=[tavily_tools, celsius_to_fahrenheit],
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4.1-mini"),
    debug_mode=True
)

agent.print_response("Qual a temperatura de agora em Curitiba em Fahrenheit?")