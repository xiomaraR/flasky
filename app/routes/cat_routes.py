from flask import Blueprint, jsonify, make_response, abort, request
from app.models.cat import Cat
from app import db

cat_bp = Blueprint("cat", __name__, url_prefix="/cats")

# CREATE CAT
@cat_bp.route("", methods=["POST"])
def create_cat():
    request_body = request.get_json()

    new_cat = Cat(
        name=request_body['name'],
        personality=request_body['personality'],
        age=request_body['age'],
        breed=request_body['breed']
    )

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} has been successfully created!",201)


# GET ALL
@cat_bp.route("", methods=["GET"])
def read_all_cats():
    cats_response = []
    cats = Cat.query.all()
    for cat in cats:
        cats_response.append(cat.to_json())

    return jsonify(cats_response), 200

def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"cat {id} is invalid"}, 400))

    cat = Cat.query.get(id)

    if not cat:
        abort(make_response({"message":f"cat {id} not found"}, 404))
    
    return cat

# GET one cat
@cat_bp.route("/<id>", methods = ["GET"])
def read_one_cat(id):
    cat = validate_cat(id)
    return jsonify(cat.to_json()), 200

@cat_bp.route("/<id>", methods = ["PUT"])
def update_one_cat(id):
    cat = validate_cat(id)
    request_body = request.get_json()

    cat.name = request_body["name"]
    cat.personality = request_body["personality"]
    cat.breed = request_body["breed"]
    cat.age = request_body["age"]
    cat.toe_beans = request_body["toe_beans"] 

    db.session.commit()
    return make_response(f"Cat #{cat.id} successfully updated"), 200

@cat_bp.route("/<id>", methods = ["DELETE"])
def delete_one_cat(id):
    cat = validate_cat(id)
    db.session.delete(cat)
    db.session.commit()

    return make_response(f"Cat #{cat.id} successfully deleted"), 200
