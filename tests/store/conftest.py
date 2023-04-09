import pytest
import datetime


@pytest.fixture(scope='function')
def test_user(faker):
    def make():
        user = {"date_added": datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S'),
                "customer_group_id": 1,
                "language_id": 1,
                "firstname": faker.unique.first_name(),
                "lastname": faker.unique.last_name(),
                "email": faker.unique.email(),
                "telephone": faker.unique.phone_number(),
                "password": faker.unique.password(length=10),
                "custom_field": "",
                "ip": faker.unique.ipv4_public(),
                "status": 1,
                "safe": 0,
                "token": "",
                "code": 1
                }
        return user

    return make


@pytest.fixture(scope='function')
def add_user_in_db(request, test_user, insert_data_in_db, check_user_in_db, del_user_from_db) -> list:
    """
        Add test user in db and return list with users, by default generate only 1 user
        support for `@pytest.mark.num_users(<some number>)
    """

    def del_users():
        for u in users:
            del_user_from_db(u['email'])

    m = request.node.get_closest_marker("num_users")
    if m and len(m.args) > 0:
        num_users = m.args[0]
    else:
        num_users = 1
    users = [test_user() for _ in range(num_users)]
    for user in users:
        insert_data_in_db(user, 'oc_customer')
        check_user_in_db(user['email'])
    request.addfinalizer(del_users)
    return users


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
