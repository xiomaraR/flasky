from flask import Blueprint, jsonify, abort, make_response, request
from ..models.cat import Cat
from app import db

bp = Blueprint("cats", __name__, url_prefix="/cats")

# helper method to turn key errors into a nice error message
# Cat.from_dict is what "knows" that it needs certain keys from
# a dictionary, but it doesn't "know" anything about Flask routes and error
# handling. So we put the responsibility that Cat should know about in a
# function in Cat, but leave the stuff that Flask should know about here.
# Further refactors are possible!

def make_cat_safe(data_dict):
    try:
        return Cat.from_dict(data_dict)
    except KeyError as e:
        abort(make_response(jsonify(dict(details=f"missing required field: {e}")), 400))

# POST /cats
@bp.route("", methods=("POST",))
def create_cat():
    request_body = request.get_json()
    cat = make_cat_safe(request_body)

    db.session.add(cat)
    db.session.commit()

    return jsonify(cat.to_dict()), 201
    
# GET /cats

@bp.route("", methods=("GET",))
def index_cats():
    cats = Cat.query.all()

    result_list = [cat.to_dict() for cat in cats]

    return jsonify(result_list)

# def validate_cat(id):
#     try:
#         id = int(id)
#     except ValueError:
#         abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))

#     for cat in cats:
#         if cat.id == id:
#             # return the cat
#             return cat

#     # no cat found
#     abort(make_response(jsonify(dict(details=f"cat id {id} not found")), 404))    

# # GET /cats/id
# @bp.route("/<id>", methods=("GET",))
# def get_cat(id):
#     cat = validate_cat(id)
#     return jsonify(cat.to_dict())
