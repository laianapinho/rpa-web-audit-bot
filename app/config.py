# Importa os, usado para ler variáveis de ambiente.
import os

# Importa Path, usado para montar caminhos compatíveis com Windows e Linux.
from pathlib import Path

# Importa load_dotenv, usado para carregar variáveis do arquivo .env.
from dotenv import load_dotenv


# Carrega variáveis de ambiente do arquivo .env, se existir.
load_dotenv()


# Pega o diretório raiz do projeto.
# __file__ aponta para app/config.py.
# parents[1] sobe para a pasta rpa-web-audit-bot.
BASE_DIR = Path(__file__).resolve().parents[1]


# Nome da aplicação.
APP_NAME = os.getenv("APP_NAME", "rpa-web-audit-bot")


# Caminho da planilha de entrada.
INPUT_FILE = os.getenv("INPUT_FILE", str(BASE_DIR / "data" / "entrada.xlsx"))


# Caminho do relatório final.
OUTPUT_FILE = os.getenv("OUTPUT_FILE", str(BASE_DIR / "output" / "resultado_auditoria.xlsx"))


# Caminho do arquivo de log.
LOG_FILE = os.getenv("LOG_FILE", str(BASE_DIR / "logs" / "execucao.log"))


# Caminho da pasta de evidências.
EVIDENCE_DIR = os.getenv("EVIDENCE_DIR", str(BASE_DIR / "evidences"))


# Caminho do HTML local.
WEB_PAGE_PATH = BASE_DIR / "web" / "index.html"


# URL local do HTML.
# No Windows, isso vira algo como:
# file:///C:/Users/.../rpa-web-audit-bot/web/index.html
WEB_PAGE_URL = WEB_PAGE_PATH.as_uri()