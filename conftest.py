import pytest
from selenium import webdriver


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
