from flask import Flask, render_template, request, redirect, jsonify
from models.queries import (
    get_all_users,
    get_all_products,
    add_user,
    get_seller_stats,
    get_seller_products
)
from db import get_cursor

app = Flask(
    __name__,
    static_folder="../frontend",
    template_folder="../frontend"
)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ADD USER ----------------
@app.route("/add_user", methods=["POST"])
def add_user_route():
    try:
        username = request.form.get("username")
        role = request.form.get("role")

        if not username or not role:
            return "Invalid input", 400

        add_user(username, role)
        return redirect("/")

    except Exception as e:
        return str(e), 500


# ---------------- PRODUCTS API ----------------
@app.route("/products")
def products_api():
    try:
        products = get_all_products()

        result = []
        for p in products:
            result.append({
                "product_id": p["product_id"],
                "product_name": p["product_name"],
                "product_description": p["product_description"],
                "image_url": p["image_url"],
                "price": float(p["price"]),
                "category": p["category"],
                "product_condition": p["product_condition"],
                "stock": p["stock"]
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- ADD TO CART ----------------
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()

    if not data or "user_id" not in data or "product_id" not in data:
        return jsonify({"error": "Invalid request"}), 400

    db, cursor = get_cursor()

    try:
        cursor.execute(
            "SELECT quantity FROM shopping_cart WHERE user_id=%s AND product_id=%s",
            (data["user_id"], data["product_id"])
        )
        existing = cursor.fetchone()

        if existing:
            cursor.execute(
                "UPDATE shopping_cart SET quantity = quantity + 1 WHERE user_id=%s AND product_id=%s",
                (data["user_id"], data["product_id"])
            )
        else:
            cursor.execute(
                "INSERT INTO shopping_cart (user_id, product_id, quantity) VALUES (%s, %s, 1)",
                (data["user_id"], data["product_id"])
            )

        db.commit()
        return jsonify({"message": "Added to cart"})

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        db.close()


# ---------------- PLACE ORDER ----------------
@app.route("/place_order", methods=["POST"])
def place_order():
    data = request.get_json()

    if not data or "user_id" not in data or "product_id" not in data:
        return jsonify({"error": "Invalid request"}), 400

    db, cursor = get_cursor()

    try:
        cursor.execute(
            "SELECT stock FROM products WHERE product_id = %s",
            (data["product_id"],)
        )
        result = cursor.fetchone()

        if not result:
            return jsonify({"error": "Product not found"}), 404

        if result["stock"] <= 0:
            return jsonify({"error": "Out of stock"}), 400

        cursor.execute(
            "INSERT INTO orders (user_id, product_id) VALUES (%s, %s)",
            (data["user_id"], data["product_id"])
        )

        cursor.execute(
            "UPDATE products SET stock = stock - 1 WHERE product_id = %s",
            (data["product_id"],)
        )

        db.commit()
        return jsonify({"message": "Order placed"})

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        db.close()


# ---------------- GET CART ----------------
@app.route("/cart/<int:user_id>")
def get_cart(user_id):
    db, cursor = get_cursor()

    try:
        cursor.execute("""
            SELECT p.product_id, p.product_name, sc.quantity            
            FROM shopping_cart sc
            JOIN products p ON sc.product_id = p.product_id
            WHERE sc.user_id = %s
        """, (user_id,))

        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        db.close()


# ---------------- SELLER DASHBOARD API ----------------
@app.route("/seller/<int:seller_id>")
def seller_dashboard(seller_id):
    try:
        stats = get_seller_stats(seller_id)
        products = get_seller_products(seller_id)

        product_list = []
        for p in products:
            product_list.append({
                "product_name": p["product_name"],
                "price": float(p["price"]),
                "stock": p["stock"]
            })

        return jsonify({
            "stats": stats,
            "products": product_list
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- ROLE-BASED DASHBOARD ----------------
@app.route("/dashboard/<int:user_id>")
def dashboard(user_id):
    db, cursor = get_cursor()

    try:
        cursor.execute(
            "SELECT role FROM users WHERE user_id = %s",
            (user_id,)
        )
        result = cursor.fetchone()

        if not result:
            return "User not found", 404

        role = result["role"]

        if role == "seller":
            return render_template("seller.html")
        else:
            return render_template("dashboard.html")

    finally:
        cursor.close()
        db.close()


# ---------------- PAGES ----------------
@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/cart")
def cart_page():
    return render_template("cart.html")


@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


@app.route("/seller_page")
def seller_page():
    return render_template("seller.html")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)