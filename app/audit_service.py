# Importa pandas para ajudar na verificação de valores vazios.
import pandas as pd

# Importa a configuração do logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


def normalizar_texto(valor):
    # Verifica se o valor está vazio ou nulo.
    if pd.isna(valor):
        # Se estiver vazio, retorna texto vazio.
        return ""

    # Converte o valor para texto.
    # Remove espaços no começo e no final.
    # Converte tudo para letras minúsculas.
    return str(valor).strip().lower()


def definir_resultado_auditoria(status_esperado, status_encontrado, mensagem, erro=""):
    # Normaliza o erro técnico recebido da automação.
    erro_normalizado = normalizar_texto(erro)

    # Se existir erro técnico, o resultado da auditoria será "Erro".
    if erro_normalizado:
        return "Erro"

    # Normaliza o status esperado vindo da planilha.
    esperado_normalizado = normalizar_texto(status_esperado)

    # Normaliza o status encontrado na página web.
    encontrado_normalizado = normalizar_texto(status_encontrado)

    # Normaliza a mensagem retornada pela página.
    mensagem_normalizada = normalizar_texto(mensagem)

    # Se a mensagem indicar que o registro não foi encontrado,
    # classificamos como "Não encontrado".
    if "não encontrado" in mensagem_normalizada or "nao encontrado" in mensagem_normalizada:
        return "Não encontrado"

    # Se o status esperado for igual ao status encontrado,
    # classificamos como "Conforme".
    if esperado_normalizado == encontrado_normalizado:
        return "Conforme"

    # Caso contrário, classificamos como "Não conforme".
    return "Não conforme"


def comparar_resultados(df_entrada, resultados_web):
    # Cria uma lista vazia para guardar o resultado final da auditoria.
    resultados_auditoria = []

    # Registra no log que a comparação começou.
    logger.info("Iniciando comparação entre planilha e resultados da página.")

    # Percorre cada linha da planilha de entrada.
    for _, linha in df_entrada.iterrows():
        # Pega o código da linha atual e remove espaços extras.
        codigo = str(linha["codigo"]).strip()

        # Pega o nome esperado vindo da planilha.
        nome_esperado = linha["nome"]

        # Pega o status esperado vindo da planilha.
        status_esperado = linha["status_esperado"]

        # Procura, dentro da lista de resultados web, o item com o mesmo código.
        resultado_web = next(
            (
                item for item in resultados_web
                if str(item["codigo"]).strip() == codigo
            ),
            None
        )

        # Se a automação não retornou nenhum resultado para esse código,
        # criamos um resultado padrão de falha.
        if resultado_web is None:
            nome_encontrado = "-"
            status_encontrado = "-"
            mensagem = "Resultado não retornado pela automação."
            evidencia = "-"
            erro = "Resultado não retornado pela automação."

        # Se a automação retornou resultado, pegamos os dados normalmente.
        else:
            nome_encontrado = resultado_web["nome_encontrado"]
            status_encontrado = resultado_web["status_encontrado"]
            mensagem = resultado_web["mensagem"]
            evidencia = resultado_web.get("evidencia", "-")
            erro = resultado_web.get("erro", "")

        # Define o resultado da auditoria:
        # Conforme, Não conforme, Não encontrado ou Erro.
        resultado_auditoria = definir_resultado_auditoria(
            status_esperado=status_esperado,
            status_encontrado=status_encontrado,
            mensagem=mensagem,
            erro=erro
        )

        # Monta o dicionário final daquele registro.
        item_auditoria = {
            "codigo": codigo,
            "nome_esperado": nome_esperado,
            "nome_encontrado": nome_encontrado,
            "status_esperado": status_esperado,
            "status_encontrado": status_encontrado,
            "resultado_auditoria": resultado_auditoria,
            "mensagem": mensagem,
            "evidencia": evidencia,
            "erro": erro
        }

        # Adiciona o registro na lista final de auditoria.
        resultados_auditoria.append(item_auditoria)

        # Registra no log o resultado daquele código.
        logger.info(
            f"Auditoria - Código: {codigo}, Esperado: {status_esperado}, "
            f"Encontrado: {status_encontrado}, Resultado: {resultado_auditoria}"
        )

    # Registra no log que a comparação terminou.
    logger.info("Comparação finalizada.")

    # Retorna a lista final de resultados da auditoria.
    return resultados_auditoria