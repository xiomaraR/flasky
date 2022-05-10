from flask import Blueprint, jsonify, make_response, abort, request
from app.models.caretaker import Caretaker
from app import db

caretaker_bp = Blueprint("caretaker", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=["GET"])
def read_all_caretakers():
    caretakers = Caretaker.query.all()
    caretakers_response = []
    for caretaker in caretakers:
        caretakers_response.append(
            {
                "id": caretaker.id, 
                "name": caretaker.name
            }
        )
    return jsonify(caretakers_response), 200

@caretaker_bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker(name = request_body["name"])
    db.session.add(new_caretaker)
    db.session.commit()
    return make_response(jsonify(f"Caretaker {new_caretaker.name} with id \
        {new_caretaker.id} successfully created"), 201)

