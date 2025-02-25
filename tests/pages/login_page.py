import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators  # Importamos Locators
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv() #got aour .env vars
class LoginPage:
    """
    Class that represents login using POM.
    """
    def __init__(self, driver: WebDriver, locator: Locators):
        self.web = driver  # saved webdriver successfully
        self.get = locator  # using right 'locator'
        self.url = os.getenv('LOGIN_URL', 'https://www.saucedemo.com/')
        
    def go_to_login_page(self):
        self.web.get(self.url)
    
    def enterUsername(self, username: str):
        """Ingresa el nombre de usuario."""
        self.get.byDataTest('username').send_keys(username)

    def enterPassword(self, password: str):
        """Ingresa la contraseña."""
        self.get.byDataTest('password').send_keys(password)

    def submitLogin(self):
        """Hace clic en el botón de login."""
        self.get.byDataTest('login-button').click()
