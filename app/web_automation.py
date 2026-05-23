import time
from selenium import webdriver

# Importa By, usado para localizar elementos na página.
# Exemplo: localizar por ID, classe, nome, seletor CSS etc.
from selenium.webdriver.common.by import By

# Importa Service, usado para configurar o serviço do ChromeDriver.
from selenium.webdriver.chrome.service import Service

# Importa ChromeDriverManager.
# Ele baixa e configura automaticamente o ChromeDriver correto.
from webdriver_manager.chrome import ChromeDriverManager

# Importa a URL da página local criada no arquivo config.py.
from app.config import WEB_PAGE_URL

# Importa a configuração de logger do projeto.
from app.logger_config import configurar_logger


# Cria o logger deste arquivo.
logger = configurar_logger()


def iniciar_navegador():
    # Registra no log que o navegador será iniciado.
    logger.info("Iniciando navegador Chrome.")

    # Cria as opções de configuração do navegador Chrome.
    options = webdriver.ChromeOptions()

    # Maximiza a janela do navegador ao abrir.
    options.add_argument("--start-maximized")

    # Cria o serviço do ChromeDriver.
    # O ChromeDriverManager().install() baixa ou localiza o driver compatível.
    service = Service(ChromeDriverManager().install())

    # Cria o navegador controlado pelo Selenium.
    driver = webdriver.Chrome(service=service, options=options)

    # Retorna o navegador para ser usado em outras funções.
    return driver


def consultar_registro(codigo: str):
    # Inicia o navegador.
    driver = iniciar_navegador()

    try:
        # Registra no log qual página será aberta.
        logger.info(f"Abrindo página local: {WEB_PAGE_URL}")

        # Abre a página HTML local no navegador.
        driver.get(WEB_PAGE_URL)

        # Aguarda 1 segundo para garantir que a página carregou.
        time.sleep(1)

        # Localiza o campo de código pelo ID "codigo".
        campo_codigo = driver.find_element(By.ID, "codigo")

        # Limpa o campo antes de digitar.
        campo_codigo.clear()

        # Digita o código recebido como parâmetro.
        campo_codigo.send_keys(codigo)

        # Registra no log o código digitado.
        logger.info(f"Código digitado na página: {codigo}")

        # Localiza o botão da página usando seletor CSS.
        # Como só existe um botão na página, podemos buscar por "button".
        botao_consultar = driver.find_element(By.CSS_SELECTOR, "button")

        # Clica no botão consultar.
        botao_consultar.click()

        # Aguarda um pouco para o resultado aparecer.
        time.sleep(1)

        # Localiza o campo onde aparece o nome.
        campo_nome = driver.find_element(By.ID, "nome")

        # Localiza o campo onde aparece o status.
        campo_status = driver.find_element(By.ID, "status")

        # Localiza o campo onde aparece a mensagem.
        campo_mensagem = driver.find_element(By.ID, "mensagem")

        # Pega o texto exibido no campo de nome.
        nome = campo_nome.text

        # Pega o texto exibido no campo de status.
        status = campo_status.text

        # Pega o texto exibido no campo de mensagem.
        mensagem = campo_mensagem.text

        # Registra o resultado no log.
        logger.info(
            f"Resultado da consulta - Código: {codigo}, Nome: {nome}, Status: {status}, Mensagem: {mensagem}"
        )

        # Retorna os dados encontrados em formato de dicionário.
        return {
            "codigo": codigo,
            "nome": nome,
            "status_encontrado": status,
            "mensagem": mensagem
        }

    except Exception as erro:
        # Registra no log qualquer erro que acontecer durante a automação.
        logger.error(f"Erro ao consultar registro {codigo}: {erro}")

        # Lança o erro novamente para o programa principal saber que deu problema.
        raise

    finally:
        # Aguarda 2 segundos antes de fechar para você conseguir ver o resultado.
        time.sleep(2)

        # Fecha o navegador.
        driver.quit()

        # Registra no log que o navegador foi fechado.
        logger.info("Navegador fechado.")