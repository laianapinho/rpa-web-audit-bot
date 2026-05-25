# Importa o pandas, pois vamos receber os dados da planilha como DataFrame.
import pandas as pd

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


def normalizar_texto(valor):
    # Verifica se o valor está vazio ou nulo.
    if pd.isna(valor):
        # Se estiver vazio, retorna uma string vazia.
        return ""

    # Converte o valor para texto, remove espaços no início/fim e deixa em letras minúsculas.
    return str(valor).strip().lower()


def definir_resultado_auditoria(status_esperado, status_encontrado, mensagem):
    # Normaliza o status esperado para evitar erro por causa de espaços ou letras maiúsculas/minúsculas.
    esperado_normalizado = normalizar_texto(status_esperado)

    # Normaliza o status encontrado.
    encontrado_normalizado = normalizar_texto(status_encontrado)

    # Normaliza a mensagem retornada pela página.
    mensagem_normalizada = normalizar_texto(mensagem)

    # Se a mensagem disser que o registro não foi encontrado, classificamos como "Não encontrado".
    if "não encontrado" in mensagem_normalizada or "nao encontrado" in mensagem_normalizada:
        return "Não encontrado"

    # Se o status esperado for igual ao status encontrado, classificamos como "Conforme".
    if esperado_normalizado == encontrado_normalizado:
        return "Conforme"

    # Caso contrário, classificamos como "Não conforme".
    return "Não conforme"


def comparar_resultados(df_entrada, resultados_web):
    # Cria uma lista vazia para guardar os resultados finais da auditoria.
    resultados_auditoria = []

    # Registra no log que a comparação começou.
    logger.info("Iniciando comparação entre planilha e resultados da página.")

    # Percorre cada linha da planilha de entrada.
    for _, linha in df_entrada.iterrows():
        # Pega o código da linha atual.
        codigo = str(linha["codigo"]).strip()

        # Pega o nome esperado da linha atual.
        nome_esperado = linha["nome"]

        # Pega o status esperado da linha atual.
        status_esperado = linha["status_esperado"]

        # Procura, na lista de resultados do Selenium, o resultado com o mesmo código.
        resultado_web = next(
            (
                item for item in resultados_web
                if str(item["codigo"]).strip() == codigo
            ),
            None
        )

        # Se não encontrar o resultado na lista, cria um resultado padrão.
        if resultado_web is None:
            nome_encontrado = "-"
            status_encontrado = "-"
            mensagem = "Resultado não retornado pela automação."
        else:
            nome_encontrado = resultado_web["nome_encontrado"]
            status_encontrado = resultado_web["status_encontrado"]
            mensagem = resultado_web["mensagem"]

        # Define se o registro está conforme, não conforme ou não encontrado.
        resultado_auditoria = definir_resultado_auditoria(
            status_esperado=status_esperado,
            status_encontrado=status_encontrado,
            mensagem=mensagem
        )

        # Monta um dicionário com o resultado completo da auditoria.
        item_auditoria = {
            "codigo": codigo,
            "nome_esperado": nome_esperado,
            "nome_encontrado": nome_encontrado,
            "status_esperado": status_esperado,
            "status_encontrado": status_encontrado,
            "resultado_auditoria": resultado_auditoria,
            "mensagem": mensagem
        }

        # Adiciona o item na lista final.
        resultados_auditoria.append(item_auditoria)

        # Registra no log o resultado individual.
        logger.info(
            f"Auditoria - Código: {codigo}, Esperado: {status_esperado}, "
            f"Encontrado: {status_encontrado}, Resultado: {resultado_auditoria}"
        )

    # Registra no log que a comparação terminou.
    logger.info("Comparação finalizada.")

    # Retorna a lista completa de auditoria.
    return resultados_auditoria