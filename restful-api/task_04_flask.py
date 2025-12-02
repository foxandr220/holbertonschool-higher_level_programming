#!/usr/bin/python3
"""A simple RESTful API built with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_usernames():
    # Return a list of all usernames
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    # 1. Try to parse JSON
    try:
        data = request.get_json()
        if data is None:
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Check username exists
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Check duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Add new user
    users[username] = data

    # 5. Return success response with 201 Created
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=False)
