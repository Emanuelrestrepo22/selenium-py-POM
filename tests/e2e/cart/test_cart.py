import pytest
from selenium.webdriver.common.by import By
from tests.pages.product_list_page import ProductListPage
from tests.pages.cart_page import CartPage
from tests.utils.asserts import Expect


@pytest.mark.usefixtures("loginSuccessful")
class TestCartPage:

    def test_cart_state_should_be_consistent_before_checkout(self, loginSuccessful):
        web, get = loginSuccessful

        # Paso 1: Instancia en PLP y agregar productos
        plp = ProductListPage(web, get)
        plp.go_to_product_list()
        added_products = plp.add_n_products_to_cart(5)
        assert len(added_products) == 5, "No se agregaron 5 productos al carrito."

        # Paso 2: Validar número en ícono del carrito
        cart_count_icon = plp.get_cart_count()
        assert cart_count_icon == 5, f"El ícono del carrito muestra {cart_count_icon} en lugar de 5."

        # Paso 3: Redirigir a la página del carrito
        plp.open_cart()
        cartPage = CartPage(web, get)

        # Paso 4: Verificar que el número de productos en el contenedor coincide con el ícono
        items_in_cart_page = len(web.find_elements(By.CSS_SELECTOR, cartPage.cart_item))
        assert items_in_cart_page == cart_count_icon, (
            f"El carrito muestra {items_in_cart_page} productos, pero el ícono indica {cart_count_icon}."
        )

        # Paso 5: Eliminar 2 productos
        for _ in range(2):
            remove_buttons = web.find_elements(By.CSS_SELECTOR, cartPage.remove_button)
            assert remove_buttons, "No hay botones para eliminar productos en el carrito."
            remove_buttons[0].click()

        # Paso 6: Validar que el ícono se actualizó correctamente
        updated_cart_count = plp.get_cart_count()
        expected_remaining = 3
        assert updated_cart_count == expected_remaining, (
            f"Se esperaban {expected_remaining} productos en el ícono, pero se encontró {updated_cart_count}."
        )

        # Paso 7: Validar que el contenedor tenga los mismos productos
        updated_cart_items = len(web.find_elements(By.CSS_SELECTOR, cartPage.cart_item))
        assert updated_cart_items == expected_remaining, (
            f"El contenedor de carrito muestra {updated_cart_items} productos en lugar de {expected_remaining}."
        )

        # Paso 8: Hacer clic en el botón de Checkout
        cartPage.go_to_checkout()

        # Paso 9: Validar que estamos en el formulario de información
        expect = Expect(web.current_url)
        expect.toContain("checkout-step-one")
