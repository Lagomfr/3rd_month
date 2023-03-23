import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_NAME = 'db.sqlite'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price INTEGER,
    photo TEXT
    )""")

    cursor.execute(
        """ CREATE id INTEGER PRIMARY KEY,
    name TEXT,"""
    )
    db.commit()


if __name__ == "__main__":
    init_db()
    create_tables()
