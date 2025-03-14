# tests/e2e/test_add_to_cart.py

import pytest
from tests.pages.product_list_page import ProductListPage
from tests.utils.asserts import Expect

@pytest.mark.usefixtures("loginSuccessful")
class TestAddToCart:

    def test_add_products_to_cart_and_validate_cart_counter(self, loginSuccessful):
        """
        Verifica que al agregar 5 productos al carrito, el contador se actualiza correctamente.
        """
        web, get = loginSuccessful

        # Paso 1: Navegar a la página de productos
        product_list_page = ProductListPage(web, get)
        product_list_page.go_to_product_list()

        # Paso 2: Agregar hasta 5 productos al carrito
        products = product_list_page.get_product_list()
        num_products_to_add = min(5, len(products))

        for product_element in products[:num_products_to_add]:
            product_name = product_list_page.get_product_name(product_element)
            assert product_list_page.add_product_to_cart(product_name), (
                f"Fallo al agregar '{product_name}' al carrito."
            )

        # Paso 3: Obtener y validar el contador del carrito
        cart_count = product_list_page.get_cart_count()
        Expect(cart_count).toBeEqual(num_products_to_add)

        print(f" {num_products_to_add} productos añadidos correctamente. El carrito muestra: {cart_count}")

    def test_remove_products_from_cart_and_validate_cart_counter(self, loginSuccessful):
        """
        Verifica que al remover un producto del carrito, el contador se actualiza correctamente.
        """
        web, get = loginSuccessful

        # Paso 1: Navegar a la página de productos
        product_list_page = ProductListPage(web, get)
        product_list_page.go_to_product_list()

        # Paso 2: Agregar 5 productos al carrito primero
        products = product_list_page.get_product_list()
        num_products_to_add = min(5, len(products))

        for product_element in products[:num_products_to_add]:
            product_name = product_list_page.get_product_name(product_element)
            product_list_page.add_product_to_cart(product_name)

        # Paso 3: Remover el primer producto del carrito
        assert product_list_page.remove_first_product_from_cart(), (
            "No se pudo remover ningún producto del carrito."
        )

        # Paso 3: Verificar que el carrito ahora tenga 4 productos (ya que se removió 1)
        cart_count = product_list_page.get_cart_count()
        expected_count_after_remove = num_products_to_add - 1

        expect = Expect(cart_count)
        expect.toBeEqual(expected_count_after_remove)

        print(f" Se removió 1 producto, quedando {cart_count} en el badge del carrito.")
        
if __name__ == "__main__":
    pytest.main()

