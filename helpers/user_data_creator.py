from random import randint


def user_data_creator() -> dict:
    user_data = {
        'firstname': 'test_first_name' + str(randint(1, 10000)),
        'lastname': 'test_last_name' + str(randint(1, 10000)),
        'email': 'test_email' + str(randint(1, 1000000)) + '@mail.com',
        'password': '123456'
    }
    return user_data

# def get_existing_user() -> dict:
#     """Extracting credentials of user that was previously created and stores in test_data/users.csv"""
#     with open(f"{ROOT_DIR}/test_data/users.csv", 'r', encoding='UTF-8') as users:
#         reader = csv.DictReader(users)
#         user = {}
#         for row in reader:
#             user = row
#             break
#         return user
