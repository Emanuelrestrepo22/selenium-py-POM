from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import List, Union

class Locators:
    """
    Clase que encapsula métodos reutilizables para encontrar y manipular elementos web.
    """

    def __init__(self, driver: WebDriver):
        self.web = driver
        
    def page(self, url: str):
        """Carga una página web en el navegador."""
        self.web.get(url)

    def byId(self, element_id: str) -> WebElement:
        """Encuentra un elemento por su ID."""
        return self.web.find_element(By.ID, element_id)

    def byName(self, name: str) -> WebElement:
        """Encuentra un elemento por su atributo 'name'."""
        return self.web.find_element(By.NAME, name)

    def byCss(self, selector: str) -> WebElement:
        """Encuentra un elemento por selector CSS."""
        return self.web.find_element(By.CSS_SELECTOR, selector)

    def byXpath(self, xpath: str) -> WebElement:
        """Encuentra un elemento por XPATH."""
        return self.web.find_element(By.XPATH, xpath)

    def byDataTest(self, value: str) -> WebElement:
        """Encuentra un elemento usando el atributo 'data-test' (muy común en testing)."""
        return self.web.find_element(By.CSS_SELECTOR, f'[data-test="{value}"]')

    def byClasses(self, class_name: str) -> List[WebElement]:
        """Encuentra una lista de elementos por clase CSS."""
        return self.web.find_elements(By.CLASS_NAME, class_name)

    def waitUntilVisible(self, locator: Union[str, WebElement], timeout=10) -> WebElement:
        """
        Espera hasta que un elemento sea visible antes de interactuar con él.
        Puede recibir un selector CSS (str) o un WebElement.
        """
        if isinstance(locator, str):  # Si es un string, buscar el elemento
            return WebDriverWait(self.web, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
            )
        else:  # Si ya es un WebElement, solo esperar su visibilidad
            return WebDriverWait(self.web, timeout).until(
                EC.visibility_of(locator)
            )

    def pressEnter(self, element: WebElement):
        """Envía la tecla Enter a un elemento."""
        element.send_keys(Keys.ENTER)

    def clickElement(self, element: WebElement):
        """Hace clic en un elemento usando ActionChains (por si hay problemas de visibilidad)."""
        ActionChains(self.web).move_to_element(element).click().perform()
        
    def contains(self, text: str) -> List[WebElement]:
        """Busca elementos que contengan un texto específico."""
        return self.web.find_elements(By.XPATH, f"//*[contains(text(), '{text}')]")
