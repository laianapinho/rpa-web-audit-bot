# Importa Path para criar pastas.
from pathlib import Path

# Importa pandas para criar a planilha de entrada.
import pandas as pd

# Importa caminhos principais.
from app.config import INPUT_FILE

# Importa logger.
from app.logger_config import configurar_logger

# Importa leitura e validação da planilha.
from app.excel_reader import carregar_dados_entrada

# Importa automação com BotCity.
from app.botcity_automation import consultar_varios_registros_botcity

# Importa comparação de auditoria.
from app.audit_service import comparar_resultados


# Cria logger deste arquivo.
logger = configurar_logger()


def criar_planilha_entrada():
    # Garante que a pasta da planilha existe.
    Path(INPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

    # Cria dados fictícios.
    dados = {
        "codigo": ["001", "002", "003", "004", "999"],
        "nome": ["Ana Silva", "João Souza", "Maria Lima", "Carlos Santos", "Registro Fantasma"],
        "status_esperado": ["Ativo", "Inativo", "Inativo", "Pendente", "Ativo"]
    }

    # Converte para DataFrame.
    df = pd.DataFrame(dados)

    # Salva em Excel.
    df.to_excel(INPUT_FILE, index=False)

    # Registra no log.
    logger.info("Planilha de entrada criada com sucesso.")

    # Mostra no terminal.
    print(f"Planilha criada em: {INPUT_FILE}")


def main():
    # Registra início.
    logger.info("Iniciando RPA Web Audit Bot com BotCity.")

    # Cria a planilha.
    criar_planilha_entrada()

    # Carrega e valida a planilha.
    df = carregar_dados_entrada()

    # Mostra dados.
    print("\nDados carregados da planilha:")
    print(df)

    # Pega códigos da planilha.
    codigos = df["codigo"].astype(str).tolist()

    # Mostra códigos.
    print("\nCódigos que serão consultados:")
    print(codigos)

    # Consulta todos os códigos com BotCity.
    resultados_web = consultar_varios_registros_botcity(codigos)

    # Compara planilha com resultados encontrados.
    resultados_auditoria = comparar_resultados(df, resultados_web)

    # Mostra resultado final.
    print("\nResultado final da auditoria:")

    # Percorre cada item.
    for item in resultados_auditoria:
        print("-----------------------------")
        print(f"Código: {item['codigo']}")
        print(f"Nome esperado: {item['nome_esperado']}")
        print(f"Nome encontrado: {item['nome_encontrado']}")
        print(f"Status esperado: {item['status_esperado']}")
        print(f"Status encontrado: {item['status_encontrado']}")
        print(f"Resultado: {item['resultado_auditoria']}")
        print(f"Mensagem: {item['mensagem']}")
        print(f"Evidência: {item['evidencia']}")

    # Registra fim.
    logger.info("Execução finalizada.")


# Executa a função principal.
if __name__ == "__main__":
    main()