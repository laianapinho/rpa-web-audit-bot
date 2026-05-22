import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "rpa-web-audit-bot")

INPUT_FILE = os.getenv("INPUT_FILE", "data/entrada.xlsx")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "output/resultado_auditoria.xlsx")
LOG_FILE = os.getenv("LOG_FILE", "logs/execucao.log")
EVIDENCE_DIR = os.getenv("EVIDENCE_DIR", "evidences")