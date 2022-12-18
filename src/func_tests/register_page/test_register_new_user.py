"""Complex test checking registration of new user"""
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.opencart_urls import OpenCartUrls
from src.locators.register_page import RegisterPage


def test_register_new_user(request, browser_handler, create_new_user):
    """This test will check if we can create new user"""
    new_user = create_new_user  # Take random name from fixture for current test

    def logger():
        """Save test data for new user in csv just in case"""
        with open('../test_data/test_users.csv', 'a', encoding='UTF-8', newline='') as users:
            writer = csv.writer(users)
            writer.writerow(new_user.values())

    # Declare all fields for user registration
    fields = {
        'first_name': RegisterPage.PersonalDetails.first_name,
        'last_name': RegisterPage.PersonalDetails.last_name,
        'email': RegisterPage.PersonalDetails.email,
        'password': RegisterPage.PersonalDetails.password
    }
    merge_data = list(zip(fields.values(), new_user.values()))
    bro = browser_handler
    bro.get(OpenCartUrls.register_page)
    for field, value in merge_data:
        bro.find_element(*field).send_keys(value)
    bro.find_element(*RegisterPage.input_newsletter_no).click()
    # agree with Privacy Policy
    bro.find_element(*RegisterPage.agree).click()
    # Finally Press "Continue Button"
    bro.find_element(*RegisterPage.submit_btn).click()
    WebDriverWait(bro, 2).until(ec.title_is("Your Account Has Been Created!"))
    request.addfinalizer(logger)
    assert bro.title == "Your Account Has Been Created!"
