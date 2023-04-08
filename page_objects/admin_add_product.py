import allure
from locators import AdminSelectors
from .base_page import BasePage


class AddNewProduct(BasePage):
    def fill_general(self, test_product: dict):
        with allure.step("Filling with test data general tab fields"):
            pass
        self._input(AdminSelectors.AddProduct.General.product_name,
                    test_product["oc_product_description"]["name"])
        self._input(AdminSelectors.AddProduct.General.product_meta,
                    test_product["oc_product_description"]["meta_title"])
        return AddNewProduct(self.driver)

    def fill_data(self, test_product: dict):
        with allure.step('Filling with test data "data" tab fields'):
            pass
        self._click(AdminSelectors.AddProduct.Data.data_tab)
        self._input(AdminSelectors.AddProduct.Data.model, test_product["oc_product"]["model"])
        return AddNewProduct(self.driver)

    def fill_seo(self, test_product: dict):
        with allure.step('Filling with test data "seo" tab fields'):
            pass
        self._click(AdminSelectors.AddProduct.SEO.seo_tab)
        self._input(AdminSelectors.AddProduct.SEO.default, test_product["oc_seo_url"]["keyword"])
        return AddNewProduct(self.driver)

    def admin_save_new_item(self):
        with allure.step('Clicking on "save new item" button'):
            pass
        self._click(AdminSelectors.AddProduct.save_btn)
        return AddNewProduct(self.driver)
