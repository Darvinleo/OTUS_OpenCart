"""
Test for adding a new item in Shopping Cart
Just a first probe, need to reformat for admin
"""

import time
from random import choice
from selenium.webdriver.common.by import By
from src.locators.MainPageSelectors import MainPage
from src.opencart_urls import OpenCartUrls


def test_add_item(browser_handler):
    """Add any item from the main page to shopping cart"""
    bro = browser_handler
    bro.get(OpenCartUrls.main_page)
    rand_promo_product = choice(bro.find_elements(*MainPage.Content.featured))
    product_name = rand_promo_product.find_element(By.CSS_SELECTOR, '.description h4 a').text
    button = rand_promo_product.find_element(By.CSS_SELECTOR, 'button[title="Add to Cart"] i')
    bro.execute_script("arguments[0].scrollIntoView()", button) # Workaround move_to_element
    time.sleep(1)  # Need to refactor into Expected Conditions
    button.click()
    alert = bro.find_element(By.CSS_SELECTOR, '#alert .alert-success')
    print(alert.text)
    assert alert.text == f'Success: You have added {product_name} to your shopping cart!'
