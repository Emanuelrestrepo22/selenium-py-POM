import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.locators import Locators

# Cargar variables desde .env
load_dotenv()

class checkoutCartPage:
    """POM to flow to in PCP"""
    
    def __init__(self, driver: WebDriver, locator: Locators):
        self.driver = driver
        self.locator = locator
        
        #URL of PCP
        self.base_url = os.getenv('BASE_URL')
        self.endpoint = '/cart.html'
        self.url = f"{self.base_url}{self.endpoint}"
        
        # Main selectors in PCP (DOM)
        self.cart_container = '[data-test="cart-list"]'
        self.cart_item = '[data-test="inventory-item"]'
        self.price_cart_item = '[data-test="inventory-item-price"]'
        self.remove_button = '[data-test^="remove-sauce-labs"]'
        self.checkout_button = '[data-test="checkout"]'

        
        #main selectors en ckeckout cart 'form'
        self.firstName = '[data-test="firstName"]'
        self.lastName = '[data-test="lastName"]'
        self.postalCode = '[data-test="postalCode"]'
        self.cancelButton = '[data-test="cancel"]'
        self.continueButton = '[data-test="continue"]'
        
        #main selectors checkoutStep
        self.checkoutUrl = 'https://www.saucedemo.com/checkout-step-two.html'
        self.price_add_all_items = '[data-test="subtotal-label"]'
        self.taxes_price = '[data-test="tax-label"]'
        self.totalPrice = '[data-test="total-label"]'
        self.finishButton = '[data-test="finish"]'
        self.titlepageCheckout = '[data-test="title"]'
        
    
