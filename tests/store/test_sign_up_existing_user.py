from helpers import get_existing_user
from page_objects import MainPage
import allure

@allure.feature("Login and Signing up")
@allure.story("Sign up already existing user")
@allure.severity(allure.severity_level.CRITICAL)
def test_sign_up_existing_user(driver):
    """Check that we cannot create user with the same email"""
    existing_user = get_existing_user()
    MainPage(driver) \
        .open() \
        .visit_sign_up()
    MainPage(driver).sign_up(existing_user)
    assert MainPage(driver).get_alert_text() == "Warning: E-Mail Address is already registered!"
