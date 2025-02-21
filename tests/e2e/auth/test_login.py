import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.login_page import LoginPage
from tests.utils.asserts import Expect
from typing import Tuple, Dict

class TestLogin:
    """
    Clase de pruebas para validar el proceso de login.
    """

    def test_successful_login(self, beforeEach: Tuple[WebDriver, object], validUser: Dict[str, str]):
        """
        Verifica que un usuario válido pueda iniciar sesión correctamente.
        """
        web, get = beforeEach  # Obtenemos el WebDriver y el Locator
        loginPage = LoginPage(web, get)  # Creamos una instancia de LoginPage

        # Realizamos el proceso de login
        loginPage.enterUsername(validUser["username"])
        loginPage.enterPassword(validUser["password"])
        loginPage.submitLogin()

        # Validamos que el usuario haya ingresado correctamente
        expect = Expect(web.current_url)
        expect.toContain("/inventory")

        # Validamos que el nombre de usuario sea visible
        user_menu = web.find_element("css selector", ".bm-burger-button")
        assert user_menu.is_displayed()
