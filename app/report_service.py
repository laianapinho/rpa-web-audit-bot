# Importa Path para trabalhar com caminhos de arquivos e criar pastas.
from pathlib import Path

# Importa pandas para transformar os resultados em uma planilha Excel.
import pandas as pd

# Importa o caminho do arquivo de saída definido no config.py.
from app.config import OUTPUT_FILE

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


def gerar_relatorio_excel(resultados_auditoria):
    # Registra no log que a geração do relatório começou.
    logger.info("Iniciando geração do relatório Excel.")

    # Garante que a pasta output existe.
    # Exemplo: output/
    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

    # Converte a lista de dicionários em um DataFrame do Pandas.
    # Cada dicionário vira uma linha da planilha.
    df = pd.DataFrame(resultados_auditoria)

    # Define a ordem das colunas no relatório.
    colunas = [
        "codigo",
        "nome_esperado",
        "nome_encontrado",
        "status_esperado",
        "status_encontrado",
        "resultado_auditoria",
        "mensagem",
        "evidencia"
    ]

    # Reorganiza o DataFrame seguindo a ordem definida.
    df = df[colunas]

    # Salva o DataFrame em um arquivo Excel.
    # index=False evita criar uma coluna extra com o índice do Pandas.
    df.to_excel(OUTPUT_FILE, index=False)

    # Registra no log o caminho do relatório.
    logger.info(f"Relatório Excel gerado com sucesso: {OUTPUT_FILE}")

    # Retorna o caminho do arquivo gerado.
    return OUTPUT_FILE