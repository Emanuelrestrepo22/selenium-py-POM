from behave import given, when  # type: ignore
from dotenv import load_dotenv
import os

load_dotenv()


@given('que el usuario está en la página de login')
def step_open_login_page(context):
    print("→ Iniciando paso: abrir página de login")
    login_url = os.getenv("LOGIN_URL")
    context.locators.page(login_url)
    context.driver.maximize_window()
    context.locators.waitUntilVisible('[data-test="username"]')
    print("✅ Página de login cargada correctamente")


@when('presiona el botón de login')
def step_click_login_button(context):
    context.locators.clickElement(context.locators.byId("login-button"))
    print("✅ Click en login realizado")
