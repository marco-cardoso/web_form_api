from flask import request, jsonify
from flask import Blueprint

app = Blueprint('main', __name__)


@app.route("/health", methods=['GET'])
def health():
    if request.method == "GET":
        return jsonify(
            {
                "message": "ok"
            }
        ), 200
