from pathlib import Path

import pandas as pd

from app.config import INPUT_FILE
from app.logger_config import configurar_logger


logger = configurar_logger()


COLUNAS_OBRIGATORIAS = ["codigo", "nome", "status_esperado"]


def verificar_arquivo_existe(caminho_arquivo: str) -> None:
    caminho = Path(caminho_arquivo)

    if not caminho.exists():
        logger.error(f"Arquivo de entrada não encontrado: {caminho_arquivo}")
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {caminho_arquivo}")

    logger.info(f"Arquivo de entrada encontrado: {caminho_arquivo}")


def ler_planilha() -> pd.DataFrame:
    verificar_arquivo_existe(INPUT_FILE)

    try:
        df = pd.read_excel(INPUT_FILE, dtype=str)
        logger.info("Planilha lida com sucesso.")
        return df

    except Exception as erro:
        logger.error(f"Erro ao ler a planilha: {erro}")
        raise


def validar_colunas(df: pd.DataFrame) -> None:
    colunas_planilha = list(df.columns)

    colunas_faltantes = [
        coluna for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in colunas_planilha
    ]

    if colunas_faltantes:
        logger.error(f"Colunas obrigatórias ausentes: {colunas_faltantes}")
        raise ValueError(f"Colunas obrigatórias ausentes: {colunas_faltantes}")

    logger.info("Todas as colunas obrigatórias foram encontradas.")


def validar_campos_vazios(df: pd.DataFrame) -> None:
    campos_vazios = df[COLUNAS_OBRIGATORIAS].isnull().sum()

    problemas = campos_vazios[campos_vazios > 0]

    if not problemas.empty:
        logger.error(f"Campos vazios encontrados: {problemas.to_dict()}")
        raise ValueError(f"Campos vazios encontrados: {problemas.to_dict()}")

    logger.info("Nenhum campo vazio foi encontrado nas colunas obrigatórias.")


def carregar_dados_entrada() -> pd.DataFrame:
    logger.info("Iniciando carregamento dos dados de entrada.")

    df = ler_planilha()

    validar_colunas(df)
    validar_campos_vazios(df)

    logger.info(f"Total de registros carregados: {len(df)}")

    return df