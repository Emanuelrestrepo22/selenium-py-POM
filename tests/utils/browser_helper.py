def set_session_username(driver, username):
    driver.add_cookie({
        'name': 'session-username',
        'value': username,
        'path': '/',
        'domain': 'www.saucedemo.com'
    })


def set_cart_contents(driver, product_ids):
    script = f"localStorage.setItem('cart-contents', JSON.stringify({product_ids}));"
    driver.execute_script(script)


def clear_cart_contents(driver):
    script = "localStorage.setItem('cart-contents', JSON.stringify([]));"
    driver.execute_script(script)
