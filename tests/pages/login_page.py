from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locator import Locator  # Importamos el nuevo Locator

class LoginPage:
    """
    Clase que representa la página de Login usando el patrón POM.
    """
    def __init__(self, driver: WebDriver):
        self.get = Locator(driver)  # Instancia de Locator

    def enterUsername(self, username: str):
        """Ingresa el nombre de usuario."""
        self.get.byDataTest('username').send_keys(username)

    def enterPassword(self, password: str):
        """Ingresa la contraseña."""
        self.get.byDataTest('password').send_keys(password)

    def submitLogin(self):
        """Hace clic en el botón de login."""
        self.get.byDataTest('login-button').click()
