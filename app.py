from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# DB connection
def connect_db():
    return sqlite3.connect("products.db")

# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price INTEGER,
        image TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()

# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")

# PRODUCTS PAGE + FILTER
@app.route("/products")
def products():
    category = request.args.get("category")

    conn = connect_db()
    cursor = conn.cursor()

    if category:
        cursor.execute("SELECT * FROM products WHERE category=?", (category,))
    else:
        cursor.execute("SELECT * FROM products")

    data = cursor.fetchall()
    conn.close()

    return render_template("products.html", products=data)

# CONTACT PAGE
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)