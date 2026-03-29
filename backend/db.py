# models/db.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbs@29",
        database="marketplace"
    )