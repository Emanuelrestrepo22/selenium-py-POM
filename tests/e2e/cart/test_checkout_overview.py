import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("overview_ready")
def test_overview_ready_fixture(overview_ready):
    """
    Test simple para validar que la fixture overview_ready funciona correctamente.
    Solo imprime información y verifica que estamos en checkout-step-two.html.
    """
    web, get, added_products = overview_ready

    print(f"\n[TEST] Productos añadidos al carrito: {added_products}")
    print(f"[TEST] URL actual: {web.current_url}")

    # Esperar explícitamente para reforzar la validación
    WebDriverWait(web, 10).until(EC.url_contains("checkout-step-two"))
    assert "checkout-step-two" in web.current_url, "No estamos en Checkout Overview."

    print("[TEST COMPLETADO] Llegamos correctamente a la página de Checkout Overview.")
