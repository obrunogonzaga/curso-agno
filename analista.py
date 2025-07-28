from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    tools=[TavilyTools(), YFinanceTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto além da tabela. Ex: | Ação | Preço | Variation | |------|-------|-----------| | Apple | 150.00 | +1.00% |",
    stream=True
)

agent.print_response("Qual a contação do dolar atualmente e variação do dia anterior?")