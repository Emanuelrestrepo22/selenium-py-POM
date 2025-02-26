import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tests.pages.product_list_page import ProductListPage
from tests.pages.login_page import LoginPage
from tests.utils.locators import Locators
from tests.utils.asserts import Expect

# Cargar variables de entorno
load_dotenv()

@pytest.fixture
def driver():
    """Configura y devuelve el WebDriver."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    """Verifica que al hacer click en 'Add to cart', el contador del carrito se actualiza correctamente."""
    
    # Paso 1: Iniciar sesión en la aplicación
    login_page = LoginPage(driver, Locators())
    login_page.go_to_login_page()
    login_page.enterUsername(os.getenv("SWL_USERNAME"))
    login_page.enterPassword(os.getenv("SWL_PASSWORD"))
    login_page.submitLogin()

    # Paso 2: Navegar a la página de productos
    product_list_page = ProductListPage(driver, Locators())
    product_list_page.go_to_product_list()

    # Paso 3: Seleccionar productos y hacer click en "Add to cart"
    products = product_list_page.get_product_list()
    num_products_to_add = min(3, len(products))  # Agregar hasta 3 productos si hay suficientes
    
    for i in range(num_products_to_add):
        product_name = product_list_page.get_product_name(products[i])
        assert product_list_page.add_product_to_cart(product_name)  # Validar que se agregó

    # Paso 4: Verificar el número de productos en el badge
    cart_count = product_list_page.get_cart_count()
    expect = Expect(cart_count)
    expect.toBeEqual(num_products_to_add)

    print(f"✅ Se agregaron {num_products_to_add} productos al carrito y el badge muestra {cart_count}")
