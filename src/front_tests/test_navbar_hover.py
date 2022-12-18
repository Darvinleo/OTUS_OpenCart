from selenium.webdriver.common.action_chains import ActionChains
from src.opencart_urls import OpenCartUrls
from src.locators import MainPage


def test_navbar_hover(browser_handler):
    """Just hover over the naviagation links in NavBar"""
    main_page = OpenCartUrls.main_page
    bro = browser_handler
    bro.get(main_page)
    elems = bro.find_elements(*MainPage.NavBar.nav_links)
    for el in elems:
        ActionChains(bro).move_to_element(el).pause(0.5).perform()
