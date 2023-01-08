import pytest
from opencart_urls import Urls
from locators import AdminSelectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

user = "user"
password = "bitnami"


@pytest.fixture(scope='session')
def administration_login(browser_handler):
    """Fixture will log in administration page of OpenCart and return browser and user_token"""
    bro = browser_handler
    bro.get(Urls.administration)
    bro.find_element(*AdminSelectors.Login.user).send_keys(user)
    bro.find_element(*AdminSelectors.Login.password).send_keys(password)
    bro.find_element(*AdminSelectors.Login.submit_btn).click()
    WebDriverWait(bro, 3).until(EC.presence_of_element_located(AdminSelectors.Menu.dashboard))
    # token = bro.current_url[bro.current_url.find('user_token')-1:]
    return bro
