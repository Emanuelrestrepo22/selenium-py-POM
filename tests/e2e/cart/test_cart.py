import pytest
from selenium.webdriver.common.by import By
from tests.pages.product_list_page import ProductListPage
from tests.pages.cart_page import CartPage
from tests.utils.asserts import Expect

@pytest.mark.usefixtures("loginSuccessful")
class TestCartPage:

    def test_should_match_cart_count_after_adding_and_removing_items(self, loginSuccessful):
        web, get = loginSuccessful

        print("🟢 Paso 1: Cargando página de productos...")
        plp = ProductListPage(web, get)
        plp.go_to_product_list()

        print("🟢 Agregando 5 productos al carrito...")
        added_products = plp.add_n_products_to_cart(5)
        print(f"🧾 Productos agregados: {added_products}")
        assert len(added_products) == 5, "No se agregaron 5 productos al carrito."

        print("🟢 Verificando número en el ícono del carrito...")
        cart_count_icon = plp.get_cart_count()
        print(f"🛒 Número en ícono del carrito: {cart_count_icon}")

        print("🟢 Haciendo clic en el ícono del carrito...")
        plp.open_cart()
        cartPage = CartPage(web, get)

        print("🟢 Verificando número de productos dentro del carrito...")
        items_in_cart_page = len(web.find_elements(By.CSS_SELECTOR, cartPage.cart_item))
        print(f"📦 Productos visibles en cart-list: {items_in_cart_page}")

        assert items_in_cart_page == cart_count_icon, (
            f"El carrito muestra {items_in_cart_page} items, pero el ícono dice {cart_count_icon}."
        )

        print("🟢 Eliminando 2 productos del carrito...")
        removed = 0
        for i in range(2):
            try:
                remove_buttons = web.find_elements(By.CSS_SELECTOR, cartPage.remove_button)
                if remove_buttons:
                    remove_buttons[0].click()
                    removed += 1
                    print(f"✅ Producto eliminado ({removed}/2)")
            except Exception as e:
                print(f"⚠️ Error al eliminar producto: {e}")

        assert removed == 2, f"Solo se eliminaron {removed} productos."

        print("🟢 Verificando ícono del carrito después de eliminar...")
        updated_cart_count = plp.get_cart_count()
        updated_cart_items = len(web.find_elements(By.CSS_SELECTOR, cartPage.cart_item))
        print(f"🛒 Ícono del carrito: {updated_cart_count}")
        print(f"📦 Productos en página: {updated_cart_items}")

        assert updated_cart_count == updated_cart_items, (
            f"Ícono muestra {updated_cart_count}, pero el carrito contiene {updated_cart_items} productos."
        )

        print("✅✅ Test completado exitosamente.")
