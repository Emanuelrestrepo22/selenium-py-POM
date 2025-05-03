from behave import when, then  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait


@when('ingresa su usuario desde el archivo .env')
def step_enter_valid_credentials(context):
    import os
    username = os.getenv("SWL_USERNAME")
    password = os.getenv("SWL_PASSWORD")
    context.locators.byId("user-name").send_keys(username)
    context.locators.byId("password").send_keys(password)
    print(f"→ Ingresando usuario válido: {username}")


@then('debería ver el mensaje de bienvenida "Products" en la página de lista de productos')
def step_verify_welcome_message(context):
    print("→ Verificando mensaje esperado: Products")
    WebDriverWait(context.driver, 10).until(
        lambda driver: context.locators.byClasses("title")
    )
    title = context.locators.byClasses("title")[0].text
    assert title == "Products", f"❌ Se esperaba 'Products', pero se obtuvo '{title}'"
    print("✅ Mensaje de bienvenida verificado correctamente")
