import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.pages.product_list_page import ProductListPage
from tests.pages.login_page import LoginPage
from tests.utils.locators import Locators
from tests.utils.asserts import Expect
from selenium.webdriver.support import expected_conditions as EC

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
    login_page = LoginPage(driver, Locators(driver))
    login_page.go_to_login_page()

    # Obtener credenciales
    username = os.getenv("SWL_USERNAME", "").strip()
    password = os.getenv("SWL_PASSWORD", "").strip()
    
    if not username or not password:
        raise ValueError("Las credenciales no están definidas en las variables de entorno.")

    login_page.enterUsername(username)
    login_page.enterPassword(password)
    login_page.submitLogin()

    # Verificar si hay un mensaje de error en el login
    error_message = driver.find_elements(By.CLASS_NAME, "error-message-container")
    if error_message:
        print(" ERROR: Fallo en el login. Verifica las credenciales o si el sitio cambió su flujo.")
        driver.save_screenshot("error_login.png")
        assert False, "El login falló."

    # Esperar hasta que la URL cambie
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    # Validar que el usuario está en la página correcta
    assert "inventory.html" in driver.current_url, "El usuario no fue redirigido a la página de productos."

    # Validar que un elemento clave en la página se ha cargado
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "No se cargó la página de productos después del login."

    """Verifica que al hacer click en 'Add to cart', el contador del carrito se actualiza correctamente."""
    
    # Paso 1: Iniciar sesión en la aplicación
    login_page = LoginPage(driver, Locators(driver))
    login_page.go_to_login_page()
    
    username = os.getenv("SWL_USERNAME", "").strip()
    password = os.getenv("SWL_PASSWORD", "").strip()
    if not username or not password:
        raise ValueError("Las credenciales no están definidas en las variables de entorno.")
    login_page.enterUsername(username)
    login_page.enterPassword(password)
    
    # Verificar si hay un mensaje de error en la página
    error_message = driver.find_elements(By.CLASS_NAME, "error-message-container")
    if error_message:
        print(" ERROR: Fallo en el login. Verifica las credenciales o si el sitio cambió su flujo.")
        driver.save_screenshot("error_login.png")  # Guardar una captura para depurar
    

    # Paso 2: Navegar a la página de productos
    product_list_page = ProductListPage(driver, Locators(driver))
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

    print(f"Se agregaron {num_products_to_add} productos al carrito y el badge muestra {cart_count}")
