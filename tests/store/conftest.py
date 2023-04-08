import pytest
import datetime


@pytest.fixture(scope='function')
def test_user(faker, request) -> dict:
    """Return dict with test data of fake user"""
    user = {"date_added": datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S'),
            "customer_group_id": 1,
            "language_id": 1,
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "email": faker.email(),
            "telephone": faker.phone_number(),
            "password": faker.password(length=10),
            "custom_field": "",
            "ip": faker.ipv4_public(),
            "status": 1,
            "safe": 0,
            "token": "",
            "code": 1
            }
    return user


@pytest.fixture(scope='function')
def add_user_in_db(request, test_user, insert_data_in_db, check_user_in_db, del_user_from_db) -> dict:
    def del_user():
        del_user_from_db(user['email'])

    user = test_user
    insert_data_in_db(user, 'oc_customer')
    check_user_in_db(user['email'])
    request.addfinalizer(del_user)
    return user


@pytest.fixture(scope='function')
def check_user_in_db(connect_db):
    def check_user(email: str):
        query = f'SELECT * FROM oc_customer WHERE email=(%s)'
        sql = connect_db.cursor().execute(query, email)
        assert sql, f'User with email "{email}" does not exist in opencart database!'

    return check_user


@pytest.fixture(scope='function')
def del_user_from_db(connect_db):
    def del_by_email(email: str):
        sql_query = f'DELETE FROM oc_customer WHERE email=(%s)'
        connect_db.cursor().execute(sql_query, email)
        connect_db.commit()
        check_query = f'SELECT * FROM oc_customer WHERE email=%s'
        assert not connect_db.cursor().execute(check_query, email), "User somehow still exist in database"

    return del_by_email
