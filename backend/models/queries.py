from db import get_cursor


# ---------------- USERS ----------------
def get_all_users():
    db, cursor = get_cursor()
    try:
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()


def add_user(username, role):
    db, cursor = get_cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, role) VALUES (%s, %s)",
            (username, role)
        )
        db.commit()
    finally:
        cursor.close()
        db.close()


# ---------------- PRODUCTS ----------------
def get_all_products():
    db, cursor = get_cursor()
    try:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()


# ---------------- SELLER ----------------
def get_seller_products(seller_id):
    db, cursor = get_cursor()
    try:
        cursor.execute(
            "SELECT product_name, price, stock FROM products WHERE seller_id = %s",
            (seller_id,)
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()


def get_seller_stats(seller_id):
    db, cursor = get_cursor()
    try:
        cursor.execute("""
            SELECT COUNT(*) AS total_products
            FROM products
            WHERE seller_id = %s
        """, (seller_id,))
        total_products = cursor.fetchone()["total_products"]

        cursor.execute("""
            SELECT COUNT(*) AS total_orders
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
            WHERE p.seller_id = %s
        """, (seller_id,))
        total_orders = cursor.fetchone()["total_orders"]

        return {
            "total_products": total_products,
            "total_orders": total_orders
        }

    finally:
        cursor.close()
        db.close()