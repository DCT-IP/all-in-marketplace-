from flask import Flask, render_template, request, redirect
from models.queries import get_all_users, get_all_products, add_user

app = Flask(__name__)

@app.route("/")
def home():
    users = get_all_users()
    products = get_all_products()
    return render_template("index.html", users=users, products=products)

@app.route("/add_user", methods=["POST"])
def add_user_route():
    username = request.form["username"]
    add_user(username)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)