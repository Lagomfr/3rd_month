import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        price INTEGER,
        photo TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        username TEXT,
        address TEXT,
        product_id INTEGER,
        FOREIGN KEY (product_id)
            REFERENCES products(id)
            ON DELETE CASCADE
    )
    """)

    db.commit()


def add_products():
    cursor.execute("""INSERT INTO products(name, description, price, photo) VALUES 
    ('Книга 1', 'Самая замечательная книга', 100, '/images/cat.jfif'),
    ('Книга 2', 'Самая замечательная книга', 200, '/images/cat.jfif')
    """)

    db.commit()


def delete_table_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


def get_products():
    cursor.execute("""
    SELECT * FROM products;
    """)

    return cursor.fetchall()


def create_clients(data):
    """
        Заполняем таблицу order
    """
    data = data.as_dict()
    cursor.execute(
        '''
        INSERT INTO orders(
        username,
        age,
        address,
        delivery_day,
        product_id
        ) VALUES (:username,:age,:address,:delivery_day,:product_id)''',
        {'username': data['name'],
         'age': data['age'],
         'address': data['address'],
         'delivery_day': data['delivery_day'],
         'product_id': data['product_id']})
    db.commit()


if __name__ == "__main__":
    init_db()
    delete_table_products()
    create_tables()
    add_products()
