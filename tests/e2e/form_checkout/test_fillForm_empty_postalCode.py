# tests/e2e/form_checkout/test_fillForm_empty_postalCode.py

import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.product_list_page import ProductListPage
from tests.pages.cart_page import CartPage
from tests.pages.fill_form_checkout_page import FillFormCheckout


class TestFillFormCheckout:

    @pytest.mark.usefixtures("loginSuccessful")
    def test_should_show_error_when_postalcode_is_missing(self, loginSuccessful):
        web, get = loginSuccessful
        fake = Faker()

        # Paso 1: Agregar productos desde PLP
        plp = ProductListPage(web, get)
        plp.go_to_product_list()
        added = plp.add_n_products_to_cart(3)
        assert len(added) == 3, "No se agregaron los productos esperados al carrito."

        # Paso 2: Ir al carrito y continuar a checkout
        plp.open_cart()
        cart_page = CartPage(web, get)
        cart_page.go_to_checkout()

        # Paso 3: Validar URL de checkout form
        assert "checkout-step-one" in web.current_url, "No se redirigió al formulario de checkout."

        # Paso 4: Completar solo nombre y apellido
        form = FillFormCheckout(web, get)
        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="lastName"]'))
        )

        get.byDataTest(form.first_name_input).send_keys(fake.first_name())
        get.byDataTest(form.last_name_input).send_keys(fake.last_name())
        get.byDataTest(form.continue_button).click()

        # Paso 5: Validar presencia de mensaje de error
        error_container = get.byCss('.error-message-container')
        assert "error" in error_container.get_attribute("class"), "No se mostró el contenedor de error."

        error_text = error_container.text.strip()
        assert error_text == "Error: Postal Code is required", f"Mensaje inesperado: {error_text}"
