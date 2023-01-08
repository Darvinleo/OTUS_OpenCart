from .common_selectors import *


class AdminSelectors:
    class Login:
        user = (el_id, "input-username")
        password = (el_id, "input-password")
        submit_btn = (class_name, "btn-primary")

    class Menu:
        dashboard = (el_id, "menu-dashboard")

        class Catalog:
            add_new_btn = (css, "a.btn[title='Add New']")
            catalog = (el_id, "menu-catalog")
            categories = (xpath, "//*[@id='collapse-1']/li/a[contains(text(), 'Categories')]")
            products = (xpath, "//*[@id='collapse-1']/li/a[contains(text(), 'Products')]")

    class AddProduct:
        save_btn = (xpath, "//*[@id='content'] /div/div/div/button[@type='submit']")
        del_btn = (class_name, "btn-danger")
        alert = (css, "div.alert-dismissible")

        class General:
            general_tab = (xpath, "//*[@href='#tab-general']")
            product_name = (el_id, "input-name-1")
            product_meta = (el_id, "input-meta-title-1")

        class Data:
            data_tab = (xpath, "//*[@href='#tab-data']")
            model = (el_id, "input-model")

        class SEO:
            seo_tab = (xpath, "//*[@href='#tab-seo']")
            default = (css, "#product-seo div div + input")

    class Filter:
        product_list = (css, "#form-product")
        product_name = (css, "input#input-name")
        button_filter = (css, "button#button-filter")
        filtered_products = (css, "tbody td[class=text-start]")
        filtered_checkbox = (css, "input.form-check-input")
