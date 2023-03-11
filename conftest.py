import datetime
import json
import os
import pytest
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import ROOT_DIR


def pytest_addoption(parser):
    parser.addoption('--browser', '-B', action='store',
                     default='chrome', help='Choose Browser [firefox/chrome]')
    parser.addoption('--headless', '-H', action='store',
                     default='true', help='Headless Mode [true/false]')


@pytest.fixture(scope='session')
def driver(request):
    """Start chosen browser and close after work"""
    browser = request.config.getoption('browser')
    headless_mode = request.config.getoption('headless')
    match browser:
        case 'chrome':
            chrome_options = ChromeOptions()
            if headless_mode == 'true':
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument('--ignore-ssl-errors=yes')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
        case 'firefox':
            firefox_options = FirefoxOptions()
            if headless_mode == 'true':
                firefox_options.add_argument("--headless")
            os.environ['MOZ_HEADLESS_WIDTH'] = '1920'
            os.environ['MOZ_HEADLESS_HEIGHT'] = '1080'
            firefox_options.add_argument("--width=1920")
            firefox_options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=firefox_options)
        case _:
            raise ValueError(f"Can't open browser with name{browser}, 'chrome' or 'firefox' only available'")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)

    return driver


@pytest.fixture(scope='module')
def connect_db(request):
    """Connect to MariaDB before test and close connection after"""
    connection = pymysql.connect(host="localhost", port=3306, user="bn_opencart", passwd="",
                                 database="bitnami_opencart")
    request.addfinalizer(connection.close)
    return connection


@pytest.fixture(scope='function')
def test_user(request, insert_into_table, del_user_from_db):
    """Inserting test user in database and delete after test"""
    date_added = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    with open(f'{ROOT_DIR}/test_data/test_users.json') as test_data:
        user = {'date_added': date_added} | json.load(test_data)['test_user_1']
    insert_into_table(user, 'oc_customer')

    def del_user():
        del_user_from_db(user['email'])

    request.addfinalizer(del_user)
    return user


@pytest.fixture(scope='function')
def check_user_exist_in_db(connect_db):
    def check_user_by_email(email: str):
        query = f'SELECT * FROM oc_customer WHERE email=(%s)'
        sql = connect_db.cursor().execute(query, email)
        assert sql, f'User with email "{email}" does not exist in opencart database!'

    return check_user_by_email


@pytest.fixture(scope='function')
def del_user_from_db(connect_db):
    def del_user_by_email(email: str):
        sql_query = f'DELETE FROM oc_customer WHERE email=(%s)'
        connect_db.cursor().execute(sql_query, email)
        connect_db.commit()
        check_query = f'SELECT * FROM oc_customer WHERE email=%s'
        assert not connect_db.cursor().execute(check_query, email), "User somehow still exist in database"

    return del_user_by_email


@pytest.fixture(scope='function')
def insert_into_table(connect_db):
    def insert(data: dict, table_name: str) -> None:
        fields = ', '.join(list(data.keys()))
        values = '%s, ' * len(data)
        query = f"INSERT INTO {table_name} ({fields}) VALUES ({values[:-2]})"
        connect_db.cursor().execute(query, tuple(data.values()))
        connect_db.commit()

    return insert
