# tests/e2e/cart/test_fill_form_checkout.py

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
    def test_should_show_error_when_firstname_is_missing(self, loginSuccessful):
        web, get = loginSuccessful
        fake = Faker()

        plp = ProductListPage(web, get)
        plp.go_to_product_list()
        added = plp.add_n_products_to_cart(3)
        assert added, "No se agregaron productos."

        plp.open_cart()
        cart_page = CartPage(web, get)
        cart_page.go_to_checkout()

        assert "checkout-step-one" in web.current_url, "No estamos en la página de Checkout Form"

        form = FillFormCheckout(web, get)
        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="lastName"]'))
        )

        get.byDataTest(form.last_name_input).send_keys(fake.last_name())
        get.byDataTest(form.postal_code_input).send_keys(fake.postalcode())
        get.byDataTest(form.continue_button).click()

        error_container = get.byCss('.error-message-container')
        assert "error" in error_container.get_attribute("class"), "No se muestra el contenedor de error."

        error_text = error_container.text.strip()
        assert "First Name is required" in error_text, "El mensaje no corresponde al error esperado."
