import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple, Dict  # ✅ Corrección de import

from tests.testbase import *
from tests.utils.asserts import Expect
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators
from tests.pages.login_page import LoginPage  # ✅ Importar LoginPage

Test = Tuple[WebDriver, Locators]  # ✅ Definir Test correctamente

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
    run = True if headless == "true" else False

    BROWSER_FUNCTIONS = {
        "chrome": Drivers(run).chromeDriver,
        "edge": Drivers(run).edgeDriver,
        "firefox": Drivers(run).firefoxDriver
    }
    driver = BROWSER_FUNCTIONS.get(browser)
    if not driver:
        raise ValueError(f'Browser "{browser}" not supported.')

    runDriver: WebDriver = driver()
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

    title = web.title
    assert title == "Google"

    yield (web, get)
    web.quit()

@pytest.fixture
def beforeEach(setWebDriver: WebDriver):
    web = setWebDriver
    get = Locators(web)
    web.implicitly_wait(10)
    get.page("https://www.saucedemo.com/")
    title = web.title
    assert title == "Swag Labs"
    yield (web, get)
    web.quit()

@pytest.fixture
def validUser():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

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

if __name__ == "__main__":
    pytest.main()
