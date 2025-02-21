# -----
# * aquí se instancia todos los WebDrivers que se necesiten
import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOpt

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOpt
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOpt
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--headless", action="store", default="false",
        help="Test execution in headless: true or false",
        choices=("true", "false"),
    )


@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")


class Drivers:

    def __init__(self, isHeadless=False) -> None:
        self.isHeadless = isHeadless

    def chromeDriver(self):
        """ Se crea una instancia del ChromeDriver con configuraciones optimizadas """
        execution = ChromeOpt()
        
        #Opciones necesarias para evitar errores en github Actions
        execution.add_argument("--no-sandbox")  # Evita problemas en GitHub Actions
        execution.add_argument("--disable-dev-shm-usage")  # Optimiza memoria en entornos Linux
        execution.add_argument("--disable-gpu")  # Evita problemas gráficos en CI
        execution.add_argument("--incognito")  # Modo incógnito para evitar conflictos de usuario
        execution.add_argument("--disable-extensions")  # Reduce interferencias
        execution.add_argument("--remote-allow-origins=*")  # Evita restricciones remotas
        execution.add_argument("--disable-infobars")  # Oculta mensajes emergentes de Chrome
        execution.add_argument("--disable-popup-blocking")  # Evita bloqueos de popups
        execution.add_argument("--disable-blink-features=AutomationControlled")  # Evita detección de automatización
        execution.add_argument("--headless")  # Corre en modo headless (necesario en GitHub Actions)

        # 🔹 SOLUCIÓN DEL ERROR: Especificar un perfil de usuario temporal para evitar conflictos
        execution.add_argument(f"--user-data-dir=/tmp/chrome-test-profile-{self.isHeadless}")

        return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=execution)

    def edgeDriver(self):
        """ Se crea una instancia del Microsoft Edge con configuraciones optimizadas """
        execution = EdgeOpt()
        execution.add_argument("--no-sandbox")
        execution.add_argument("--disable-dev-shm-usage")
        execution.add_argument("--disable-gpu")
        execution.add_argument("--incognito")
        execution.add_argument("--disable-extensions")
        if self.isHeadless:
            execution.add_argument("--headless")
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=execution)

    def firefoxDriver(self):
        """ Se crea una instancia del FireFox con configuraciones optimizadas """
        execution = FirefoxOpt()
        execution.add_argument("--no-sandbox")
        execution.add_argument("--disable-dev-shm-usage")
        execution.add_argument("--disable-gpu")
        execution.add_argument("--incognito")
        execution.add_argument("--disable-extensions")
        if self.isHeadless:
            execution.add_argument("--headless")
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=execution)


if __name__ == "__main__":
    pytest.main()
    