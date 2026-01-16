from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "Você é um pesquisador sênior encarregado de escrever um relatório coeso para uma consulta de pesquisa. "
    "Você receberá a consulta original e algumas pesquisas iniciais feitas por um assistente de pesquisa.\n"
    "Primeiro, você deve elaborar um esboço para o relatório que descreva a estrutura e o "
    "fluxo do texto. Em seguida, gere o relatório e retorne-o como sua saída final.\n"
    "A saída final deve estar em formato markdown e deve ser extensa e detalhada. Mire em "
    "5 a 10 páginas de conteúdo, com pelo menos 1000 palavras.\n"
    "Basei-se na Norma ABNT NBR 10719:2015 para a formatação do relatório."
)



class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")

    markdown_report: str = Field(description="The final report")

    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)