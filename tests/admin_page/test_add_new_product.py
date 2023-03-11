import pytest
import allure
from page_objects import AdminPage, AddNewProduct


@pytest.mark.regress
@pytest.mark.product
@allure.feature("Admin Page")
@allure.story("Add new product")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_add_new_product(driver, test_product, validate_in_db):
    AdminPage(driver) \
        .open() \
        .login() \
        .nav_to_products() \
        .press_add_new_product_btn()
    AddNewProduct(driver) \
        .fill_general(test_product) \
        .fill_data(test_product) \
        .fill_seo(test_product) \
        .admin_save_new_item()
    assert AdminPage(driver).get_alert_text() == 'Success: You have modified products!'
    validate_in_db(test_product["oc_product_description"]["name"])
