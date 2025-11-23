from flask import Flask, request, jsonify
from database import add_or_update_client
import os

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    client_id = data.get("client_id")
    if not client_id:
        return jsonify({"error": "Aucun ID reçu"}), 400

    message = add_or_update_client(client_id)
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
