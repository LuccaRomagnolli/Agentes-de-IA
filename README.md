# Agentes de IA - Deep Research Report

Um sistema avançado de agentes inteligentes para geração automática de relatórios de pesquisa profundos usando IA, baseado em planejamento, busca e redação coordenada.

## 🎯 Visão Geral

Este projeto implementa um sistema multi-agente que automatiza a criação de relatórios de pesquisa complexos. Cada agente especializado realiza uma função específica:

- **Planner Agent**: Estrutura o plano de pesquisa e define objetivos
- **Search Agent**: Realiza buscas web e coleta informações relevantes
- **Writer Agent**: Redige conteúdo profissional e bem estruturado
- **Email Agent**: Gerencia comunicações e notificações
- **Research Manager**: Coordena a orquestração de todos os agentes

## ✨ Características

- 🤖 Sistema de agentes multi-especializados
- 🔍 Busca e coleta automática de informações
- 📝 Geração de relatórios profissionais
- 🌐 Interface web intuitiva com Gradio
- 📧 Integração com sistema de emails
- 🚀 Deployment com Docker
- 🔄 Processamento assíncrono
- 📚 Suporte para múltiplos modelos de IA (Claude, GPT)

## 📋 Pré-requisitos

- Python 3.8+
- API Keys:
  - Claude (Anthropic)
  - OpenAI
  - SendGrid (para emails)

## 🚀 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/LuccaRomagnolli/Agentes-de-IA.git
cd Agentes-de-IA
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r Projects/deep-research-report/requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cd Projects/deep-research-report
cp .env.example .env
# Edite o arquivo .env com suas API keys
```

Variáveis necessárias no `.env`:
```
ANTHROPIC_API_KEY=your_claude_api_key
OPENAI_API_KEY=your_openai_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
```

## 💻 Uso

### Iniciar a interface web
```bash
cd Projects/deep-research-report
python app.py
```

A aplicação estará disponível em `http://localhost:7860`

### Uso programático
```python
from research_manager import ResearchManager

manager = ResearchManager()
result = manager.generate_report(topic="Seu tópico aqui")
print(result)
```

## 🐳 Docker

```bash
cd Projects/deep-research-report
docker build -t agentes-ia:latest .
docker run -p 7860:7860 --env-file .env agentes-ia:latest
```

## 📁 Estrutura do Projeto

```
Projects/deep-research-report/
├── app.py                 # Aplicação principal com interface Gradio
├── research_manager.py    # Orquestrador central dos agentes
├── planner_agent.py       # Agente de planejamento
├── search_agent.py        # Agente de busca
├── writer_agent.py        # Agente de redação
├── email_agent.py         # Agente de comunicação
├── requirements.txt       # Dependências do projeto
├── Dockerfile            # Configuração Docker
└── __init__.py           # Inicialização do pacote
```

## 🔧 Componentes Principais

### Planner Agent
Responsável por estruturar a pesquisa, definindo:
- Objetivos principais
- Subtópicos a investigar
- Palavras-chave
- Estrutura do relatório

### Search Agent
Realiza coleta de informações através de:
- Buscas web
- Wikipedia
- Scraping de sites relevantes

### Writer Agent
Produz conteúdo:
- Redação profissional
- Formatação estruturada
- Citações e referências
- Revisão de qualidade

### Email Agent
Gerencia comunicações:
- Notificação de conclusão
- Envio de relatórios
- Atualizações de status

## 🤝 Modelos de IA Suportados

- **Claude** (Anthropic) - Recomendado
- **GPT-4/GPT-3.5** (OpenAI)
- LangChain para integração flexível

## 📊 Exemplos

### Gerar um relatório de pesquisa
```python
from research_manager import ResearchManager

manager = ResearchManager()
report = manager.generate_report(
    topic="Inteligência Artificial em 2026",
    depth="detailed",
    max_pages=20
)
```

### Usar agente específico
```python
from planner_agent import PlannerAgent

planner = PlannerAgent()
plan = planner.create_research_plan("Machine Learning")
print(plan)
```

## 🌟 Roadmap

- [ ] Suporte a mais idiomas
- [ ] Integração com bancos de dados acadêmicos
- [ ] Interface desktop
- [ ] Sistema de cache inteligente
- [ ] Análise de sentimento dos resultados
- [ ] Exportação em múltiplos formatos

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Lucca Maximus Romagnolli**
- GitHub: [@LuccaRomagnolli](https://github.com/LuccaRomagnolli)

## 🙏 Agradecimentos

- Anthropic pelo Claude API
- OpenAI pelo GPT
- Comunidade Python por bibliotecas incríveis

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma [Issue](https://github.com/LuccaRomagnolli/Agentes-de-IA/issues)
- Envie um Pull Request com melhorias

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**
