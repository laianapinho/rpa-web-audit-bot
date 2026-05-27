# Importa os para abrir o relatório automaticamente no Windows.
import os

# Importa Path para converter caminhos relativos em caminhos absolutos.
from pathlib import Path

# Importa o logger do projeto.
from app.logger_config import configurar_logger

# Importa a função que cria a planilha fake de entrada.
from app.sample_data_service import criar_planilha_entrada_exemplo

# Importa a função que lê e valida a planilha.
from app.excel_reader import carregar_dados_entrada

# Importa a automação com BotCity.
from app.botcity_automation import consultar_varios_registros_botcity

# Importa a comparação da auditoria.
from app.audit_service import comparar_resultados

# Importa a geração do relatório Excel.
from app.report_service import gerar_relatorio_excel


# Cria o logger deste arquivo.
logger = configurar_logger()


def imprimir_dados_entrada(df):
    # Mostra no terminal os dados carregados da planilha.
    print("\nDados carregados da planilha:")

    # Imprime o DataFrame completo.
    print(df)


def obter_codigos_para_consulta(df):
    # Converte a coluna codigo em uma lista de textos.
    codigos = df["codigo"].astype(str).tolist()

    # Mostra os códigos no terminal.
    print("\nCódigos que serão consultados:")

    # Imprime a lista de códigos.
    print(codigos)

    # Retorna a lista.
    return codigos


def imprimir_resultado_auditoria(resultados_auditoria):
    # Mostra o título do resultado final.
    print("\nResultado final da auditoria:")

    # Percorre cada item da auditoria.
    for item in resultados_auditoria:
        # Imprime separador visual.
        print("-----------------------------")

        # Imprime o código auditado.
        print(f"Código: {item['codigo']}")

        # Imprime o nome esperado.
        print(f"Nome esperado: {item['nome_esperado']}")

        # Imprime o nome encontrado.
        print(f"Nome encontrado: {item['nome_encontrado']}")

        # Imprime o status esperado.
        print(f"Status esperado: {item['status_esperado']}")

        # Imprime o status encontrado.
        print(f"Status encontrado: {item['status_encontrado']}")

        # Imprime o resultado da auditoria.
        print(f"Resultado: {item['resultado_auditoria']}")

        # Imprime a mensagem retornada.
        print(f"Mensagem: {item['mensagem']}")

        # Imprime o caminho da evidência.
        print(f"Evidência: {item['evidencia']}")

        # Imprime erro técnico, quando existir.
        print(f"Erro técnico: {item['erro']}")


def abrir_relatorio_automaticamente(caminho_relatorio):
    # Converte o caminho do relatório para caminho absoluto.
    caminho_relatorio_absoluto = Path(caminho_relatorio).resolve()

    # Mostra o caminho absoluto no terminal.
    print(f"\nRelatório Excel gerado em: {caminho_relatorio_absoluto}")

    # Abre o relatório automaticamente no Windows.
    os.startfile(caminho_relatorio_absoluto)


def executar_auditoria():
    # Cria a planilha de entrada de exemplo.
    criar_planilha_entrada_exemplo()

    # Carrega e valida os dados da planilha.
    df = carregar_dados_entrada()

    # Mostra os dados carregados.
    imprimir_dados_entrada(df)

    # Obtém a lista de códigos que serão consultados.
    codigos = obter_codigos_para_consulta(df)

    # Consulta os códigos com BotCity.
    resultados_web = consultar_varios_registros_botcity(codigos)

    # Compara os dados da planilha com os dados encontrados na página.
    resultados_auditoria = comparar_resultados(df, resultados_web)

    # Imprime o resultado final da auditoria no terminal.
    imprimir_resultado_auditoria(resultados_auditoria)

    # Gera o relatório Excel final.
    caminho_relatorio = gerar_relatorio_excel(resultados_auditoria)

    # Abre o relatório automaticamente.
    abrir_relatorio_automaticamente(caminho_relatorio)

    # Conta o total de registros auditados.
    total_registros = len(resultados_auditoria)

    # Conta quantos registros ficaram como Conforme.
    total_conforme = sum(
        1 for item in resultados_auditoria
        if item["resultado_auditoria"] == "Conforme"
    )

    # Conta quantos registros ficaram como Não conforme.
    total_nao_conforme = sum(
        1 for item in resultados_auditoria
        if item["resultado_auditoria"] == "Não conforme"
    )

    # Conta quantos registros ficaram como Não encontrado.
    total_nao_encontrado = sum(
        1 for item in resultados_auditoria
        if item["resultado_auditoria"] == "Não encontrado"
    )

    # Conta quantos registros ficaram como Erro.
    total_erro = sum(
        1 for item in resultados_auditoria
        if item["resultado_auditoria"] == "Erro"
    )

    # Mostra um resumo final no terminal.
    print("\nResumo da execução:")
    print(f"Total de registros: {total_registros}")
    print(f"Conformes: {total_conforme}")
    print(f"Não conformes: {total_nao_conforme}")
    print(f"Não encontrados: {total_nao_encontrado}")
    print(f"Erros técnicos: {total_erro}")


def main():
    # Registra o início da aplicação.
    logger.info("Iniciando RPA Web Audit Bot com BotCity.")

    # Executa o fluxo principal da auditoria.
    executar_auditoria()

    # Registra o fim da aplicação.
    logger.info("Execução finalizada.")


# Executa a aplicação quando o arquivo é chamado diretamente.
if __name__ == "__main__":
    main()