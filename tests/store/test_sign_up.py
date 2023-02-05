import allure

from helpers import data_logger, user_data_creator
from page_objects import MainPage


@allure.feature("Login and Signing up")
@allure.story("Sign up new user")
@allure.severity(allure.severity_level.CRITICAL)
def test_sign_up(driver):
    """This test will check if we can create new user"""
    new_user = user_data_creator()  # Take random name from fixture for current test
    MainPage(driver) \
        .open() \
        .visit_sign_up()
    MainPage(driver).sign_up(new_user)
    MainPage(driver).wait_success_sign_up_page()
    assert driver.title == "Your Account Has Been Created!"
    data_logger(new_user, 'users')
