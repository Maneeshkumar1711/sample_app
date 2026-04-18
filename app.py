from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

items = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask API running on Azure 🚀",
        "endpoints": [
            "GET /health",
            "GET /items",
            "POST /items"
        ]
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }), 200


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({
        "count": len(items),
        "data": items
    }), 200


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({
            "error": "Invalid request. 'name' is required."
        }), 400

    item = {
        "id": len(items) + 1,
        "name": data["name"],
        "created_at": datetime.utcnow().isoformat()
    }

    items.append(item)

    return jsonify({
        "message": "Item created successfully",
        "item": item
    }), 201
