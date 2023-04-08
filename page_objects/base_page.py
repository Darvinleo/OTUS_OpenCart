import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from locators.main_page_selectors import MainPageSelectors


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: tuple, index: int = 0):
        """return element by chosen search strategy"""
        element = self.driver.find_elements(*selector)
        return f"Can't find element with locator {selector}" if element == [] else element[index]

    def _click(self, selector, index=0):
        self._wait_for_visible(selector, index)
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, index=0, wait=5):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))

    def _wait_for_presence(self, selector):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions) \
            .until(EC.presence_of_element_located(selector))

    def _get_element_text(self, selector, index=0):
        return self.__element(selector, index).text

    def visit_login(self):
        with allure.step('Go to login page'):
            pass
        self._click(MainPageSelectors.TopNav.admin_links, 1)
        self._click(MainPageSelectors.TopNav.login_btn)
        pass

    def visit_sign_up(self):
        with allure.step('Go to "sign up" page'):
            pass
        self._click(MainPageSelectors.TopNav.admin_links, 1)
        self._click(MainPageSelectors.TopNav.register_btn)
