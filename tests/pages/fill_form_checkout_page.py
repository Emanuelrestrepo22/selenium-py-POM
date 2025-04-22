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
        self.endpoint = '/cart.html'
        self.url = f"{self.base_url}{self.endpoint}"
        
        # 📝 Selectores del formulario
        self.first_name_input = 'firstName'
        self.last_name_input = 'lastName'
        self.postal_code_input = 'postalCode'
        self.cancel_button = 'cancel'
        self.continue_button = 'continue'
        self.checkout_title = '[data-test="title"]'
        
        # 🔤 Faker data (generado una vez al instanciar)
        fake = Faker()
        self.first_name = fake.first_name_female_common()
        self.last_name = fake.last_name_common()
        self.postal_code = fake.postal_code()
        
    # ====================
    # 📝 Formulario de Checkout
    # ====================
    def fill_form(self):
        """Completa el formulario de usuario usando Faker."""
        self.get.byDataTest(self.first_name_input).send_keys(self.first_name)
        self.get.byDataTest(self.last_name_input).send_keys(self.last_name)
        self.get.byDataTest(self.postal_code_input).send_keys(self.postal_code)
        self.get.byDataTest(self.continue_button).click()