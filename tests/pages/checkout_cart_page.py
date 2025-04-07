import os
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.locators import Locators
from tests.pages.product_list_page import ProductListPage

# Load environment variables
load_dotenv()

class CheckoutCartPage(ProductListPage):
    """Page Object Model: Checkout Cart Page."""

    def __init__(self, driver: WebDriver, locator: Locators):
        super().__init__(driver, locator)
        self.endpoint = '/inventory.html'  # You can override if needed
        self.url = f"{self.base_url}{self.endpoint}"

        # 🛒 Cart & Checkout buttons
        self.icon_cart = '[data-test="shopping-cart-link"]'
        self.cart_container = '[data-test="cart-list"]'
        self.cart_item = '[data-test="inventory-item"]'
        self.remove_button = '[data-test^="remove-sauce-labs"]'
        self.checkout_button = '[data-test="checkout"]'
        self.continue_shopping_button = '[data-test="continue-shopping"]'

        # 📝 Form inputs
        self.first_name_input = 'firstName'
        self.last_name_input = 'lastName'
        self.postal_code_input = 'postalCode'
        self.cancel_button = 'cancel'
        self.continue_button = 'continue'

        # 📦 Summary & Finish
        self.checkout_step_two_url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.subtotal_label = '[data-test="subtotal-label"]'
        self.tax_label = '[data-test="tax-label"]'
        self.total_label = '[data-test="total-label"]'
        self.finish_button = '[data-test="finish"]'
        self.checkout_title = '[data-test="title"]'

    # ✅ Métodos heredados como `go_to_product_list()` ya están disponibles

    def open_cart(self):
        self.get.byDataTest("shopping-cart-link").click()

    def back_to_product_list(self):
        self.get.byDataTest("continue-shopping").click()

    def click_checkout(self):
        """Click on 'Checkout' button to proceed to form."""
        self.get.byDataTest("checkout").click()

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """Fill form with customer data (faker will be used)."""
        self.get.byDataTest(self.first_name_input).send_keys(first_name)
        self.get.byDataTest(self.last_name_input).send_keys(last_name)
        self.get.byDataTest(self.postal_code_input).send_keys(postal_code)
        self.get.byDataTest(self.continue_button).click()
