from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

# Agregar el directorio del proyecto al sys.path para importar locators correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from tests.utils.locators import Locators

# Cargar variables desde el archivo .env
load_dotenv()

@given('que el usuario está en la página de login')
def step_open_login_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.locators = Locators(context.driver)  # Instancia de la clase Locators

    login_url = os.getenv("LOGIN_URL", "").strip()
    if not login_url:
        raise ValueError("LOGIN_URL no está definido o está vacío en el archivo .env")

    context.locators.page(login_url)  # Usamos la función `page()` de Locators
    context.driver.maximize_window()

    # Esperamos a que el campo de usuario sea visible antes de continuar
    context.locators.waitUntilVisible('[data-test="username"]')

@when('ingresa su usuario desde el archivo .env')
def step_enter_valid_credentials(context):
    username = os.getenv("SWL_USERNAME")
    password = os.getenv("SWL_PASSWORD")

    username_field = context.locators.byId("user-name")
    password_field = context.locators.byId("password")

    username_field.send_keys(username)
    password_field.send_keys(password)

@when('presiona el botón de login')
def step_click_login_button(context):
    login_button = context.locators.byId("login-button")
    context.locators.clickElement(login_button)

@then('debería ver el mensaje de bienvenida "{expected_text}" en la página de lista de productos')
def step_verify_welcome_message(context, expected_text):
    title = context.locators.byClasses("title")[0].text
    assert title == expected_text, f"Se esperaba '{expected_text}', pero se obtuvo '{title}'"

@when('ingresa un usuario incorrecto y una contraseña incorrecta')
def step_enter_invalid_credentials(context):
    username_field = context.locators.byId("user-name")
    password_field = context.locators.byId("password")

    username_field.send_keys("usuario_incorrecto")
    password_field.send_keys("clave_incorrecta")

@then('debería ver el mensaje de error "{expected_error}"')
def step_verify_error_message(context, expected_error):
    error_message = context.locators.byClasses("error-message-container")[0].text
    assert expected_error in error_message, f"Se esperaba '{expected_error}', pero se obtuvo '{error_message}'"
