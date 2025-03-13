from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from tests.utils.locators import Locators

def before_all(context):
    """Se ejecuta una vez antes de cualquier test para inicializar el WebDriver."""
    chrome_options = Options()

    # 🚀 Opciones para evitar errores SSL y mejorar estabilidad
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--log-level=3")  

    # 🔹 Modo Headless en entornos CI/CD
    chrome_options.add_argument("--headless")  # No UI
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        context.driver.maximize_window()
        context.locators = Locators(context.driver)  # Instancia de locators
    except Exception as e:
        print(f" Error al iniciar WebDriver: {e}")
        raise

def after_all(context):
    """Se ejecuta una vez después de todos los tests para cerrar el WebDriver."""
    if context.driver:
        context.driver.quit()

def before_scenario(context, scenario):
    """Se ejecuta antes de cada escenario."""
    print(f"\n🔹 Iniciando escenario: {scenario.name}")

def after_scenario(context, scenario):
    """Se ejecuta después de cada escenario."""
    if scenario.status == "failed":
        print(f"\n Escenario fallido: {scenario.name}")
        context.driver.save_screenshot(f"screenshots/{scenario.name}.png")
    else:
        print(f"\n Finalizado escenario: {scenario.name}")
