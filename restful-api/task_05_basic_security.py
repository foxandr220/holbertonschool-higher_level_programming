#!/usr/bin/python3
"""API Security example with Basic Auth and JWT"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ---------- Basic config for JWT ----------
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# ---------- In-memory users DB ----------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ---------- BASIC AUTH ----------

@auth.verify_password
def verify_password(username, password):
    """Verify username & password for Basic Auth."""
    user = users.get(username)
    if not user:
        return False
    if not check_password_hash(user["password"], password):
        return False
    return username  # auth.current_user() будет содержать username


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protected with Basic Auth."""
    return "Basic Auth: Access Granted"


# ---------- JWT LOGIN & PROTECTED ROUTES ----------

@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint.

    Expects JSON:
    {
        "username": "...",
        "password": "..."
    }
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Вшиваем роль в claims токена
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims,
    )
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Simple JWT protected route."""
    # identity = get_jwt_identity()  # если нужно, но тут не обязательно
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route available only for admin users."""
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ---------- JWT ERROR HANDLERS (все 401, как требует задание) ----------

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    # Нет токена / неправильный заголовок
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    # Токен невалиден (подпись, структура и т.п.)
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    # Время жизни токена истекло
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    # Если когда-нибудь будешь делать revocation list
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    # Для fresh токенов (здесь просто для полноты примера)
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=False)
