import allure
from locators import MainPageSelectors, RegPageSelectors
from .base_page import BasePage


class MainPage(BasePage):
    main = "http://localhost/"

    def open(self):
        with allure.step('Opening Main Page'):
            pass
        self.driver.get(self.main)
        return MainPage(self.driver)

    def sign_up(self, user_data: dict):
        with allure.step('Filling new user info on "sign up page"'):
            pass
        self._input(RegPageSelectors.PersonalDetails.first_name, user_data['firstname'])
        self._input(RegPageSelectors.PersonalDetails.last_name, user_data['lastname'])
        self._input(RegPageSelectors.PersonalDetails.email, user_data['email'])
        self._input(RegPageSelectors.PersonalDetails.password, user_data['password'])
        self._click(RegPageSelectors.input_newsletter_yes)
        self._click(RegPageSelectors.agree)
        self._click(RegPageSelectors.submit_btn)

    def wait_success_sign_up_page(self):
        self._wait_for_presence(RegPageSelectors.common_success)

    def get_alert_text(self):
        return self._get_element_text(MainPageSelectors.alert)
