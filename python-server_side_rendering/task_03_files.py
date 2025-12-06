#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_products():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return None


def load_csv_products():
    products = []
    try:
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
    except Exception:
        return None


@app.route('/products')
def products():
    source = request.args.get("source")
    prod_id = request.args.get("id")

    # Wrong source
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    # Load proper file
    if source == "json":
        products = load_json_products()
    else:
        products = load_csv_products()

    if products is None:
        return render_template("product_display.html", error="Could not load data")

    # If id provided, filter
    if prod_id:
        try:
            prod_id = int(prod_id)
        except ValueError:
            return render_template("product_display.html", error="Product not found")

        filtered = [p for p in products if p["id"] == prod_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found")

        products = filtered

    return render_template("product_display.html", products=products, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
