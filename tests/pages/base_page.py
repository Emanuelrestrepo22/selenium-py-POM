# tests/pages/base_page.py

import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from typing import List

load_dotenv()

class BasePage:
    """BasePage con funcionalidad compartida entre múltiples páginas."""
    def __init__(self, driver: WebDriver, locator: Locators):
        self.driver = driver
        self.get = locator
        self.base_url = os.getenv('BASE_URL', "https://www.saucedemo.com")

        # Selectores compartidos
        self.cart_item = 'inventory_item'
        self.product_name_selector = '[data-test="inventory-item-name"]'
        self.product_price_selector = '[data-test="inventory-item-price"]'
        self.add_to_cart_selector = '[data-test^="add-to-cart"]'
        self.remove_from_cart_selector = '[data-test^="remove-sauce-labs"]'
        self.cart_link_selector = 'shopping-cart-link'
        self.cart_badge_selector = 'shopping-cart-badge'

    def open_cart(self):
        self.get.byDataTest(self.cart_link_selector).click()

    def get_cart_count(self):
        try:
            badge = self.get.byDataTest(self.cart_badge_selector)
            return int(badge.text) if badge else 0
        except:
            return 0

    def get_product_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.cart_item))
        )
        return self.get.byClasses(self.cart_item)

    def get_product_name(self, product_element):
        return product_element.find_element(By.CSS_SELECTOR, self.product_name_selector).text

    def get_product_price(self, product_element):
        price = product_element.find_element(By.CSS_SELECTOR, self.product_price_selector).text
        return float(price.replace('$', ''))

    def add_product_to_cart(self, product_name):
        products = self.get_product_list()
        for product in products:
            if self.get_product_name(product) == product_name:
                add_button = product.find_elements(By.CSS_SELECTOR, self.add_to_cart_selector)
                remove_button = product.find_elements(By.CSS_SELECTOR, self.remove_from_cart_selector)
                if remove_button:
                    return False
                if add_button:
                    add_button[0].click()
                    return True
        return False

    def remove_product_from_cart(self):
        if "/inventory.html" not in self.driver.current_url:
            self.driver.get(f"{self.base_url}/inventory.html")

        products = self.get_product_list()
        removed_count = 0

        for product in products:
            remove_buttons = product.find_elements(By.CSS_SELECTOR, self.remove_from_cart_selector)
            if remove_buttons:
                remove_buttons[0].click()
                removed_count += 1

        return removed_count

    def add_n_products_to_cart(self, n: int) -> List[str]:
        products = self.get_product_list()
        added = []
        for i in range(min(n, len(products))):
            name = self.get_product_name(products[i])
            if self.add_product_to_cart(name):
                added.append(name)
        return added
