# tests/pages/product_list_page.py

from tests.pages.base_page import BasePage

class ProductListPage(BasePage):
    """Página específica de la lista de productos."""
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.endpoint = '/inventory.html'
        self.url = f"{self.base_url}{self.endpoint}"

    def go_to_product_list(self):
        self.driver.get(self.url)