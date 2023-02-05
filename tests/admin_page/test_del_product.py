from page_objects import AdminPage
import allure

test_name = 'Test_Name'


@allure.feature("Admin Page")
@allure.story("Delete existing product")
@allure.severity(allure.severity_level.CRITICAL)
def test_del_product(driver):
    AdminPage(driver) \
        .open() \
        .login() \
        .nav_to_products() \
        .filter_product(test_name) \
        .select_first_filtered_checkbox()
    AdminPage(driver).del_selected_products()
    assert AdminPage(driver).get_alert_text() == "Success: You have modified products!"
