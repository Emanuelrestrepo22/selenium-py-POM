from faker import Faker
import pytest
import os
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple, Dict, Optional
from tests.pages.cart_page import CartPage
from tests.pages.fill_form_checkout_page import FillFormCheckout
from tests.testbase import *
from tests.utils.asserts import Expect
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators
from tests.pages.login_page import LoginPage
from tests.pages.product_list_page import ProductListPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
import requests
from tests.utils.browser_helper import set_session_username, set_cart_contents



#alias para tipo de datos utilizando pruebas
Test = Tuple[WebDriver, Locators]

def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to use: chrome, edge, firefox",
        choices=("chrome", "edge", "firefox"),
    )
    parser.addoption(
        "--headless", action="store", default="false",
        help="Test execution in headless: true or false",
        choices=("true", "false"),
    )

@pytest.fixture
def browser(request: pytest.FixtureRequest):
    return request.config.getoption("--browser")

@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")

@pytest.fixture
def setWebDriver(headless: str, browser: str):
    run = headless.lower() == "true"

    BROWSER_FUNCTIONS = {
        "chrome": Drivers(run).chromeDriver,
        "edge": Drivers(run).edgeDriver,
        "firefox": Drivers(run).firefoxDriver
    }
    
    driver_function = BROWSER_FUNCTIONS.get(browser)
    if not driver_function:
        raise ValueError(f'Browser "{browser}" not supported.')

    runDriver: WebDriver = driver_function()
    return runDriver

@pytest.fixture
def web(setWebDriver: WebDriver):
    return setWebDriver

@pytest.fixture
def get(web: WebDriver):
    return Locators(web)

@pytest.fixture
def setup(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)

    web.implicitly_wait(10)
    get.page("https://google.com")

    assert web.title == "Google"

    yield (web, get)
    web.quit()

@pytest.fixture
def beforeEach(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)
    web.implicitly_wait(10)
    get.page("https://www.saucedemo.com/")
    
    assert web.title == "Swag Labs"
    
    yield (web, get)
    web.quit()

@pytest.fixture
def validUser() -> Dict[str, str]:
    username = os.getenv("SWL_USERNAME", "").strip()
    password = os.getenv("SWL_PASSWORD", "").strip()

    if not username or not password:
        pytest.fail("Las credenciales no están definidas en las variables de entorno.")

    return {"username": username, "password": password}

@pytest.fixture
def driver(setWebDriver: WebDriver):
    """Devuelve el WebDriver configurado y lo cierra después de la ejecución."""
    web_driver = setWebDriver
    yield web_driver
    web_driver.quit()

@pytest.fixture
def loginSuccessful(beforeEach: Test, validUser: Dict[str, str]):
    web, get = beforeEach
    loginPage = LoginPage(web, get) 

    loginPage.enterUsername(validUser["username"])
    loginPage.enterPassword(validUser["password"])
    loginPage.submitLogin()

    expect = Expect(web.current_url)  
    expect.toContain("/inventory")

    yield (web, get)
    
@pytest.fixture
def cart_with_items(loginSuccessful: Test):
    """
    Fixture que realiza login exitoso y añade productos al carrito.
    Devuelve el driver, los localizadores y los productos añadidos.
    """
    web, get = loginSuccessful
    product_list = ProductListPage(web, get)

    # Cantidad configurable si se quiere ajustar
    num_products_to_add = 5
    added_products = product_list.add_n_products_to_cart(num_products_to_add)

    yield web, get, added_products
@pytest.fixture
def overview_ready(cart_with_items):
    """
    Usuario logueado, carrito listo y formulario completado, parado en checkout overview (/checkout-step-two.html).
    """
    web, get, added_products = cart_with_items
    fake = Faker()

    # Ir al carrito y hacer click en Checkout
    product_list = ProductListPage(web, get)
    product_list.open_cart()

    cart_page = CartPage(web, get)
    cart_page.go_to_checkout()

    # Llenar formulario de checkout
    form_page = FillFormCheckout(web, get)
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="firstName"]'))
    )
    get.byDataTest(form_page.first_name_input).send_keys(fake.first_name())
    get.byDataTest(form_page.last_name_input).send_keys(fake.last_name())
    get.byDataTest(form_page.postal_code_input).send_keys(fake.postcode())
    get.byDataTest(form_page.continue_button).click()

    # Validar llegada a checkout overview
    WebDriverWait(web, 10).until(EC.url_contains("checkout-step-two"))
    assert "checkout-step-two" in web.current_url, "No se redirigió correctamente a Checkout Overview."

    yield web, get, added_products




@pytest.fixture
def cart_with_local_storage(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)

    web.get("https://www.saucedemo.com/")

    # Setear cookie de sesión
    set_session_username(web, "standard_user")

    # Setear productos en carrito (IDs como string)
    product_ids = ["4", "1", "0"]  # IDs según la aplicación (ajustar si es necesario)
    set_cart_contents(web, product_ids)

    web.refresh()

    yield web, get, product_ids

    web.quit()

if __name__ == "__main__":
    pytest.main()
