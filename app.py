from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# In-memory storage (for learning/demo only)
items = []


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome! Flask API is running successfully 🚀"
    }), 200


# ---------------------------
# Health Check Endpoint
# ---------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }), 200


# ---------------------------
# Home Endpoint
# ---------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask API running on Azure 🚀",
        "endpoints": [
            "GET /health",
            "GET /items",
            "POST /items"
        ]
    })


# ---------------------------
# GET Items
# ---------------------------
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({
        "count": len(items),
        "data": items
    }), 200


# ---------------------------
# POST Item
# ---------------------------
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    # Validation
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


# ---------------------------
# Entry Point (for local run)
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)