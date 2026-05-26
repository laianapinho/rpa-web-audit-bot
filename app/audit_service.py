# Importa pandas para verificar valores nulos.
import pandas as pd

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria logger deste arquivo.
logger = configurar_logger()


def normalizar_texto(valor):
    # Se o valor for nulo, retorna string vazia.
    if pd.isna(valor):
        return ""

    # Converte para texto, remove espaços e deixa minúsculo.
    return str(valor).strip().lower()


def definir_resultado_auditoria(status_esperado, status_encontrado, mensagem):
    # Normaliza status esperado.
    esperado_normalizado = normalizar_texto(status_esperado)

    # Normaliza status encontrado.
    encontrado_normalizado = normalizar_texto(status_encontrado)

    # Normaliza mensagem.
    mensagem_normalizada = normalizar_texto(mensagem)

    # Se a mensagem indicar registro não encontrado.
    if "não encontrado" in mensagem_normalizada or "nao encontrado" in mensagem_normalizada:
        return "Não encontrado"

    # Se esperado e encontrado forem iguais.
    if esperado_normalizado == encontrado_normalizado:
        return "Conforme"

    # Caso contrário, há divergência.
    return "Não conforme"


def comparar_resultados(df_entrada, resultados_web):
    # Cria lista final da auditoria.
    resultados_auditoria = []

    # Registra início da comparação.
    logger.info("Iniciando comparação entre planilha e resultados da página.")

    # Percorre cada linha da planilha.
    for _, linha in df_entrada.iterrows():
        # Pega código da linha.
        codigo = str(linha["codigo"]).strip()

        # Pega nome esperado.
        nome_esperado = linha["nome"]

        # Pega status esperado.
        status_esperado = linha["status_esperado"]

        # Procura resultado web com mesmo código.
        resultado_web = next(
            (
                item for item in resultados_web
                if str(item["codigo"]).strip() == codigo
            ),
            None
        )

        # Se não houver resultado web.
        if resultado_web is None:
            nome_encontrado = "-"
            status_encontrado = "-"
            mensagem = "Resultado não retornado pela automação."
            evidencia = "-"

        # Se houver resultado web.
        else:
            nome_encontrado = resultado_web["nome_encontrado"]
            status_encontrado = resultado_web["status_encontrado"]
            mensagem = resultado_web["mensagem"]
            evidencia = resultado_web.get("evidencia", "-")

        # Define resultado da auditoria.
        resultado_auditoria = definir_resultado_auditoria(
            status_esperado=status_esperado,
            status_encontrado=status_encontrado,
            mensagem=mensagem
        )

        # Monta item final.
        item_auditoria = {
            "codigo": codigo,
            "nome_esperado": nome_esperado,
            "nome_encontrado": nome_encontrado,
            "status_esperado": status_esperado,
            "status_encontrado": status_encontrado,
            "resultado_auditoria": resultado_auditoria,
            "mensagem": mensagem,
            "evidencia": evidencia
        }

        # Adiciona na lista final.
        resultados_auditoria.append(item_auditoria)

        # Registra no log.
        logger.info(
            f"Auditoria - Código: {codigo}, Esperado: {status_esperado}, "
            f"Encontrado: {status_encontrado}, Resultado: {resultado_auditoria}"
        )

    # Registra fim.
    logger.info("Comparação finalizada.")

    # Retorna lista final.
    return resultados_auditoria