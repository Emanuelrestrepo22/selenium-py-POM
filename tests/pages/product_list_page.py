import os 
from dotenv import load_dotenv  # Cargar variables de entorno
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.locators import Locators

# Cargar variables de entorno
load_dotenv()

class ProductListPage:
    """POM para la página de lista de productos."""

    def __init__(self, driver: WebDriver, locator: Locators):
        self.driver = driver  # WebDriver de Selenium
        self.get = locator  # Instancia de locators para reutilizar selectores
        self.base_url = os.getenv('BASE_URL', "https://www.saucedemo.com")  # Valor por defecto si no existe
        self.endpoint = '/inventory.html'
        self.url = f"{self.base_url}{self.endpoint}"  # Construcción de la URL completa

    ## **🟢 Métodos para Navegación en la Web** ##
    def go_to_product_list(self):
        """Navega a la página de lista de productos."""
        self.driver.get(self.url)
    
    ## **🟢 Métodos para Interacción con el Carrito** ##
    def open_cart(self):
        """Hace clic en el icono del carrito."""
        self.get.byDataTest('shopping-cart-link').click()

    def get_cart_count(self):
        """Devuelve la cantidad de productos en el carrito."""
        try:
            badge = self.get.byDataTest('shopping-cart-badge')
            return int(badge.text) if badge else 0
        except:
            return 0  # Si el badge no existe, el carrito está vacío

    ## **🟢 Métodos para Interacción con Productos** ##
    def get_product_list(self):
        """Obtiene la lista de todos los productos en la página."""
        return self.get.allByDataTest('inventory-item')

    def get_product_name(self, product_element):
        """Obtiene el nombre de un producto desde su card."""
        return product_element.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]').text

    def get_product_price(self, product_element):
        """Obtiene el precio de un producto desde su card."""
        return product_element.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-price"]').text

    def add_product_to_cart(self, product_name):
        """Añade un producto al carrito usando su nombre."""
        products = self.get_product_list()
        for product in products:
            if self.get_product_name(product) == product_name:
                product.find_element(By.CSS_SELECTOR, '[data-test^="add-to-cart"]').click()
                return True  # Producto añadido al carrito
        return False  # Producto no encontrado

    def remove_product_from_cart(self, product_name):
        """Elimina un producto del carrito usando su nombre."""
        products = self.get_product_list()
        for product in products:
            if self.get_product_name(product) == product_name:
                product.find_element(By.CSS_SELECTOR, '[data-test^="remove"]').click()