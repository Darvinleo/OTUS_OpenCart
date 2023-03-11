import pytest
import allure
from page_objects import AdminPage


@pytest.mark.regress
@pytest.mark.product
@allure.feature("Admin Page")
@allure.story("Delete product")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_product(driver, add_product_to_db, product_in_db):
    product_name = add_product_to_db
    AdminPage(driver).open()
    AdminPage(driver).login()
    AdminPage(driver).nav_to_products()
    AdminPage(driver).filter_product(product_name)
    AdminPage(driver).select_first_filtered_checkbox()
    AdminPage(driver).del_selected_products()
    assert AdminPage(driver).get_alert_text() == "Success: You have modified products!"
    assert not product_in_db(product_name), f"Product {product_name} does not exist in db"
