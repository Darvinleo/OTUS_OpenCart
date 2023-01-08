from page_objects import AdminPage

# test data
test_name = 'Test_Name'


def test_admin_add_new_product(driver):
    AdminPage(driver) \
        .open() \
        .login() \
        .nav_to_products() \
        .press_add_new_product_btn()
    AdminPage.AddNewProduct(driver) \
        .fill_general_tab_fields() \
        .fill_data_tab_fields() \
        .fill_seo_tab_fields() \
        .admin_save_new_item()
    assert AdminPage.AddNewProduct(driver).get_alert_text() == 'Success: You have modified products!'
    AdminPage(driver) \
        .nav_to_products() \
        .filter_product(test_name)
    # print(AdminPage(driver).get_filtered_products_list())
    assert test_name in AdminPage(driver).get_filtered_products_list()