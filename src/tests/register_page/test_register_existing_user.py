from src.opencart_urls import OpenCartUrls
from src.locators import RegisterPage


def test_register_existing_user(browser_handler):
    """Check that we cannot create user with the same email"""
    register_page = OpenCartUrls.register_page
    bro = browser_handler
    bro.get(register_page)
    # finding first_name field by css and filling with test name
    bro.find_element(*RegisterPage.PersonalDetails.first_name).send_keys("Test_First_Name")
    # finding last_name field by css and filling with test last name
    bro.find_element(*RegisterPage.PersonalDetails.last_name).send_keys("Test_Lat_Name")
    # finding email field and filling with test_email
    bro.find_element(*RegisterPage.PersonalDetails.email).send_keys("test_email@mail.com")
    # finding password field and filling with test_password
    bro.find_element(*RegisterPage.PersonalDetails.password).send_keys("123456")
    # finding Newsletter checkbox and select "No" option
    bro.find_element(*RegisterPage.input_newsletter_no).click()
    # agree with Privacy Policy
    bro.find_element(*RegisterPage.agree).click()
    # Finally Press "Continue Button"
    bro.find_element(*RegisterPage.submit_btn).click()
    assert bro.find_element(*RegisterPage.alert).text == "Warning: E-Mail Address is already registered!"
