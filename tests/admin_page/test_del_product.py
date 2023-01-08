from page_objects import AdminPage

test_name = 'Test_Name'


def test_del_product(driver):
    AdminPage(driver) \
        .open() \
        .login() \
        .nav_to_products() \
        .filter_product(test_name) \
        .select_first_filtered_checkbox()
    AdminPage(driver).del_selected_products()
    assert AdminPage(driver).get_alert_text() == "Success: You have modified products!"