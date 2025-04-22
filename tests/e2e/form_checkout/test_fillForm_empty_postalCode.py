# tests/e2e/form_checkout/test_fillForm_empty_postalCode.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

from tests.pages.fill_form_checkout_page import FillFormCheckout
from tests.pages.cart_page import CartPage
from tests.pages.product_list_page import ProductListPage


class TestFillFormCheckout:

    @pytest.mark.usefixtures("loginSuccessful")
    def test_should_show_error_when_postalcode_is_missing(self, loginSuccessful):
        web, get = loginSuccessful
        fake = Faker()

        print("🟢 Paso 1: Agregando productos desde PLP...")
        plp = ProductListPage(web, get)
        plp.go_to_product_list()
        added = plp.add_n_products_to_cart(3)
        assert added, "❌ No se agregaron productos al carrito."

        print("🛒 Paso 2: Abriendo carrito y navegando a Checkout...")
        plp.open_cart()
        cart_page = CartPage(web, get)
        cart_page.go_to_checkout()

        print("🟢 Paso 3: Verificando URL de página de Checkout Form...")
        current_url = web.current_url
        print(f"🌐 URL actual: {current_url}")
        assert "checkout-step-one" in current_url, "❌ No estamos en el formulario de checkout."

        print("📝 Paso 4: Completando solo First Name y Last Name (sin postal code)...")
        form = FillFormCheckout(web, get)

        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="lastName"]'))
        )

        get.byDataTest(form.first_name_input).send_keys(fake.first_name())
        get.byDataTest(form.last_name_input).send_keys(fake.last_name())
        get.byDataTest(form.continue_button).click()

        print("🚨 Paso 5: Validando mensaje de error por postal code vacío...")
        error_container = get.byCss('.error-message-container')
        assert "error" in error_container.get_attribute("class"), "❌ No se muestra el contenedor de error."

        error_text = error_container.text.strip()
        print(f"🧪 Texto del error: {error_text}")
        assert "Postal Code is required" in error_text, "❌ El mensaje de error no corresponde al esperado."

        print("✅ Test completado correctamente.")
