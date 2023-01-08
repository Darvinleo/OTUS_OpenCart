from locators import AdminSelectors
from opencart_urls import Urls
from .BasePage import BasePage


class AdminPage(BasePage):
    """Describing administration page in PageObject style"""
    def open(self):
        self.driver.get(Urls.administration)
        return AdminPage(self.driver)

    def login(self):
        self._input(AdminSelectors.Login.user, 'user')
        self._input(AdminSelectors.Login.password, 'bitnami')
        self._click(AdminSelectors.Login.submit_btn)
        return AdminPage(self.driver)

    def nav_to_products(self):
        self._click(AdminSelectors.Menu.Catalog.catalog)
        self._click(AdminSelectors.Menu.Catalog.products)
        return AdminPage(self.driver)

    def press_add_new_product_btn(self):
        self._click(AdminSelectors.Menu.Catalog.add_new_btn)
        return AdminPage(self.driver)

    def filter_product(self, name='', model='', price='', quantity: int = 0, status=''):
        self._input(AdminSelectors.Filter.product_name, name)
        self._click(AdminSelectors.Filter.button_filter)
        return AdminPage(self.driver)

    def get_filtered_products_list(self):
        self._wait_for_presence(AdminSelectors.Filter.filtered_products)
        raw_list = self.driver.find_elements(*AdminSelectors.Filter.filtered_products)
        return [x.text[:-8] for x in raw_list if x.text.endswith("\nEnabled")]

    class AddNewProduct(BasePage):

        def fill_general_tab_fields(self):
            self._input(AdminSelectors.AddProduct.General.product_name, 'Test_Name')  # need test data
            self._input(AdminSelectors.AddProduct.General.product_meta, 'Test_Meta')  # need test data
            return AdminPage.AddNewProduct(self.driver)

        def fill_data_tab_fields(self):
            self._click(AdminSelectors.AddProduct.Data.data_tab)
            self._input(AdminSelectors.AddProduct.Data.model, 'Model')  # need test data
            return AdminPage.AddNewProduct(self.driver)

        def fill_seo_tab_fields(self):
            self._click(AdminSelectors.AddProduct.SEO.seo_tab)
            self._input(AdminSelectors.AddProduct.SEO.default, 'Unique_value')  # need test data
            return AdminPage.AddNewProduct(self.driver)

        def admin_save_new_item(self):
            self._click(AdminSelectors.AddProduct.save_btn)
            return AdminPage.AddNewProduct(self.driver)

        def get_alert_text(self):
            return self._get_element_text(AdminSelectors.AddProduct.alert)
