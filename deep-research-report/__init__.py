# Este arquivo é necessário para que o Python reconheça esta pasta como um módulo
# Pode ficar vazio ou conter informações sobre o módulo

"""
Módulo principal do Deep Research
Contém todos os agentes e funcionalidades de pesquisa avançada
"""

__version__ = "1.0.0"
__author__ = "Lucca Maximus Romagnolli"
__description__ = "Sistema de pesquisa avançada com IA"

# Importar componentes principais para facilitar o acesso
try:
    from research_manager import ResearchManager
    from app import app
    __all__ = ['ResearchManager', 'app']
except ImportError:
    # Se houver problemas com imports, deixar vazio
    __all__ = []