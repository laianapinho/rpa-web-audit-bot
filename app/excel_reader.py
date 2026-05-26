# Importa Path para verificar se arquivos existem.
from pathlib import Path

# Importa pandas para ler planilhas Excel.
import pandas as pd

# Importa o caminho da planilha de entrada.
from app.config import INPUT_FILE

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


# Define as colunas obrigatórias da planilha.
COLUNAS_OBRIGATORIAS = ["codigo", "nome", "status_esperado"]


def verificar_arquivo_existe(caminho_arquivo: str) -> None:
    # Converte o caminho em objeto Path.
    caminho = Path(caminho_arquivo)

    # Verifica se o arquivo existe.
    if not caminho.exists():
        logger.error(f"Arquivo de entrada não encontrado: {caminho_arquivo}")
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {caminho_arquivo}")

    # Registra que o arquivo foi encontrado.
    logger.info(f"Arquivo de entrada encontrado: {caminho_arquivo}")


def ler_planilha() -> pd.DataFrame:
    # Verifica se o arquivo existe antes de ler.
    verificar_arquivo_existe(INPUT_FILE)

    try:
        # Lê a planilha como texto.
        df = pd.read_excel(INPUT_FILE, dtype=str)

        # Registra sucesso.
        logger.info("Planilha lida com sucesso.")

        # Retorna os dados.
        return df

    except Exception as erro:
        # Registra erro de leitura.
        logger.error(f"Erro ao ler a planilha: {erro}")

        # Relança o erro.
        raise


def validar_colunas(df: pd.DataFrame) -> None:
    # Pega as colunas da planilha.
    colunas_planilha = list(df.columns)

    # Verifica quais colunas obrigatórias estão ausentes.
    colunas_faltantes = [
        coluna for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in colunas_planilha
    ]

    # Se houver colunas faltando, lança erro.
    if colunas_faltantes:
        logger.error(f"Colunas obrigatórias ausentes: {colunas_faltantes}")
        raise ValueError(f"Colunas obrigatórias ausentes: {colunas_faltantes}")

    # Registra sucesso.
    logger.info("Todas as colunas obrigatórias foram encontradas.")


def validar_campos_vazios(df: pd.DataFrame) -> None:
    # Conta campos vazios nas colunas obrigatórias.
    campos_vazios = df[COLUNAS_OBRIGATORIAS].isnull().sum()

    # Filtra somente colunas com problemas.
    problemas = campos_vazios[campos_vazios > 0]

    # Se houver problemas, lança erro.
    if not problemas.empty:
        logger.error(f"Campos vazios encontrados: {problemas.to_dict()}")
        raise ValueError(f"Campos vazios encontrados: {problemas.to_dict()}")

    # Registra sucesso.
    logger.info("Nenhum campo vazio foi encontrado nas colunas obrigatórias.")


def carregar_dados_entrada() -> pd.DataFrame:
    # Registra início do carregamento.
    logger.info("Iniciando carregamento dos dados de entrada.")

    # Lê a planilha.
    df = ler_planilha()

    # Valida as colunas.
    validar_colunas(df)

    # Valida campos vazios.
    validar_campos_vazios(df)

    # Registra total carregado.
    logger.info(f"Total de registros carregados: {len(df)}")

    # Retorna DataFrame validado.
    return df