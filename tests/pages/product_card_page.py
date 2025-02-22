from selenium.webdriver.common.by import By
from utils.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import Actions

class ProductCardPage:
    def __init__(self, driver, product_element):
        self.web = driver
        self.actions = Actions(driver)
        self.product = product_element
        
        #locators in each card
        self.title = (By.CSS_SELECTOR, '.inventory_item_name')
        self.description = (By.CSS_SELECTOR, '.inventory_item_description')
        self.price = (By.CSS_SELECTOR, '.inventory_item_price')
        self.add_to_cart_button = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        self.remove_button = (By.CSS_SELECTOR, '[data-test^="remove"]')
        
    def get_title(self):
        """get title of product"""
        return self.actions.get_text((By.CSS_SELECTOR, ''))
    
    def remove_from_cart(self):
        """Doing click on button 'add to cart'"""
        self.actions.click_element(self.remove_button)
        
    def go_product_detail(self):
        """Doing click on product's title to open product detail"""
        self.actions.click_element(self.title)