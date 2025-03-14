# tests/e2e/test_add_to_cart.py

import pytest
from tests.pages.product_list_page import ProductListPage
from tests.utils.asserts import Expect

@pytest.mark.usefixtures("loginSuccessful")
class TestAddToCart:

    def test_add_products_to_cart_and_validate_cart_counter(self, loginSuccessful):
        """
        Verifica que al agregar productos al carrito, el contador se actualiza correctamente.
        """
        web, get = loginSuccessful

        # Instanciamos el objeto de la página ProductListPage
        product_list_page = ProductListPage(web, get)

        # Paso 1: Navegar a la página de productos
        product_list_page.go_to_product_list()

        # Paso 2: Esperar que la lista de productos cargue
        products = product_list_page.get_product_list()
        num_products_to_add = min(3, len(products))  # Agregar máximo 3 productos

        # Paso 3: Agregar productos al carrito y verificar que fueron agregados correctamente
        for product_element in products[:num_products_to_add]:
            product_name = product_list_page.get_product_name(product_element)
            added_successfully = product_list_page.add_product_to_cart(product_name)
            assert added_successfully, f"No se pudo agregar el producto '{product_name}' al carrito."

        # Paso 4: Obtener y validar el contador del carrito
        cart_count = product_list_page.get_cart_count()
        assert int(cart_count) == num_products_to_add, (
            f"Se esperaba {num_products_to_add} productos en el carrito, pero se encontraron {cart_count}"
        )

        print(f" {num_products_to_add} productos añadidos al carrito correctamente. El badge muestra: {cart_count}")

