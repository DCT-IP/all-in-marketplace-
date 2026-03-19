from db import cursor, db

def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_all_products():
    cursor.execute("SELECT * FROM inventory")
    return cursor.fetchall()

def add_user(username):
    cursor.execute(
        "INSERT INTO users (username, date_of_join) VALUES (%s, CURDATE())",
        (username,)
    )
    db.commit()