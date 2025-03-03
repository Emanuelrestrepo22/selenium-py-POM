# tests/steps/cart_steps.py

from behave import given, when, then
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from tests.pages.login_page import LoginPage
from tests.pages.product_list_page import ProductListPage
from tests.utils.asserts import Expect

# Cargar variables de entorno
load_dotenv()

@given('que el usuario ha iniciado sesión y está en la página de lista de productos')
def step_user_on_product_list(context):
    """
    Paso que asegura que el usuario ha iniciado sesión y está en la página de lista de productos.
    """
    # Obtener credenciales y URL desde el archivo .env
    login_url = os.getenv("LOGIN_URL", "").strip()
    username = os.getenv("SWL_USERNAME", "").strip()
    password = os.getenv("SWL_PASSWORD", "").strip()

    # Validar que las variables de entorno estén configuradas
    if not login_url or not username or not password:
        raise ValueError("Las credenciales o la URL de inicio de sesión no están configuradas correctamente en el archivo .env")

    # Instanciar la página de inicio de sesión y realizar el proceso de login
    context.login_page = LoginPage(context.driver, context.locators)
    context.driver.get(login_url)
    context.login_page.enterUsername(username)
    context.login_page.enterPassword(password)
    context.login_page.submitLogin()

    # Verificar que el usuario ha sido redirigido a la página de productos
    expect = Expect(context.driver.current_url)
    expect.toContain("/inventory")

    # Instanciar la página de lista de productos
    context.product_list_page = ProductListPage(context.driver, context.locators)

@given('que el usuario ha añadido {num_products} productos al carrito')
def step_user_added_products_to_cart(context, num_products):
    """
    Paso que añade una cantidad específica de productos al carrito.
    """
    num_products = int(num_products)
    products = context.product_list_page.get_product_list()

    # Verificar que hay suficientes productos disponibles
    if len(products) < num_products:
        raise ValueError(f"No hay suficientes productos disponibles. Se esperaban {num_products}, pero se encontraron {len(products)}.")

    # Añadir los productos al carrito
    context.added_products = []
    for i in range(num_products):
        product_name = context.product_list_page.get_product_name(products[i])
        context.product_list_page.add_product_to_cart(product_name)
        context.added_products.append(product_name)

    # Verificar que el número de productos en el carrito es el esperado
    cart_count = context.product_list_page.get_cart_count()
    expect = Expect(cart_count)
    expect.toBeEqual(num_products)
    print(f"Se han añadido {cart_count} productos al carrito.")

@when('el usuario remueve {num_products} productos del carrito')
def step_remove_products_from_cart(context, num_products):
    """
    Paso que remueve una cantidad específica de productos del carrito.
    """
    num_products = int(num_products)
    removed_count = 0

    # Intentar remover la cantidad especificada de productos
    for _ in range(num_products):
        removed = context.product_list_page.remove_first_product_from_cart()
        if removed:
            removed_count += 1
        else:
            print("No hay más productos para remover.")
            break

    # Verificar que se han removido la cantidad correcta de productos
    if removed_count < num_products:
        raise ValueError(f"Se intentaron remover {num_products} productos, pero solo se pudieron remover {removed_count}.")

@then('debería ver el número {expected_count} en el icono del carrito')
def step_verify_cart_count(context, expected_count):
    """
    Paso que verifica que el icono del carrito muestra la cantidad correcta de productos.
    """
    expected_count = int(expected_count)
    cart_count = context.product_list_page.get_cart_count()
    expect = Expect(cart_count)
    expect.toBeEqual(expected_count)
    print(f"El icono del carrito muestra {cart_count} productos.")
