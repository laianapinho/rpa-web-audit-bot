import os
from pathlib import Path
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env, se ele existir.
load_dotenv()


# Guarda o nome da aplicação.
# Se APP_NAME não existir no .env, usa "rpa-web-audit-bot" como valor padrão.
APP_NAME = os.getenv("APP_NAME", "rpa-web-audit-bot")


# Caminho da planilha de entrada.
# Essa planilha fica dentro da pasta data.
INPUT_FILE = os.getenv("INPUT_FILE", "data/entrada.xlsx")


# Caminho do relatório final que será gerado nos próximos dias.
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "output/resultado_auditoria.xlsx")


# Caminho do arquivo de log.
LOG_FILE = os.getenv("LOG_FILE", "logs/execucao.log")


# Caminho da pasta onde serão salvas as evidências da automação.
EVIDENCE_DIR = os.getenv("EVIDENCE_DIR", "evidences")


# Pega o diretório raiz do projeto.
# __file__ representa este arquivo atual: app/config.py.
# parents[1] sobe duas partes:
# app/config.py -> app -> rpa-web-audit-bot
BASE_DIR = Path(__file__).resolve().parents[1]


# Monta o caminho completo da página HTML local.
# Exemplo final:
# /home/laiana/.../rpa-web-audit-bot/web/index.html
WEB_PAGE_PATH = BASE_DIR / "web" / "index.html"


# Transforma o caminho da página HTML em uma URL local.
# O Selenium precisa abrir como URL no formato file:///...
WEB_PAGE_URL = WEB_PAGE_PATH.as_uri()