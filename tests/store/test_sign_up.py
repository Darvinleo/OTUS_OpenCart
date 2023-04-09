import allure
import pytest
from page_objects import MainPage


@pytest.mark.smoke
@pytest.mark.regress
@allure.feature("Signing up")
class TestSignUP:
    @allure.story("Sign up new user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up(self, driver, test_user, check_user_in_db, del_user_from_db):
        new_user = test_user()
        MainPage(driver).open()
        MainPage(driver).visit_sign_up()
        MainPage(driver).sign_up(new_user)
        MainPage(driver).wait_success_sign_up_page()
        check_user_in_db(email=new_user['email'])
        del_user_from_db(email=new_user['email'])
        assert driver.title == "Your Account Has Been Created!"

    @allure.story("Sign up already existing user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up_existing_user(self, driver, add_user_in_db):
        user = add_user_in_db[0]
        MainPage(driver).open()
        MainPage(driver).visit_sign_up()
        MainPage(driver).sign_up(user)
        assert MainPage(driver).get_alert_text() == "Warning: E-Mail Address is already registered!"
