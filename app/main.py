import pandas as pd

from app.config import INPUT_FILE
from app.logger_config import configurar_logger
from app.excel_reader import carregar_dados_entrada


logger = configurar_logger()


def criar_planilha_entrada():
    dados = {
        "codigo": ["001", "002", "003", "004"],
        "nome": ["Ana Silva", "João Souza", "Maria Lima", "Carlos Santos"],
        "status_esperado": ["Ativo", "Inativo", "Ativo", "Pendente"]
    }

    df = pd.DataFrame(dados)
    df.to_excel(INPUT_FILE, index=False)

    logger.info("Planilha de entrada criada com sucesso.")
    print(f"Planilha criada em: {INPUT_FILE}")


def main():
    logger.info("Iniciando o projeto RPA Web Audit Bot.")

    criar_planilha_entrada()

    df = carregar_dados_entrada()

    print("\nDados carregados da planilha:")
    print(df)

    logger.info("Execução finalizada.")


if __name__ == "__main__":
    main()