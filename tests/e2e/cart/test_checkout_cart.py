
import pytest
from tests.pages.checkout_cart_page import CheckoutCartPage
from tests.utils.asserts import Expect

@pytest.mark.usefixtures("loginSuccessful", "cart_with_items")
def test_cart_functionality(cart_with_items):
    web, get, added = cart_with_items
    print(added)  # Muestra los productos añadidos al carrito

