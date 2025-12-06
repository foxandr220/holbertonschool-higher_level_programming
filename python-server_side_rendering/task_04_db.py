#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# --------------------
# Load JSON
# --------------------
def load_products_from_json():
    with open("products.json", "r") as f:
        return json.load(f)


# --------------------
# Load CSV
# --------------------
def load_products_from_csv():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


# --------------------
# Load SQL
# --------------------
def load_products_from_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products

    except Exception:
        return None


# --------------------
# Route
# --------------------
@app.route("/products")
def products():
    source = request.args.get("source")
    prod_id = request.args.get("id")

    # Wrong source
    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html",
                               error="Wrong source",
                               products=[])

    # Load Data
    if source == "json":
        products = load_products_from_json()
    elif source == "csv":
        products = load_products_from_csv()
    else:
        products = load_products_from_sql()
        if products is None:
            return render_template("product_display.html",
                                   error="Database error",
                                   products=[])

    # Filter by id
    if prod_id:
        try:
            prod_id = int(prod_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=[])

        filtered = [p for p in products if p["id"] == prod_id]
        if not filtered:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=[])

        products = filtered

    return render_template("product_display.html",
                           error=None,
                           products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
