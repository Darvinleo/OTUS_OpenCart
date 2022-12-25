import pytest
from selenium import webdriver

import opencart_urls
from locators import admin_page as ap


def pytest_addoption(parser):
    parser.addoption('--browser', '-B', action='store', default='chrome', help='Choose Browser')


@pytest.fixture(scope='session')
def browser_handler(request):
    """Start choosen browser and close after work"""
    browser = request.config.getoption('browser')
    match browser:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
        case _:
            raise ValueError(f"Can't open browser with name{browser}, 'chrome' or 'firefox' only available'")
    driver.maximize_window()
    driver.implicitly_wait(4)
    request.addfinalizer(driver.close)
    return driver
