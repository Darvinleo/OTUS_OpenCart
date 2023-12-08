import pytest
import pymysql
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', '-B', action='store',
                     default='chrome', help='Choose Browser [firefox/chrome]')
    parser.addoption('--headless', '-H', action='store',
                     default='false', help='Headless Mode [true/false]')


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
    connection = pymysql.connect(host="localhost", port=3306, user="bn_opencart", passwd="",
                                 database="bitnami_opencart")
    request.addfinalizer(connection.close)
    return connection


@pytest.fixture(scope='function')
def insert_data_in_db(connect_db):
    def inserter(data: dict, t_name: str):
        cursor = connect_db.cursor()
        columns = f"({', '.join(list(data.keys()))})"
        values = tuple(val for val in data.values())
        sql_query = f"INSERT INTO {t_name} {columns} VALUES ({'%s,' * len(data)}"[:-1] + ")"
        cursor.execute(sql_query, values)
        connect_db.commit()

    return inserter
