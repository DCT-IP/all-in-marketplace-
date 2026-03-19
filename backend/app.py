from flask import Flask, request, jsonify, render_template
from db import get_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# ---------------- PRODUCTS ----------------
@app.route('/products')
def get_products():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM inventory")
    products = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(products)


# ---------------- CART ----------------
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO shopping_cart(user_id, product_id, quantity) VALUES (%s,%s,%s)",
        (data['user_id'], data['product_id'], 1)
    )

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Added to cart"})


@app.route('/cart/<int:user_id>')
def view_cart(user_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT i.product_name, sc.quantity
        FROM shopping_cart sc
        JOIN inventory i ON sc.product_id = i.product_id
        WHERE sc.user_id = %s
    """, (user_id,))

    cart = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(cart)


# ---------------- ORDER ----------------
@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json

    db = get_db()
    cursor = db.cursor()

    cursor.callproc('place_order', [data['user_id'], data['product_id']])
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Order placed successfully"})


if __name__ == '__main__':
    app.run(debug=True)