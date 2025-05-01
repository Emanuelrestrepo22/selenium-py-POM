# tests/e2e/form_checkout/test_fillForm_happy_path.py

import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.product_list_page import ProductListPage
from tests.pages.cart_page import CartPage
from tests.pages.fill_form_checkout_page import FillFormCheckout


class TestFillFormCheckoutHappyPath:

    @pytest.mark.usefixtures("loginSuccessful")
    def test_fill_form_successfully_redirects_to_checkout_step_two(self, loginSuccessful):
        web, get = loginSuccessful
        fake = Faker()

        # Paso 1: Agregar productos al carrito
        plp = ProductListPage(web, get)
        plp.go_to_product_list()
        added = plp.add_n_products_to_cart(3)
        assert added, "No se agregaron productos al carrito."

        # Paso 2: Ir al carrito y hacer clic en Checkout
        plp.open_cart()
        cart_page = CartPage(web, get)
        cart_page.go_to_checkout()

        # Paso 3: Verificar que estamos en la página del formulario de checkout
        assert "checkout-step-one" in web.current_url, f"No estamos en la página de Checkout Form: {web.current_url}"

        # Paso 4: Llenar todos los campos correctamente
        form = FillFormCheckout(web, get)
        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="firstName"]'))
        )

        get.byDataTest(form.first_name_input).send_keys(fake.first_name())
        get.byDataTest(form.last_name_input).send_keys(fake.last_name())
        get.byDataTest(form.postal_code_input).send_keys(fake.postcode())
        get.byDataTest(form.continue_button).click()

        # Paso 5: Verificar que se redirige a /checkout-step-two.html
        WebDriverWait(web, 10).until(EC.url_contains("checkout-step-two"))
        assert "checkout-step-two" in web.current_url, "No se redirigió al siguiente paso del checkout."
