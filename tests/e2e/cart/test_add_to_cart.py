import pytest
from tests.pages.product_list_page import ProductListPage

@pytest.mark.usefixtures("loginSuccessful")
def test_add_to_cart(loginSuccessful):
    """
    Verifica que al hacer clic en 'Add to cart', el contador del carrito se actualiza correctamente.
    """
    web, get = loginSuccessful

    # Paso 2: Navegar a la página de productos
    product_list_page = ProductListPage(web, get)
    product_list_page.go_to_product_list()

    # Paso 3: Esperar que los productos sean visibles antes de interactuar con ellos
    product_list_page.get_product_list()  
    num_products_to_add = min(3, len(product_list_page.get_product_list()))
    
    # Agregar productos al carrito
    product_list_page.add_multiple_products_to_cart(num_products_to_add)

    # Paso 4: Verificar el número de productos en el badge
    cart_count = product_list_page.get_cart_count()
    assert cart_count == num_products_to_add, f"Se esperaban {num_products_to_add} productos en el carrito, pero se encontraron {cart_count}."

    print(f"✅ Se agregaron {num_products_to_add} productos al carrito y el badge muestra {cart_count}.")
