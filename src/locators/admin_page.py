from selenium.webdriver.common.by import By


class Login:
    user = (By.ID, "input-username")
    password = (By.ID, "input-password")
    submit_btn = (By.CLASS_NAME, "btn-primary")


class Menu:
    dashboard = (By.ID, "menu-dashboard")

    class Catalog:
        add_new_btn = (By.XPATH, "//*[contains(@class, 'float-end')]/a")
        catalog = (By.ID, "menu-catalog")
        categories = (By.XPATH, "// *[@id='menu-catalog']/ul/li/a [contains(text(),'Categories')]")
        products = (By.XPATH, "// *[@id='menu-catalog']/ul/li/a [contains(text(),'Products')]")


class AddProduct:
    save_btn = (By.XPATH, "//*[@id='content'] /div/div/div/button[@type='submit']")

    class General:
        general_tab = (By.XPATH, "//*[@href='#tab-general']")
        product_name = (By.ID, "input-name-1")
        product_meta = (By.ID, "input-meta-title-1")

    class Data:
        data_tab = (By.XPATH, "//*[@href='#tab-data']")
        model = (By.ID, "input-model")

    class SEO:
        seo_tab = (By.XPATH, "//*[@href='#tab-seo']")
        default = (By.CSS_SELECTOR, "#product-seo div div + input")


class Filter:
    product_list = (By.CSS_SELECTOR, "#form-product")
    product_name = (By.CSS_SELECTOR, "input#input-name")
    button_filter = (By.CSS_SELECTOR, "button#button-filter")
    filtered_names = (By.CSS_SELECTOR, "td[class=text-start]")