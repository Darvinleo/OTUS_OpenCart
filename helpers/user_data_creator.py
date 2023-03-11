from random import randint


def user_data_creator() -> dict:
    user_data = {
        'firstname': 'test_first_name' + str(randint(1, 10000)),
        'lastname': 'test_last_name' + str(randint(1, 10000)),
        'email': 'test_email' + str(randint(1, 1000000)) + '@mail.com',
        'password': '123456'
    }
    return user_data
