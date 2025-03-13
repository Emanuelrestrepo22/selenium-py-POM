import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from tests.utils.locators import Locators
from tests.pages.login_page import LoginPage
from tests.utils.asserts import Expect
from typing import Tuple, Dict

Test = Tuple[webdriver.Chrome, Locators]

def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--browser", action="store", default="chrome", choices=("chrome",))
    parser.addoption("--headless", action="store", default="false", choices=("true", "false"))

@pytest.fixture
def browser(request: pytest.FixtureRequest):
    return request.config.getoption("--browser")

@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")

@pytest.fixture
def setWebDriver(headless: str):
    """
    Configura y devuelve el WebDriver de Chrome con opciones optimizadas para CI/CD.
    """
    run = headless.lower() == "true"
    chrome_options = Options()

    # 🚀 Opciones para mejorar la estabilidad en GitHub Actions
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--log-level=3")

    # 🔹 Evita bloqueos en GitHub Actions
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")

    # 🔹 🔥 **Corrección: Eliminamos --user-data-dir**
    # chrome_options.add_argument(f"--user-data-dir=/tmp/chrome-user-data-{os.getpid()}")  <-- Eliminado

    # 🔹 🔥 **Corrección: Forzar nuevo modo Headless en CI/CD**
    if run:
        chrome_options.add_argument("--headless=new")

    # 🔹 🔥 **Corrección: Agregar opciones para evitar fallos en GitHub Actions**
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Previene errores en memoria compartida
    chrome_options.add_argument("--disable-software-rasterizer")  # Evita fallos gráficos
    chrome_options.add_argument("--remote-debugging-port=9222")  # Previene bloqueos de DevTools

    # 🚀 Inicializar Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

@pytest.fixture
def web(setWebDriver: webdriver.Chrome):
    return setWebDriver

@pytest.fixture
def get(web: webdriver.Chrome):
    return Locators(web)

@pytest.fixture
def setup(setWebDriver: webdriver.Chrome):
    web = setWebDriver
    get = Locators(web)

    web.implicitly_wait(10)
    get.page("https://google.com")

    assert web.title == "Google"

    yield (web, get)
    web.quit()

@pytest.fixture
def beforeEach(setWebDriver: webdriver.Chrome):
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
def driver(setWebDriver: webdriver.Chrome):
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
