import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.pages.cart_page import CartPage

load_dotenv()

class CheckoutOverviewPage(CartPage):
    def __init__(self, driver: WebDriver, locator: Locators):
        super().__init__(driver, locator)
        self.driver = driver
        self.get = locator
        self.endpoint = '/checkout-step-two.html'
        self.url = f"{self.base_url}{self.endpoint}"

        # Selectores específicos de esta página
        self.subtotal_selector = '[data-test="subtotal-label"]'
        self.tax_selector = '[data-test="tax-label"]'
        self.total_selector = '[data-test="total-label"]'
        self.finish_button_selector = '[data-test="finish"]'
        self.title_selector = '[data-test="title"]'

    def get_all_cart_prices(self):
        """Suma todos los precios visibles en el container del carrito"""
        total = 0.0
        try:
            items = self.driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
            print(f"[INFO] Se encontraron {len(items)} productos en el resumen del carrito.")

            for idx, item in enumerate(items, start=1):
                try:
                    price_element = item.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
                    price_text = price_element.text
                    price = float(price_text.replace('$', '').strip())
                    total += price
                    print(f"[OK] Producto {idx}: ${price:.2f}")
                except Exception as e:
                    print(f"[ERROR] No se pudo leer el precio del producto {idx}: {e}")

            print(f"[RESULTADO] Suma total de productos individuales: ${total:.2f}")
        except Exception as e:
            print(f"[ERROR GENERAL] No se pudieron obtener los productos del carrito: {e}")

        return total
