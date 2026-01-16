FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expor a porta (Render usa PORT do ambiente, padrão 7860)
EXPOSE 7860

# Definir variável de ambiente PORT (será sobrescrita pelo Render se necessário)
ENV PORT=7860

CMD ["python", "app.py"]
