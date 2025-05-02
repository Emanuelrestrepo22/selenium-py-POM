import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("cart_with_local_storage")
def test_cart_items_count(cart_with_local_storage):
    """
    Valida que al inyectar datos en localStorage, el carrito muestre
    la cantidad correcta de productos al abrir la página de cart.html.
    """
    web, get, product_ids = cart_with_local_storage

    web.get("https://www.saucedemo.com/cart.html")

    # Encontrar todos los productos visibles en el carrito
    items = web.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')

    # Assert 1: Validar que la cantidad coincide con lo cargado
    assert len(items) == len(product_ids), (
        f"Se esperaban {len(product_ids)} productos en el carrito, pero se encontraron {len(items)}."
    )

    # Assert 2: Validar que cada producto tenga precio visible
    for idx, item in enumerate(items, start=1):
        price_elements = item.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
        assert price_elements, f"El producto #{idx} no tiene precio visible."
        price_text = price_elements[0].text.strip()
        assert price_text.startswith("$"), f"El producto #{idx} tiene un precio inválido: {price_text}"

    # Assert 3: Validar que el botón 'Checkout' esté disponible
    checkout_buttons = web.find_elements(By.CSS_SELECTOR, '[data-test="checkout"]')
    assert checkout_buttons, "El botón 'Checkout' no está presente en la página del carrito."
    assert checkout_buttons[0].is_enabled(), "El botón 'Checkout' no está habilitado."