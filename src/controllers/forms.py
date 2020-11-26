from flask import Blueprint
from flask import request, jsonify

from src.database import forms, client

app = Blueprint('forms', __name__)

db = client.Database().db


@app.route("/data", methods=["POST"])
def insert_form():
    if request.method == "POST":
        form = request.get_json()
        result = forms.insert(db, form)
        return jsonify(
            {
                "id": str(result.inserted_id)
            }
        ), 201


@app.route("/data/<form_id>", methods=["GET"])
def get_form(form_id):
    if request.method == "GET":
        form = forms.find_by_id(db, form_id)
        return jsonify(
            {
                "form": form
            }
        ), 200
