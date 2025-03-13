import pytest
import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple, Dict, Optional
from tests.testbase import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from tests.utils.asserts import Expect
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators
from tests.pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

#alias para tipo de datos utilizando pruebas
Test = Tuple[WebDriver, Locators]

def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to use: chrome, edge, firefox",
        choices=("chrome", "edge", "firefox"),
    )
    parser.addoption(
        "--headless", action="store", default="false",
        help="Test execution in headless: true or false",
        choices=("true", "false"),
    )

@pytest.fixture
def browser(request: pytest.FixtureRequest):
    return request.config.getoption("--browser")

@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")

@pytest.fixture
def setWebDriver(headless: str, browser: str):
    run = headless.lower() == "true"

    chrome_options = Options()

    # 🚀 Opciones para evitar errores SSL y otros errores de conexión
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--log-level=3")

    # 🔹 Solución: Forzar Modo Incógnito en lugar de usar `--user-data-dir`
    chrome_options.add_argument("--incognito")

    # 🔹 Modo Headless en entornos CI/CD
    if run:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 🚀 Configuración del Driver según el navegador
    if browser != "chrome":
        raise ValueError(f'Browser "{browser}" not supported.')

    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)
@pytest.fixture
def web(setWebDriver: WebDriver):
    return setWebDriver

@pytest.fixture
def get(web: WebDriver):
    return Locators(web)

@pytest.fixture
def setup(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)

    web.implicitly_wait(10)
    get.page("https://google.com")

    assert web.title == "Google"

    yield (web, get)
    web.quit()

@pytest.fixture
def beforeEach(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)
    web.implicitly_wait(10)
    get.page("https://www.saucedemo.com/")
    
    assert web.title == "Swag Labs"
    
    yield (web, get)
    web.quit()

@pytest.fixture
def validUser() -> Dict[str, str]:
    username = os.getenv("SWL_USERNAME", "").strip()
    password = os.getenv("SWL_PASSWORD", "").strip()

    if not username or not password:
        pytest.fail("Las credenciales no están definidas en las variables de entorno.")

    return {"username": username, "password": password}

@pytest.fixture
def driver(setWebDriver: WebDriver):
    
    """Configura y devuelve el WebDriver con opciones avanzadas para evitar errores SSL."""
    chrome_options = Options()
    
    # 🚀 Opciones para evitar errores SSL
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignorar errores de certificado
    chrome_options.add_argument("--allow-insecure-localhost")  # Permitir localhost con SSL inválido
    chrome_options.add_argument("--allow-running-insecure-content")  # Permitir contenido inseguro
    chrome_options.add_argument("--disable-web-security")  # Deshabilitar seguridad web
    chrome_options.add_argument("--ignore-ssl-errors")  # Ignorar errores SSL
    chrome_options.add_argument("--disable-popup-blocking")  # Evitar bloqueos inesperados
    chrome_options.add_argument("--log-level=3")  # Reducir el nivel de logs para menos ruido en consola
    
    # Opciones de ejecución en entornos CI/CD
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    """Devuelve el WebDriver configurado y lo cierra después de la ejecución."""
    web_driver = setWebDriver
    yield web_driver
    web_driver.quit()

@pytest.fixture
def loginSuccessful(beforeEach: Test, validUser: Dict[str, str]):
    web, get = beforeEach
    loginPage = LoginPage(web, get) 

    loginPage.enterUsername(validUser["username"])
    loginPage.enterPassword(validUser["password"])
    loginPage.submitLogin()

    expect = Expect(web.current_url)  
    expect.toContain("/inventory")

    yield (web, get)

if __name__ == "__main__":
    pytest.main()
