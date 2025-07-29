from agno.agent import Agent
#from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from agno.storage.sqlite import SqliteStorage
from agno.playground import Playground, serve_playground_app

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

db = SqliteStorage(table_name="agent_session", db_file="tmp/agent.db")

agent = Agent(
    tools=[tavily_tools, celsius_to_fahrenheit],
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4.1-mini"),
    storage=db,
    add_history_to_messages=True,
    num_history_runs=3,
    debug_mode=True
)

app = Playground(agents=[agent]).get_app(prefix="")
#agent.print_response("Qual a temperatura de agora em Curitiba em Fahrenheit?")

if __name__ == "__main__":
    serve_playground_app("own_tools:app", reload=True)