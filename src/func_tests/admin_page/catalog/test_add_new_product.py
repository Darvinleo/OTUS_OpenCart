from src.opencart_urls import OpenCartUrls
from src.locators import admin_page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAdminProducts:

    def test_add_new_item(self, administration_login):
        """Checking that we can add new product wia admin_page"""
        link = "http://localhost/administration/index.php?route=catalog/product"
        bro, token = administration_login
        bro.get(link+token)
        bro.find_element(*admin_page.Menu.Catalog.add_new_btn).click()
        product_name = 'Test Product'
        product_meta = 'Test product meta'
        bro.find_element(*admin_page.AddProduct.General.product_name).send_keys(product_name)
        bro.find_element(*admin_page.AddProduct.General.product_meta).send_keys(product_meta)
        bro.find_element(*admin_page.AddProduct.Data.data_tab).click()
        bro.find_element(*admin_page.AddProduct.Data.model).send_keys('Test Model')
        bro.find_element(*admin_page.AddProduct.SEO.seo_tab).click()
        bro.find_element(*admin_page.AddProduct.SEO.default).send_keys('Default')
        bro.find_element(*admin_page.AddProduct.save_btn).click()
        bro.get(link+token)
        bro.find_element(*admin_page.Filter.button_filter).click()
        WebDriverWait(bro, 5).until(EC.presence_of_element_located(admin_page.Filter.product_list))
        filtered_products = [x.text[:-8] for x in bro.find_elements(*admin_page.Filter.filtered_names) if
                             x.text.endswith("\nEnabled")]
        assert product_name in filtered_products
