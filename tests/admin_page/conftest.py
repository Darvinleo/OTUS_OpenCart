import datetime
import pytest


@pytest.fixture(scope='function')
def test_product(faker):
    date = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    product = {
        "oc_product": {
            "model": faker.word(),
            "sku": "",
            "upc": "",
            "ean": "",
            "jan": "",
            "isbn": "",
            "mpn": "",
            "location": "",
            "quantity": 1,
            "stock_status_id": 5,
            "image": "",
            "rating": faker.random.randint(1, 10),
            "manufacturer_id": 11,
            "tax_class_id": 0,
            'date_available': datetime.datetime.now().strftime("%Y-%m-%d"),
            'date_added': date,
            'date_modified': date
        },
        "oc_product_description": {
            "language_id ": 1,
            "name": faker.word(),
            "description": faker.text(max_nb_chars=150),
            "tag": "",
            "meta_title": faker.word(),
            "meta_description": "",
            "meta_keyword": ""
        },
        "oc_seo_url": {
            "store_id": 0,
            "language_id": 0,
            "`key`": "product_id",
            "keyword": faker.word(),
            "sort_order": 0
        }
    }
    return product


@pytest.fixture(scope='function')
def add_product_to_db(request, connect_db, test_product, insert_data_in_db, del_product_from_db):
    cursor = connect_db.cursor()
    product = test_product
    insert_data_in_db(product['oc_product'], 'oc_product')
    cursor.execute('SELECT product_id FROM oc_product WHERE model=(%s)',
                   product['oc_product']['model'])
    pid = cursor.fetchone()
    insert_data_in_db({'product_id': pid} | product['oc_product_description'], 'oc_product_description')
    insert_data_in_db({'value': pid} | product['oc_seo_url'], 'oc_seo_url')

    def del_product():
        del_product_from_db(product['oc_product_description']['name'])

    request.addfinalizer(del_product)
    return product['oc_product_description']['name']


@pytest.fixture(scope='function')
def product_in_db(connect_db):
    """return True or False"""

    def find_by_name(product_name):
        cursor = connect_db.cursor()
        query = f'SELECT name FROM oc_product_description WHERE name=(%s)'
        return cursor.execute(query, product_name)

    return find_by_name


@pytest.fixture(scope='function')
def del_product_from_db(connect_db):
    def del_by_name(product_name):
        cursor = connect_db.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%oc_product%'")
        tables = [tab for tup in cursor.fetchall() for tab in tup]
        cursor.execute('SELECT product_id FROM oc_product_description WHERE name=(%s)', product_name)
        product_id = cursor.fetchone()
        if product_id:
            for table in tables:
                cursor.execute(f'DELETE FROM {table} WHERE product_id=(%s)', product_id)
            cursor.execute('DELETE FROM oc_seo_url WHERE value=(%s)', product_id)
            connect_db.commit()
        else:
            return f"Product with id : {product_id} does not exist in db"

    return del_by_name


@pytest.fixture(scope='function')
def validate_in_db(connect_db, del_product_from_db):
    def find_by_name(product_name):
        cursor = connect_db.cursor()
        query = f'SELECT name FROM oc_product_description WHERE name=(%s)'
        sql = cursor.execute(query, product_name)
        assert sql, f'Product with name "{product_name}" does not exist in database'
        del_product_from_db(product_name)

    return find_by_name
