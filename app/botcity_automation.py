# Importa Path para criar caminhos de evidência.
from pathlib import Path

# Importa WebBot, Browser e By da BotCity.
from botcity.web import WebBot, Browser, By

# Importa ChromeDriverManager para localizar/baixar o ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager

# Importa a URL local da página e a pasta de evidências.
from app.config import WEB_PAGE_URL, EVIDENCE_DIR

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


def iniciar_botcity_webbot():
    # Registra início do BotCity.
    logger.info("Iniciando WebBot do BotCity.")

    # Cria o objeto principal do BotCity Web.
    bot = WebBot()

    # Define o navegador como Chrome.
    bot.browser = Browser.CHROME

    # Define que o navegador será visível.
    bot.headless = False

    # Define o caminho do ChromeDriver.
    # O webdriver-manager baixa/localiza automaticamente.
    bot.driver_path = ChromeDriverManager().install()

    # Retorna o bot configurado.
    return bot


def abrir_pagina(bot: WebBot):
    # Registra a URL aberta.
    logger.info(f"Abrindo página local com BotCity: {WEB_PAGE_URL}")

    # Abre a página local.
    bot.browse(WEB_PAGE_URL)

    # Aguarda 1 segundo.
    bot.wait(1000)


def salvar_evidencia(bot: WebBot, codigo: str):
    # Garante que a pasta de evidências existe.
    Path(EVIDENCE_DIR).mkdir(parents=True, exist_ok=True)

    # Monta o nome da evidência.
    caminho_evidencia = Path(EVIDENCE_DIR) / f"evidencia_{codigo}.png"

    # Acessa o driver interno do BotCity.
    driver = bot.driver

    # Salva o print da tela.
    driver.save_screenshot(str(caminho_evidencia))

    # Registra no log.
    logger.info(f"Evidência salva: {caminho_evidencia}")

    # Retorna o caminho da evidência como texto.
    return str(caminho_evidencia)


def consultar_registro_com_bot(bot: WebBot, codigo: str):
    # Registra o código consultado.
    logger.info(f"Iniciando consulta com BotCity para o código: {codigo}")

    # Acessa o driver interno do BotCity.
    driver = bot.driver

    # Localiza o campo de código pelo ID.
    campo_codigo = driver.find_element(By.ID, "codigo")

    # Limpa o campo.
    campo_codigo.clear()

    # Digita o código.
    campo_codigo.send_keys(codigo)

    # Localiza o botão de consulta.
    botao_consultar = driver.find_element(By.CSS_SELECTOR, "button")

    # Clica no botão.
    botao_consultar.click()

    # Aguarda resultado aparecer.
    bot.wait(700)

    # Lê o nome encontrado.
    nome = driver.find_element(By.ID, "nome").text

    # Lê o status encontrado.
    status = driver.find_element(By.ID, "status").text

    # Lê a mensagem exibida.
    mensagem = driver.find_element(By.ID, "mensagem").text

    # Salva evidência da tela após a consulta.
    evidencia = salvar_evidencia(bot, codigo)

    # Monta o resultado.
    resultado = {
        "codigo": codigo,
        "nome_encontrado": nome,
        "status_encontrado": status,
        "mensagem": mensagem,
        "evidencia": evidencia
    }

    # Registra resultado.
    logger.info(f"Resultado BotCity: {resultado}")

    # Retorna resultado.
    return resultado


def consultar_varios_registros_botcity(codigos):
    # Cria lista para guardar resultados.
    resultados = []

    # Inicia o BotCity.
    bot = iniciar_botcity_webbot()

    try:
        # Abre a página local.
        abrir_pagina(bot)

        # Percorre cada código da planilha.
        for codigo in codigos:
            # Consulta o código atual.
            resultado = consultar_registro_com_bot(bot, codigo)

            # Adiciona o resultado na lista.
            resultados.append(resultado)

        # Retorna todos os resultados.
        return resultados

    except Exception as erro:
        # Registra erro.
        logger.error(f"Erro durante consultas com BotCity: {erro}")

        # Relança erro.
        raise

    finally:
        # Aguarda 2 segundos para visualizar.
        bot.wait(2000)

        # Fecha o navegador.
        bot.stop_browser()

        # Registra fechamento.
        logger.info("Navegador BotCity fechado.")