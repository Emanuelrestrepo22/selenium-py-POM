# tests/e2e/cart/test_fill_form_checkout.py

import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.cart_page import CartPage
from tests.pages.product_list_page import ProductListPage
from tests.pages.fill_form_checkout_page import FillFormCheckout

class TestFillFormCheckout:

    @pytest.mark.usefixtures("cart_with_items")
    def test_should_show_error_when_lastname_is_missing(self, cart_with_items):
        web, get, _ = cart_with_items
        fake = Faker()

        plp = ProductListPage(web, get)
        plp.go_to_product_list()
        plp.add_n_products_to_cart(3)

        cart_page = CartPage(web, get)
        cart_page.open_cart()
        cart_page.go_to_checkout()

        assert "checkout-step-one" in web.current_url, "No estamos en la página de Checkout Form"

        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="lastName"]'))
        )
        get.byDataTest("firstName").send_keys(fake.first_name())
        get.byDataTest("postalCode").send_keys(fake.postcode())
        get.byDataTest("continue").click()

        error_container = get.byCss(".error-message-container.error")
        error_text = error_container.text
        assert "Last Name is required" in error_text, "El mensaje de error no es el esperado."
