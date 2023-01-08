from opencart_urls import Urls
from locators import MainPageSelectors, RegPageSelectors
from .BasePage import BasePage


class MainPage(BasePage):
    """Describing MainPage in PageObject"""

    def open(self):
        self.driver.get(Urls.main)
        return MainPage(self.driver)

    def visit_login(self):
        self._click(MainPageSelectors.TopNav.admin_links, 1)  # Click to My Account
        self._click(MainPageSelectors.TopNav.login_btn)
        pass

    def visit_sign_up(self):
        self._click(MainPageSelectors.TopNav.admin_links, 1)
        self._click(MainPageSelectors.TopNav.register_btn)

    def sign_up(self, data: dict):
        self._input(RegPageSelectors.PersonalDetails.first_name, data['first_name'])
        self._input(RegPageSelectors.PersonalDetails.last_name, data['last_name'])
        self._input(RegPageSelectors.PersonalDetails.email, data['email'])
        self._input(RegPageSelectors.PersonalDetails.password, data['password'])
        self._click(RegPageSelectors.input_newsletter_yes)
        self._click(RegPageSelectors.agree)
        self._click(RegPageSelectors.submit_btn)

    def wait_success_sign_up_page(self):
        self._wait_for_presence(RegPageSelectors.common_success)

    def get_alert_text(self):
        return self._get_element_text(MainPageSelectors.alert)
