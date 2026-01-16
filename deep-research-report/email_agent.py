import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

# Variável global para armazenar o email do destinatário
recipient_email = "lucca2408@gmail.com"  # Email padrão

def update_recipient_email(email: str):
    """Atualiza o email do destinatário"""
    global recipient_email
    recipient_email = email
    print(f"Email do destinatário atualizado para: {email}")

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send an email with the given subject and HTML body """
    global recipient_email
    
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("luccaromagnolli@icloud.com") # put your verified sender here
    to_email = To(recipient_email) # Agora usa o email do usuário
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print(f"Email enviado para: {recipient_email}")
    print("Email response", response.status_code)
    return {"status": "success", "recipient": recipient_email}

INSTRUCTIONS = """Você é capaz de enviar um e-mail em HTML bem formatado com base em um relatório detalhado.
Será fornecido a você um relatório detalhado. Você deve usar sua ferramenta para enviar um e-mail, convertendo
o relatório em um HTML limpo e bem apresentado, com uma linha de assunto apropriada.
O email será enviado para o endereço especificado pelo usuário."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)