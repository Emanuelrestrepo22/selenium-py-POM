import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.pages.base_page import BasePage
from faker import Faker

# Load environment variables
load_dotenv()

class FillFormCheckout(BasePage):
    def __init__(self, driver: WebDriver, locator: Locators):
        super().__init__(driver, locator)
        self.driver = driver
        self.get = locator
        self.endpoint = '/checkout-step-one.html'
        self.url = f"{self.base_url}{self.endpoint}"
        
        # 📝 Selectores del formulario
        self.first_name_input = 'firstName'
        self.last_name_input = 'lastName'
        self.postal_code_input = 'postalCode'
        self.cancel_button = 'cancel'
        self.continue_button = 'continue'
        self.checkout_title = '[data-test="title"]'
        self.error_message = '[data-test="error"]'

        # 🔤 Faker data (válido)
        fake = Faker()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.postal_code = fake.postcode()

    # ====================
    # 📝 Formulario de Checkout
    # ====================
    def fill_form(self):
        """Completa el formulario con datos válidos (Faker)."""
        self.get.byDataTest(self.first_name_input).send_keys(self.first_name)
        self.get.byDataTest(self.last_name_input).send_keys(self.last_name)
        self.get.byDataTest(self.postal_code_input).send_keys(self.postal_code)
        self.get.byDataTest(self.continue_button).click()

    def submit_with_fields(self, first_name: str = "", last_name: str = "", postal_code: str = ""):
        """Envía el formulario con valores personalizados (para pruebas negativas)."""
        if first_name:
            self.get.byDataTest(self.first_name_input).send_keys(first_name)
        if last_name:
            self.get.byDataTest(self.last_name_input).send_keys(last_name)
        if postal_code:
            self.get.byDataTest(self.postal_code_input).send_keys(postal_code)
        self.get.byDataTest(self.continue_button).click()

    def get_error_message(self) -> str:
        """Devuelve el mensaje de error visible en el formulario."""
        return self.get.byCss(self.error_message).text
