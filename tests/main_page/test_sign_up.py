from helpers import data_logger, user_data_creator, get_existing_user
from page_objects import MainPage


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

def test_sign_up_existing_user(driver):
    """Check that we cannot create user with the same email"""
    existing_user = get_existing_user()
    MainPage(driver) \
        .open() \
        .visit_sign_up()
    MainPage(driver).sign_up(existing_user)
    assert MainPage(driver).get_alert_text() == "Warning: E-Mail Address is already registered!"