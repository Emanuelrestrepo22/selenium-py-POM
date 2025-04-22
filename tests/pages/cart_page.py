import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.pages.base_page import BasePage

# Load environment variables
load_dotenv()

class CartPage(BasePage):
    """Page Object Model: Checkout Cart Page - Flujo de Checkout completo."""

    def __init__(self, driver: WebDriver, locator: Locators):
        super().__init__(driver, locator)
        self.driver = driver
        self.get = locator
        self.endpoint = '/cart.html'
        self.url = f"{self.base_url}{self.endpoint}"

        # 🛒 Selectores del carrito
        self.cart_container = '[data-test="cart-list"]'
        self.cart_item = '[data-test="inventory-item"]'
        self.remove_button = '[data-test^="remove-sauce-labs"]'
        self.checkout_button = 'checkout'
        self.continue_shopping_button = '[data-test="continue-shopping"]'

        

        # 💵 Selectores del resumen
        self.checkout_step_two_url = f"{self.base_url}/checkout-step-two.html"
        self.subtotal_label = '[data-test="subtotal-label"]'
        self.tax_label = '[data-test="tax-label"]'
        self.total_label = '[data-test="total-label"]'
        self.finish_button = '[data-test="finish"]'

        # ✅ Selectores de página de confirmación
        self.complete_title = '[data-test="title"]'
        self.complete_header = '[data-test="complete-header"]'
        self.complete_text = '[data-test="complete-text"]'
        self.back_home_button = '[data-test="back-to-products"]'


    # ====================
    # 🧭 Navegación
    # ====================
    def open_cart(self):
        self.get.byDataTest("shopping-cart-link").click()

    def back_to_product_list(self):
        self.get.byDataTest("continue-shopping").click()

    def go_to_checkout(self):
        self.get.byDataTest(self.checkout_button).click()


    # ====================
    # 📦 Checkout Overview
    # ====================
    def get_all_cart_prices(self):
        """Suma todos los precios visibles en el carrito."""
        total = 0.0
        items = self.driver.find_elements(By.CSS_SELECTOR, self.cart_item)

        for item in items:
            try:
                price_text = item.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-price"]').text
                price = float(price_text.replace('$', '').strip())
                total += price
            except Exception as e:
                print(f"⚠️ Error al leer precio: {e}")

        print(f"💰 Total en carrito: ${total:.2f}")
        return total

    def get_totals(self):
        """Obtiene subtotal, tax y total final como float."""
        subtotal = float(self.get.byDataTest(self.subtotal_label).text.replace("Item total: $", ""))
        tax = float(self.get.byDataTest(self.tax_label).text.replace("Tax: $", ""))
        total = float(self.get.byDataTest(self.total_label).text.replace("Total: $", ""))
        return subtotal, tax, total

    def click_finish(self):
        self.get.byDataTest(self.finish_button).click()

    # ====================
    # ✅ Confirmación Final
    # ====================
    def assert_order_complete(self):
        """Verifica que la orden haya sido completada correctamente."""
        assert "checkout-complete.html" in self.driver.current_url
        header = self.get.byDataTest(self.complete_header).text
        assert header == "Thank you for your order!"

        message = self.get.byDataTest(self.complete_text).text
        assert "Your order has been dispatched" in message
