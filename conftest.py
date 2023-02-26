import pytest
import pymysql
import datetime
import json
from selenium import webdriver
from config import ROOT_DIR


def pytest_addoption(parser):
    parser.addoption('--browser', '-B', action='store', default='chrome', help='Choose Browser')


@pytest.fixture(scope='function')
def driver(request):
    """Start chosen browser and close after work"""
    browser = request.config.getoption('browser')
    match browser:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
        case _:
            raise ValueError(f"Can't open browser with name{browser}, 'chrome' or 'firefox' only available'")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)

    return driver


@pytest.fixture(scope='function')
def connect_db(request):
    """Connect to MariaDB before test and close connection after"""
    connection = pymysql.connect(host="localhost", port=3306, user="bn_opencart", passwd="",
                                 database="bitnami_opencart")
    request.addfinalizer(connection.close)
    return connection


@pytest.fixture(scope='function')
def insert_test_user_in_db(request, connect_db):
    cursor = connect_db.cursor()
    date_added = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    test_user = {'date_added': date_added}
    with open(f'{ROOT_DIR}/test_data/test_users.json') as test_data:
        test_user |= json.load(test_data)['test_user_1']
    columns = f"({', '.join([field for field in test_user.keys()])})"
    values = tuple(val for val in test_user.values())
    sql_query = f'INSERT INTO oc_customer {columns} \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(sql_query, values)
    connect_db.commit()

    def del_user_by_email():
        sql_query = f'DELETE FROM oc_customer WHERE email=(%s)'
        connect_db.cursor().execute(sql_query, test_user['email'])
        connect_db.commit()

    request.addfinalizer(del_user_by_email)
    return test_user


@pytest.fixture(scope='function')
def check_user_exist_in_db(connect_db):
    def check_user_by_email(email: str):
        sql_query = f'SELECT * FROM oc_customer WHERE email=(%s)'
        sql_exec = connect_db.cursor().execute(sql_query, email)
        assert sql_exec, f'User with email "{email}" is not exist in opencart database!'

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
