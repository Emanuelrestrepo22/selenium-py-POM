from selenium.webdriver.common.by import By
from utils.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import Actions

class ProductListPage:
    def __init__(self, driver):
        self.web = driver
        self.actions = Actions(driver)
        self.cart_icon = self.web.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        self.cart_badge = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        self.product_cards_locator = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
        
    def get_cart_count(self):
        """got count  of products in the cart"""
        cart_elements =self.actions.wait_until_all_elements_present(self.cart_badge, timeout= 5)
        return int(cart_elements[0].text) if cart_elements else 0
    
    def open_cart(self):
        """Doing click on cart's icon"""
        self.actions.click_element(self.cart_icon)
        
    def get_produt_cart(self):
        """return a list with all visible cardsin the page """
        product_elements =self.actions.wait_until_all_elements_present(self.product_cards_locator)
        return [ProductListPage(self.web, elem) for elem in product_elements]