from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.utils.locators import Locators

def before_all(context):
    """Se ejecuta una vez antes de cualquier test para inicializar el WebDriver."""
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.locators = Locators(context.driver)  # Instancia de locators

def after_all(context):
    """Se ejecuta una vez después de todos los tests para cerrar el WebDriver."""
    context.driver.quit()

def before_scenario(context, scenario):
    """Se ejecuta antes de cada escenario."""
    print(f"\n🔹 Iniciando escenario: {scenario.name}")

def after_scenario(context, scenario):
    """Se ejecuta después de cada escenario."""
    print(f"\n✅ Finalizado escenario: {scenario.name}")
