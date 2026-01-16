from agents import Agent, WebSearchTool, ModelSettings

INSTRUCTIONS = (
    "Você é um assistente de pesquisa. Dado um termo de busca, você pesquisa na web sobre esse termo e "
    "produz um resumo conciso dos resultados. O resumo deve ter de 2 a 3 parágrafos e menos de 300 "
    "palavras. Capture os pontos principais. Escreva de forma sucinta, sem necessidade de frases completas "
    "ou boa gramática. Isso será usado por alguém que vai sintetizar um relatório, portanto é vital que você "
    "capte a essência e ignore qualquer informação supérflua. Não inclua comentários adicionais além do próprio resumo."
)


search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
)