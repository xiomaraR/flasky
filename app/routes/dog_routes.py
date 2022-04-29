from flask import Blueprint, jsonify, abort, make_response
from ..models.dog import Dog
from app import db

bp = Blueprint("dogs", __name__, url_prefix="/dogs")

# See cat.py for more about why this method is here
def make_dog_safe(data_dict):
    try:
        return Dog.from_dict(data_dict)
    except KeyError as e:
        abort(make_response(jsonify(dict(details=f"missing required field: {e}")), 400))

# POST /dogs
@bp.route("", methods=("POST",))
def create_dog():
    request_body = request.get_json()
    dog = make_dog_safe(request_body)

    db.session.add(dog)
    db.session.commit()

    return jsonify(dog.to_dict()), 201

# GET /dogs

@bp.route("", methods=("GET",))
def index_dogs():
    dogs = Dog.query.all()

    result_list = [dog.to_dict() for dog in dogs]

    return jsonify(result_list)

# def validate_dog(id):
#     try:
#         id = int(id)
#     except ValueError:
#         abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))

#     for dog in dogs:
#         if dog.id == id:
#             # return the dog
#             return dog

#     # no dog found
#     abort(make_response(jsonify(dict(details=f"dog id {id} not found")), 404))    

# # GET /dogs/id
# @bp.route("/<id>", methods=("GET",))
# def get_dog(id):
#     dog = validate_dog(id)
#     return jsonify(dog.to_dict())
