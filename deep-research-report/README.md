# 🔬 Deep Research - Ferramenta de Pesquisa Avançada com IA

Sistema de pesquisa avançada com IA que realiza análises profundas e gera relatórios detalhados sobre qualquer tópico.

## 🚀 Funcionalidades

- **Pesquisa Inteligente**: Realiza múltiplas buscas na web de forma estratégica
- **Análise Profunda**: Gera relatórios extensos e detalhados (5-10 páginas)
- **Envio por Email**: Envia relatórios completos por email
- **Interface Moderna**: Interface web elegante com tema dark

## 📋 Pré-requisitos

- Python 3.10 ou superior
- Conta OpenAI com API key
- Conta SendGrid (opcional, para envio de emails)

**Nota**: Este projeto utiliza a biblioteca `agents` da OpenAI. Certifique-se de que ela está instalada. Se não estiver incluída automaticamente, você pode precisar instalá-la separadamente ou verificar se está incluída nas dependências do OpenAI.

## 🛠️ Instalação Local

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd deep-research-report
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto:
```
OPENAI_API_KEY=sua_chave_openai
SENDGRID_API_KEY=sua_chave_sendgrid
```

4. Execute a aplicação:
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:7860`

## 🌐 Deploy para URL Pública

### Opção 1: Render.com (Recomendado)

1. Crie uma conta em [Render.com](https://render.com)
2. Conecte seu repositório GitHub
3. Crie um novo Web Service
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment Variables**:
     - `OPENAI_API_KEY`: sua chave OpenAI
     - `SENDGRID_API_KEY`: sua chave SendGrid
     - `PORT`: 7860
5. Deploy!

### Opção 2: Railway.app

1. Crie uma conta em [Railway.app](https://railway.app)
2. Conecte seu repositório GitHub
3. Railway detectará automaticamente o `railway.json` e `Dockerfile`
4. Configure as variáveis de ambiente:
   - `OPENAI_API_KEY`
   - `SENDGRID_API_KEY`
5. Deploy!

### Opção 3: Hugging Face Spaces (Ideal para Gradio)

1. Crie uma conta em [Hugging Face](https://huggingface.co)
2. Crie um novo Space
3. Selecione "Gradio" como SDK
4. Faça upload dos arquivos do projeto
5. Configure as Secrets (variáveis de ambiente):
   - `OPENAI_API_KEY`
   - `SENDGRID_API_KEY`
6. O Space será automaticamente deployado!

### Opção 4: Google Cloud Run

1. Instale o Google Cloud SDK
2. Faça build da imagem Docker:
```bash
gcloud builds submit --tag gcr.io/[PROJECT-ID]/deep-research
```
3. Deploy:
```bash
gcloud run deploy deep-research --image gcr.io/[PROJECT-ID]/deep-research --platform managed
```

## 📝 Variáveis de Ambiente

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `OPENAI_API_KEY` | Chave da API OpenAI | Sim |
| `SENDGRID_API_KEY` | Chave da API SendGrid | Não (apenas para emails) |
| `PORT` | Porta do servidor | Não (padrão: 7860) |

## 🏗️ Estrutura do Projeto

```
deep-research-report/
├── app.py                 # Interface Gradio principal
├── research_manager.py    # Gerenciador de pesquisa
├── planner_agent.py       # Agente de planejamento
├── search_agent.py        # Agente de busca
├── writer_agent.py        # Agente de escrita
├── email_agent.py         # Agente de email
├── requirements.txt       # Dependências Python
├── Dockerfile            # Configuração Docker
└── README.md             # Este arquivo
```

## 📦 Dependências Principais

- `gradio`: Interface web
- `openai`: API OpenAI
- `anthropic`: API Anthropic (Claude)
- `langchain`: Framework para LLMs
- `sendgrid`: Envio de emails
- `beautifulsoup4`: Web scraping

## 🔒 Segurança

⚠️ **IMPORTANTE**: Nunca commite arquivos `.env` ou chaves de API no repositório. Use variáveis de ambiente do serviço de deploy.

## 📄 Licença

MIT License - Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

**Lucca Maximus Romagnolli**

- LinkedIn: [lucca-maximus-6792a1221](https://www.linkedin.com/in/lucca-maximus-6792a1221/)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
