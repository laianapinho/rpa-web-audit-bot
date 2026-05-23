# Importa o pandas, usado para criar a planilha de entrada.
import pandas as pd

# Importa o caminho da planilha de entrada definido no config.py.
from app.config import INPUT_FILE

# Importa a função que configura os logs do projeto.
from app.logger_config import configurar_logger

# Importa a função que carrega e valida os dados da planilha.
from app.excel_reader import carregar_dados_entrada

# Importa a função que faz a consulta automática na página web.
from app.web_automation import consultar_registro


# Cria o logger deste arquivo.
logger = configurar_logger()


def criar_planilha_entrada():
    # Cria um dicionário com dados fictícios para a planilha.
    dados = {
        "codigo": ["001", "002", "003", "004"],
        "nome": ["Ana Silva", "João Souza", "Maria Lima", "Carlos Santos"],
        "status_esperado": ["Ativo", "Inativo", "Ativo", "Pendente"]
    }

    # Converte o dicionário em um DataFrame do Pandas.
    df = pd.DataFrame(dados)

    # Salva o DataFrame em um arquivo Excel.
    df.to_excel(INPUT_FILE, index=False)

    # Registra no log que a planilha foi criada.
    logger.info("Planilha de entrada criada com sucesso.")

    # Mostra no terminal o local onde a planilha foi criada.
    print(f"Planilha criada em: {INPUT_FILE}")


def main():
    # Registra no log o início da aplicação.
    logger.info("Iniciando o projeto RPA Web Audit Bot.")

    # Cria a planilha de entrada com dados fictícios.
    criar_planilha_entrada()

    # Carrega e valida os dados da planilha.
    df = carregar_dados_entrada()

    # Mostra no terminal os dados carregados.
    print("\nDados carregados da planilha:")
    print(df)

    # Define um código fixo para testar a automação.
    codigo_teste = "003"

    # Mostra no terminal qual código será consultado.
    print(f"\nConsultando código de teste: {codigo_teste}")

    # Chama a função do Selenium para consultar o código na página web.
    resultado = consultar_registro(codigo_teste)

    # Mostra o resultado retornado pela automação.
    print("\nResultado encontrado na página:")
    print(f"Código: {resultado['codigo']}")
    print(f"Nome: {resultado['nome']}")
    print(f"Status encontrado: {resultado['status_encontrado']}")
    print(f"Mensagem: {resultado['mensagem']}")

    # Registra no log que a execução terminou.
    logger.info("Execução finalizada.")


# Verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":
    # Chama a função principal do projeto.
    main()