import allure
from locators import AdminSelectors
from opencart_urls import Urls
from .BasePage import BasePage


class AdminPage(BasePage):
    """Describing administration page in PageObject style"""

    def open(self):
        self.driver.get(Urls.administration)
        with allure.step(f"Open page {Urls.administration}"):
            assert self.driver.current_url == Urls.administration, \
                f"Current url is not {Urls.administration}"
        return AdminPage(self.driver)

    def login(self):
        with allure.step("Login Admininistration page"):
            pass
        self._input(AdminSelectors.Login.user, 'user')
        self._input(AdminSelectors.Login.password, 'bitnami')
        self._click(AdminSelectors.Login.submit_btn)
        return AdminPage(self.driver)

    def nav_to_products(self):
        with allure.step("Navigate to products page"):
            pass
        self._click(AdminSelectors.Menu.Catalog.catalog)
        self._click(AdminSelectors.Menu.Catalog.products)
        return AdminPage(self.driver)

    def press_add_new_product_btn(self):
        with allure.step('Clicking on "add new button"'):
            pass
        self._click(AdminSelectors.Menu.Catalog.add_new_btn)
        return AdminPage(self.driver)

    def filter_product(self, name=''):
        with allure.step(f'Trying to filter {name}'):
            pass
        self._input(AdminSelectors.Filter.product_name, name)
        self._click(AdminSelectors.Filter.button_filter)
        self._wait_for_presence(AdminSelectors.Filter.filtered_products)
        return AdminPage(self.driver)

    def get_filtered_products_list(self):
        with allure.step('Getting filtered products names'):
            pass
        raw_list = self.driver.find_elements(*AdminSelectors.Filter.filtered_products)
        return [x.text[:-8] for x in raw_list if x.text.endswith("\nEnabled")]

    def select_first_filtered_checkbox(self):
        with allure.step('selecting filtered_checkbox'):
            pass
        self._wait_for_presence(AdminSelectors.Filter.filtered_checkbox)
        self._click(AdminSelectors.Filter.filtered_checkbox, 1)

    def del_selected_products(self):
        with allure.step("Deleting selected products"):
            pass
        self._wait_for_presence(AdminSelectors.AddProduct.del_btn)
        self._click(AdminSelectors.AddProduct.del_btn)
        self.driver.switch_to.alert.accept()

    def get_alert_text(self):
        with allure.step('Getting alert text'):
            pass
        return self._get_element_text(AdminSelectors.AddProduct.alert)
