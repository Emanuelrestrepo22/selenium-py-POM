from behave import given, when, then # type: ignore
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
from tests.pages.login_page import LoginPage
from tests.pages.product_list_page import ProductListPage
from tests.utils.asserts import Expect

@given('que el usuario ha iniciado sesión y está en la página de lista de productos')
def step_user_on_product_list(context):
    context.login_page = LoginPage(context.driver, context.locators)
    login_url = os.getenv("LOGIN_URL", "").strip()
    username = os.getenv("SWL_USERNAME", "").strip()
    password = os.getenv("SWL_PASSWORD", "").strip()

    context.driver.get(login_url)  # Ir a la página de login
    context.login_page = LoginPage(context.driver, context.locators)  # Instanciar LoginPage
    context.login_page.enterUsername(username)
    context.login_page.enterPassword(password)
    context.login_page.submitLogin()

    # Verificar que el usuario llegó a la página de productos después del login
    expect = Expect(context.driver.current_url)
    expect.toContain("/inventory")
    
    
    if not login_url or not username or not password:
        raise ValueError("Las credenciales o URL no están configuradas correctamente en el archivo .env")


    # Instanciar ProductListPage y navegar a la lista de productos
    context.product_list_page = ProductListPage(context.driver, context.locators)
    context.product_list_page.go_to_product_list()
    context.product_list_page = ProductListPage(context.driver, context.locators)
    context.product_list_page.go_to_product_list()

@when('el usuario añade {num_products} productos al carrito')
def step_add_products_to_cart(context, num_products):
    num_products = int(num_products)
    products = context.product_list_page.get_product_list()
     # 🔹 Asegurar que hay productos disponibles
    if not products or len(products) < num_products:
        raise ValueError(f"No hay suficientes productos disponibles. Se esperaban {num_products}, pero se encontraron {len(products)}.")
    context.added_products = []  # Almacenar productos agregados

    for i in range(num_products):
        product_name = context.product_list_page.get_product_name(products[i])
        context.product_list_page.add_product_to_cart(product_name)
        context.added_products.append(product_name)  # Guardar producto agregado

@then('debería ver el número {expected_count} en el icono del carrito')
def step_verify_cart_count(context, expected_count):
    cart_count = context.product_list_page.get_cart_count()
    expect = Expect(cart_count)
    expect.toBeEqual(int(expected_count))

@when('el usuario remueve {num_removed} productos del carrito')
def step_remove_products_from_cart(context, num_removed):
    num_removed = int(num_removed)

    for i in range(num_removed):
        if context.added_products:
            product_name = context.added_products.pop()  # Remover de la lista
            context.product_list_page.remove_product_from_cart(product_name)
