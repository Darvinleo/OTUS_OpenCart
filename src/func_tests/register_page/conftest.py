import pytest
import csv
from random import randint


@pytest.fixture()
def create_new_user():
    user_data = {
        'first_name': 'test_first_name' + str(randint(1, 10000)),
        'last_name': 'test_last_name' + str(randint(1, 10000)),
        'email': 'test_email' + str(randint(1, 1000000)) + '@mail.com',
        'password': '123456'
    }
    return user_data
