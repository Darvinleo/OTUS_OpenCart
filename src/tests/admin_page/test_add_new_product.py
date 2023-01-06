from src.page_objects import AdminPage


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

    AdminPage(driver) \
        .nav_to_products() \
        .filter_product('Test_Name')
    # print(AdminPage(driver).get_filtered_products_list())
    assert 'Test_Name' in AdminPage(driver).get_filtered_products_list()
