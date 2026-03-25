import mysql.connector


def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbs@29",   # <-- CHANGE THIS
        database="marketplace"          # <-- CHANGE THIS
    )


def get_cursor():
    db = get_db()
    return db, db.cursor(dictionary=True)