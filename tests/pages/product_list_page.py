from tests.pages.base_page import BasePage
from dotenv import load_dotenv

load_dotenv()
class ProductListPage(BasePage):
    """POM to product list page."""
    
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.endpoint = "/inventory.html"
        
    def go_to_product_list(self):
        self.go_to_page(self.endpoint)
        
    def get_product_list(self):
        return super().get_product_list()
    
    def get_product_name(self, product_element):
        return super().get_product_name(product_element)
    def add_product_to_cart(self, product_name):
        return super().add_product_to_cart(product_name)
    def remove_first_product_from_cart(self):
        return super().remove_first_product_from_cart()
    
    def remove_product_from_cart(self, product_name):
        return super().remove_product_from_cart(product_name)