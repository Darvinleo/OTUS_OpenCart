import allure
import pytest
from helpers import data_logger, user_data_creator, get_existing_user
from page_objects import MainPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.feature("Signing up")
class TestSignUP:
    @pytest.mark.dependency()
    @allure.story("Sign up new user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up(self, driver):
        """This test will check if we can create new user"""
        new_user = user_data_creator()  # Take random name from fixture for current test
        MainPage(driver) \
            .open() \
            .visit_sign_up()
        MainPage(driver).sign_up(new_user)
        MainPage(driver).wait_success_sign_up_page()
        assert driver.title == "Your Account Has Been Created!"
        data_logger(new_user, 'users')

    @pytest.mark.dependency(depends=["TestSignUP::test_sign_up"])
    @allure.story("Sign up already existing user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up_existing_user(self, driver):
        """Check that we cannot create user with the same email"""
        existing_user = get_existing_user()
        MainPage(driver) \
            .open() \
            .visit_sign_up()
        MainPage(driver).sign_up(existing_user)
        assert MainPage(driver).get_alert_text() == "Warning: E-Mail Address is already registered!"
