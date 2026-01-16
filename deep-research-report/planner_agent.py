from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 20

INSTRUCTIONS = f"Você é um assistente de pesquisa útil. Dada uma consulta, elabore um conjunto de pesquisas na web \
para realizar a fim de responder da melhor forma à consulta. Produza {HOW_MANY_SEARCHES} termos para pesquisar."



class WebSearchItem(BaseModel):
    reason: str = Field(description="Sua justificativa para explicar por que essa pesquisa é importante para a consulta.")
    query: str = Field(description="O termo de pesquisa a ser usado na busca na web.")



class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="Uma lista de pesquisas na web a serem realizadas para responder da melhor forma à consulta.")

    
planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)