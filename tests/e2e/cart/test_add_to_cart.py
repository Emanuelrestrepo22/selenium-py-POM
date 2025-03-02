# tests/e2e/test_add_to_cart.py

import pytest
from tests.pages.product_list_page import ProductListPage
from tests.utils.asserts import Expect

@pytest.mark.usefixtures("loginSuccessful")
def test_add_to_cart(loginSuccessful):
    """
    Verifica que al hacer clic en 'Add to cart', el contador del carrito se actualiza correctamente.
    """
    web, get = loginSuccessful

    # Paso 2: Navegar a la página de productos
    product_list_page = ProductListPage(web, get)
    product_list_page.go_to_product_list()

    # Paso 3: Seleccionar productos y hacer clic en "Add to cart"
    products = product_list_page.get_product_list()
    num_products_to_add = min(3, len(products))  # Agregar hasta 3 productos si hay suficientes

    for i in range(num_products_to_add):
        product_name = product_list_page.get_product_name(products[i])
        assert product_list_page.add_product_to_cart(product_name), f"El producto {product_name} no se pudo agregar al carrito."

    # Paso 4: Verificar el número de productos en el badge
    cart_count = product_list_page.get_cart_count()
    expect = Expect(cart_count)
    expect.toBeEqual(num_products_to_add)

    print(f"Se agregaron {num_products_to_add} productos al carrito y el badge muestra {cart_count}")
