import csv
from random import randint
from src.locators.RegPageSelectors import RegisterPage
from selenium import webdriver

chrome = webdriver.Chrome()
print(chrome.capabilities)

def create_new_user():
    user_data = {
        'first_name': 'test_first_name' + str(randint(1, 10000)),
        'last_name': 'test_last_name' + str(randint(1, 10000)),
        'email': 'test_email' + str(randint(1, 1000000)),
        'password': '123456'
    }
    return user_data


