"""Just for learning, delete before push"""
from selenium.webdriver.common.action_chains import ActionChains
from src.locators import MainPage


def test_registration_page(opencart_ip, browser_handler):
    """Just move to test_registration wia TopNav"""
    bro = browser_handler
    bro.get(opencart_ip)
    admin_links = bro.find_elements(*MainPage.TopNav.admin_links)
    my_acc = admin_links[1]
    ActionChains(bro).move_to_element(my_acc).click().pause(1).perform()

    reg_btn = my_acc.find_element(*MainPage.TopNav.register_btn)
    ActionChains(bro).move_to_element(reg_btn).click().pause(1).perform()
    assert bro.title == "Register Account"
