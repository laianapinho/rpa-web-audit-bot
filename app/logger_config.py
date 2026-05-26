# Importa logging para registrar logs da aplicação.
import logging

# Importa Path para criar a pasta de logs, caso ela não exista.
from pathlib import Path

# Importa o caminho do arquivo de log.
from app.config import LOG_FILE


def configurar_logger():
    # Cria ou recupera um logger com nome fixo.
    logger = logging.getLogger("rpa_web_audit_bot")

    # Define o nível mínimo de log.
    logger.setLevel(logging.INFO)

    # Evita que mensagens sejam duplicadas no logger raiz.
    logger.propagate = False

    # Se já houver handlers, retorna o logger.
    # Isso evita logs repetidos.
    if logger.handlers:
        return logger

    # Garante que a pasta de logs existe.
    Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

    # Cria handler para salvar logs em arquivo.
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

    # Define nível do arquivo.
    file_handler.setLevel(logging.INFO)

    # Cria handler para mostrar logs no terminal.
    console_handler = logging.StreamHandler()

    # Define nível do terminal.
    console_handler.setLevel(logging.INFO)

    # Define formato das mensagens.
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Aplica formato ao arquivo.
    file_handler.setFormatter(formatter)

    # Aplica formato ao terminal.
    console_handler.setFormatter(formatter)

    # Adiciona handler de arquivo.
    logger.addHandler(file_handler)

    # Adiciona handler de terminal.
    logger.addHandler(console_handler)

    # Retorna logger configurado.
    return logger