from behave import when, then  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait


@when('ingresa un usuario incorrecto y una contraseña incorrecta')
def step_enter_invalid_credentials(context):
    context.locators.byId("user-name").send_keys("usuario_incorrecto")
    context.locators.byId("password").send_keys("clave_incorrecta")
    print("→ Ingresando credenciales incorrectas")


@then('debería ver el mensaje de error "Epic sadface: Username and password do not match any user in this service"')
def step_verify_error_message(context):
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    print(f"→ Verificando mensaje de error esperado: {expected_error}")
    WebDriverWait(context.driver, 10).until(
        lambda driver: context.locators.byClasses("error-message-container")
    )
    elements = context.locators.byClasses("error-message-container")
    print(f"[DEBUG] Elementos encontrados con clase 'error-message-container': {len(elements)}")
    error_text = elements[0].text if elements else ""
    print(f"[DEBUG] Texto real del mensaje de error: {error_text}")
    assert expected_error in error_text, f"❌ Se esperaba '{expected_error}', pero se obtuvo '{error_text}'"
    print("✅ Mensaje de error verificado correctamente")
