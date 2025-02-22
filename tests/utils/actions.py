from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Actions:
    """
    Clase de utilidades para encapsular acciones reutilizables con Selenium WebDriver.
    """

    def __init__(self, driver: WebDriver):
        self.web = driver

    def wait_until_visible(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Espera hasta que un elemento sea visible antes de interactuar con él."""
        return WebDriverWait(self.web, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Espera hasta que un elemento sea clickeable antes de hacer clic."""
        return WebDriverWait(self.web, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_presence(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Espera hasta que un elemento esté presente en el DOM."""
        return WebDriverWait(self.web, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_until_all_elements_present(self, locator: tuple, timeout: int = 10):
        """Espera hasta que varios elementos estén presentes en el DOM y los devuelve en una lista."""
        return WebDriverWait(self.web, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator: tuple, timeout: int = 10):
        """Espera a que un elemento sea clickeable y lo hace clic."""
        element = self.wait_until_clickable(locator, timeout)
        element.click()

    def get_text(self, locator: tuple, timeout: int = 10) -> str:
        """Espera a que un elemento sea visible y devuelve su texto."""
        return self.wait_until_visible(locator, timeout).text

    def get_attribute(self, locator: tuple, attribute: str, timeout: int = 10) -> str:
        """Espera a que un elemento sea visible y devuelve el valor de un atributo."""
        return self.wait_until_visible(locator, timeout).get_attribute(attribute)
