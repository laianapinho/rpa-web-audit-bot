# Importa o time, usado para pequenas pausas durante a automação.
import time

# Importa o webdriver do Selenium.
# Ele permite controlar o navegador automaticamente.
from selenium import webdriver

# Importa By, usado para localizar elementos na página.
# Exemplo: By.ID, By.CSS_SELECTOR, By.NAME.
from selenium.webdriver.common.by import By

# Importa Service, usado para configurar o serviço do ChromeDriver.
from selenium.webdriver.chrome.service import Service

# Importa ChromeDriverManager.
# Ele baixa ou encontra automaticamente o ChromeDriver compatível com seu Chrome.
from webdriver_manager.chrome import ChromeDriverManager

# Importa a URL local da página HTML criada no Dia 3.
from app.config import WEB_PAGE_URL

# Importa o logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger para registrar eventos deste arquivo.
logger = configurar_logger()


def iniciar_navegador():
    # Registra no log que o navegador será iniciado.
    logger.info("Iniciando navegador Chrome.")

    # Cria um objeto de opções do Chrome.
    options = webdriver.ChromeOptions()

    # Abre o navegador maximizado.
    options.add_argument("--start-maximized")

    # Cria o serviço do ChromeDriver usando o WebDriver Manager.
    service = Service(ChromeDriverManager().install())

    # Cria o driver do Chrome.
    # O driver é o objeto que controla o navegador.
    driver = webdriver.Chrome(service=service, options=options)

    # Retorna o navegador aberto para outras funções usarem.
    return driver


def abrir_pagina(driver):
    # Registra no log qual página será aberta.
    logger.info(f"Abrindo página local: {WEB_PAGE_URL}")

    # Abre a página HTML local.
    driver.get(WEB_PAGE_URL)

    # Aguarda a página carregar.
    time.sleep(1)


def consultar_registro_com_driver(driver, codigo: str):
    # Registra no log qual código será consultado.
    logger.info(f"Iniciando consulta do código: {codigo}")

    # Localiza o campo de código pelo ID "codigo".
    campo_codigo = driver.find_element(By.ID, "codigo")

    # Limpa o campo antes de digitar o próximo código.
    campo_codigo.clear()

    # Digita o código no campo da página.
    campo_codigo.send_keys(codigo)

    # Localiza o botão de consulta.
    botao_consultar = driver.find_element(By.CSS_SELECTOR, "button")

    # Clica no botão.
    botao_consultar.click()

    # Aguarda o resultado aparecer na tela.
    time.sleep(0.5)

    # Localiza o campo de nome pelo ID "nome".
    campo_nome = driver.find_element(By.ID, "nome")

    # Localiza o campo de status pelo ID "status".
    campo_status = driver.find_element(By.ID, "status")

    # Localiza o campo de mensagem pelo ID "mensagem".
    campo_mensagem = driver.find_element(By.ID, "mensagem")

    # Pega o texto do nome exibido na tela.
    nome = campo_nome.text

    # Pega o texto do status exibido na tela.
    status = campo_status.text

    # Pega o texto da mensagem exibida na tela.
    mensagem = campo_mensagem.text

    # Registra o resultado no log.
    logger.info(
        f"Consulta finalizada - Código: {codigo}, Nome: {nome}, Status: {status}, Mensagem: {mensagem}"
    )

    # Retorna os dados encontrados em formato de dicionário.
    return {
        "codigo": codigo,
        "nome_encontrado": nome,
        "status_encontrado": status,
        "mensagem": mensagem
    }


def consultar_varios_registros(codigos):
    # Cria uma lista vazia para guardar os resultados.
    resultados = []

    # Inicia o navegador apenas uma vez.
    driver = iniciar_navegador()

    try:
        # Abre a página local apenas uma vez.
        abrir_pagina(driver)

        # Percorre cada código recebido na lista.
        for codigo in codigos:
            # Chama a função que consulta um código usando o navegador já aberto.
            resultado = consultar_registro_com_driver(driver, codigo)

            # Adiciona o resultado na lista de resultados.
            resultados.append(resultado)

        # Retorna a lista com todos os resultados.
        return resultados

    except Exception as erro:
        # Registra qualquer erro que aconteça durante as consultas.
        logger.error(f"Erro durante a consulta de vários registros: {erro}")

        # Lança o erro novamente para o main.py saber que algo deu errado.
        raise

    finally:
        # Espera um pouco para você ver o último resultado na tela.
        time.sleep(2)

        # Fecha o navegador no final.
        driver.quit()

        # Registra no log que o navegador foi fechado.
        logger.info("Navegador fechado.")