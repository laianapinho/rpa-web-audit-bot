# Importa o pandas, usado para criar a planilha de entrada.
import pandas as pd

# Importa o caminho da planilha de entrada definido no config.py.
from app.config import INPUT_FILE

# Importa a função que configura os logs do projeto.
from app.logger_config import configurar_logger

# Importa a função que carrega e valida os dados da planilha.
from app.excel_reader import carregar_dados_entrada

# Importa a função que consulta vários registros na página web.
from app.web_automation import consultar_varios_registros

# Importa a função que compara os dados esperados com os dados encontrados.
from app.audit_service import comparar_resultados


# Cria o logger deste arquivo.
logger = configurar_logger()


def criar_planilha_entrada():
    # Cria um dicionário com dados fictícios para a planilha.
    dados = {
        "codigo": ["001", "002", "003", "004","999"],
        "nome": ["Ana Silva", "João Souza", "Maria Lima", "Carlos Santos", "Fernanda Rocha"],
        "status_esperado": ["Ativo", "Inativo", "Ativo", "Pendente", "Ativo"]
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

    # Pega todos os códigos da coluna "codigo" da planilha.
    codigos = df["codigo"].astype(str).tolist()

    # Mostra os códigos que serão consultados.
    print("\nCódigos que serão consultados:")
    print(codigos)

    # Consulta todos os códigos na página web.
    resultados_web = consultar_varios_registros(codigos)

    # Compara os dados da planilha com os resultados encontrados no site.
    resultados_auditoria = comparar_resultados(df, resultados_web)

    # Mostra o resultado final da auditoria no terminal.
    print("\nResultado final da auditoria:")

    # Percorre cada item da auditoria.
    for item in resultados_auditoria:
        print("-----------------------------")
        print(f"Código: {item['codigo']}")
        print(f"Nome esperado: {item['nome_esperado']}")
        print(f"Nome encontrado: {item['nome_encontrado']}")
        print(f"Status esperado: {item['status_esperado']}")
        print(f"Status encontrado: {item['status_encontrado']}")
        print(f"Resultado: {item['resultado_auditoria']}")
        print(f"Mensagem: {item['mensagem']}")

    # Registra no log que a execução terminou.
    logger.info("Execução finalizada.")


# Verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":
    # Chama a função principal do projeto.
    main()