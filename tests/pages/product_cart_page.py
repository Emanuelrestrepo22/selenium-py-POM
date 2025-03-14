import os 
from dotenv import load_dotenv  # Cargar variables de entorno
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.locators import Locators
from tests.pages.product_list_page import ProductListPage


load_dotenv()
from tests.pages.product_list_page import ProductListPage  # Heredamos de ProductListPage

class ProductCartPage(ProductListPage):
    def __init__(self, driver: WebDriver, locator: Locators):
        super().__init__(driver, locator)
        self.endpoint = '/cart.html'  # Definimos un nuevo endpoint para la página del carrito
        self.url = f"{self.base_url}{self.endpoint}"  # Nueva URL basada en la del padre
    
        
    def go_to_cart_page(self):
        self.driver.get(self.url)
        
    def get_cart_items(self):
        #return all elements in the cart
        cart_container = self.get.byDataTest('cart-list')
        return cart_container.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    