# Importa Path para criar pastas e trabalhar com caminhos.
from pathlib import Path

# Importa pandas para criar a planilha Excel de exemplo.
import pandas as pd

# Importa o caminho da planilha de entrada.
from app.config import INPUT_FILE

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


def criar_planilha_entrada_exemplo():
    # Garante que a pasta data existe.
    Path(INPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

    # Cria os dados fictícios usados para testar a automação.
    dados = {
        "codigo": ["001", "002", "003", "004", "999"],
        "nome": [
            "Ana Silva",
            "João Souza",
            "Maria Lima",
            "Carlos Santos",
            "Registro Fantasma"
        ],
        "status_esperado": [
            "Ativo",
            "Inativo",
            "Inativo",
            "Pendente",
            "Ativo"
        ]
    }

    # Converte os dados em uma tabela do Pandas.
    df = pd.DataFrame(dados)

    # Salva a tabela como arquivo Excel.
    df.to_excel(INPUT_FILE, index=False)

    # Registra no log que a planilha foi criada.
    logger.info("Planilha de entrada de exemplo criada com sucesso.")

    # Mostra no terminal onde a planilha foi criada.
    print(f"Planilha de entrada criada em: {INPUT_FILE}")

    # Retorna o caminho da planilha criada.
    return INPUT_FILE