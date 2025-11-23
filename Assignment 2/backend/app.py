from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Path to stored message file
DATA_PATH = "/data/message.txt"


def read_message():
    """
    TODO: 
    - If DATA_PATH exists, read and return the text inside
    - If it doesn't exist, return an empty string
    """
    try:
        if os.path.exists(DATA_PATH):
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                return f.read()
        return ""
    except Exception:
        return ""


def write_message(msg: str):
    """
    TODO:
    - Open DATA_PATH
    - Write msg to the file
    """
    try:
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            f.write(msg)
    except Exception:
        return


@app.route("/api/message", methods=["GET"])
def get_message():
    """
    TODO:
    - Call read_message()
    - Return { "message": <stored message> } as JSON
    """
    msg = read_message()
    return jsonify({"message": msg})


@app.route("/api/message", methods=["POST"])
def update_message():
    """
    TODO:
    - Get JSON from request
    - Extract the field "message"
    - Call write_message() to save it
    - Return { "status": "ok" }
    """
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    write_message(message)
    return jsonify({"status": "ok"})


# v1 has no /api/health endpoint
# (Students add this in v2)

# v2 TODO:
# - Modify write_message() or update_message() to include a timestamp
#   Format: "<message> (updated at YYYY-MM-DD HH:MM:SS)"
#
# - Add new endpoint /api/health that returns:
#   { "status": "healthy" }


if __name__ == "__main__":
    # Do not change the host or port
    app.run(host="0.0.0.0", port=5001)
