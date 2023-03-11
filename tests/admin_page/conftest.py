import datetime
import json
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from opencart_urls import Urls
from locators import AdminSelectors
from config import ROOT_DIR

USER = "user"
PASSWORD = "bitnami"


@pytest.fixture(scope='session')
def administration_login(driver):
    """Fixture will log in administration page of OpenCart and return browser and user_token"""
    driver.get(Urls.administration)
    driver.find_element(*AdminSelectors.Login.user).send_keys(USER)
    driver.find_element(*AdminSelectors.Login.password).send_keys(PASSWORD)
    driver.find_element(*AdminSelectors.Login.submit_btn).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(AdminSelectors.Menu.dashboard))
    return driver


@pytest.fixture(scope='function')
def test_product():
    date_fields = {
        'date_added': datetime.datetime.now().strftime("%Y-%m-%d"),
        'date_available': datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S"),
        'date_modified': datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    }
    with open(f"{ROOT_DIR}/test_data/test_products.json") as test_data:
        product = json.load(test_data)['test_product_1']
        product['oc_product'] |= date_fields
    return product


@pytest.fixture(scope='function')
def product_in_db(connect_db):
    """return True or False"""

    def find_by_name(product_name):
        cursor = connect_db.cursor()
        query = f'SELECT name FROM oc_product_description WHERE name=(%s)'
        return cursor.execute(query, product_name)

    return find_by_name


@pytest.fixture(scope='function')
def add_product_to_db(request, connect_db, test_product, insert_into_table, del_product_from_db):
    cursor = connect_db.cursor()
    product = test_product
    insert_into_table(product['oc_product'], 'oc_product')
    cursor.execute('SELECT product_id FROM oc_product WHERE model=(%s)',
                   product['oc_product']['model'])
    pid = cursor.fetchone()
    insert_into_table({'product_id': pid} | product['oc_product_description'], 'oc_product_description')
    insert_into_table({'value': pid} | product['oc_seo_url'], 'oc_seo_url')

    def del_product():
        del_product_from_db(product['oc_product_description']['name'])

    request.addfinalizer(del_product)
    return product['oc_product_description']['name']


@pytest.fixture(scope='function')
def del_product_from_db(connect_db):
    def del_by_name(product_name):
        cursor = connect_db.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%oc_product%'")
        tables = [tab for tup in cursor.fetchall() for tab in tup]
        cursor.execute('SELECT product_id FROM oc_product_description WHERE name=(%s)', product_name)
        product_id = cursor.fetchone()
        if product_id:
            for table in tables:
                cursor.execute(f'DELETE FROM {table} WHERE product_id=(%s)', product_id)
            cursor.execute('DELETE FROM oc_seo_url WHERE value=(%s)', product_id)
            connect_db.commit()
        else:
            return f"Product with id : {product_id} does not exist in db"
    return del_by_name


@pytest.fixture(scope='function')
def validate_in_db(connect_db, del_product_from_db):
    def find_by_name(product_name):
        cursor = connect_db.cursor()
        query = f'SELECT name FROM oc_product_description WHERE name=(%s)'
        sql = cursor.execute(query, product_name)
        assert sql, f'Product with name "{product_name}" does not exist in database'
        del_product_from_db(product_name)

    return find_by_name
