from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Application configuration from environment variables
APP_ENV = os.getenv("APP_ENV", "development")
DB_HOST = os.getenv("DB_HOST", "localhost")
APP_PORT = int(os.getenv("APP_PORT", "8080"))

# Temporary in-memory product store
products = {}
next_product_id = 1


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "application": "E-Commerce Product API",
        "environment": APP_ENV
    }), 200


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(list(products.values())), 200


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = products.get(product_id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(product), 200


@app.route("/products", methods=["POST"])
def add_product():
    global next_product_id

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "name" not in data or "price" not in data:
        return jsonify({
            "error": "name and price are required"
        }), 400

    product = {
        "id": next_product_id,
        "name": data["name"],
        "price": data["price"]
    }

    products[next_product_id] = product
    next_product_id += 1

    return jsonify(product), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = products.get(product_id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    data = request.get_json()

    if "name" in data:
        product["name"] = data["name"]

    if "price" in data:
        product["price"] = data["price"]

    return jsonify(product), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({
            "error": "Product not found"
        }), 404

    deleted_product = products.pop(product_id)

    return jsonify({
        "message": "Product deleted successfully",
        "product": deleted_product
    }), 200


if __name__ == "__main__":
    print(f"Starting Product API")
    print(f"APP_ENV: {APP_ENV}")
    print(f"DB_HOST: {DB_HOST}")
    print(f"APP_PORT: {APP_PORT}")

    app.run(
        host="0.0.0.0",
        port=APP_PORT
    )