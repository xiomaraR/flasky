from flask import Blueprint, jsonify, request
from app.models.cats import Cat
from app import db

cats_bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@cats_bp.route('', methods=['POST'])
def create_one_cat():
    request_body = request.get_json()
    new_cat = Cat(name=request_body["name"],
                  age=request_body["age"],
                  color=request_body["color"])
    db.session.add(new_cat)
    db.session.commit()
    return {
        "id": new_cat.id,
        "msg": f"Succesfully created cat with id {new_cat.id}"
    }, 201

@cats_bp.route('', methods=['GET'])
def get_all_cats():
    cats = Cat.query.all()
    cats_response = []
    for cat in cats:
        cats_response.append({
            'id': cat.id,
            'name': cat.name,
            'age': cat.age,
            'color': cat.color
        })
    return jsonify(cats_response)




# @cats_bp.route('', methods=['GET'])
# def get_all_cats():
#     cat_response = []
#     for cat in cats:
#         cat_response.append({
#             'id': cat.id,
#             'name': cat.name,
#             'age': cat.age,
#             'color': cat.color
#         })
#     return jsonify(cat_response)


# @cats_bp.route('/<cat_id>', methods=['GET'])
# def get_one_cat(cat_id):
#     try:
#         cat_id = int(cat_id)
#     except ValueError:
#         rsp = {"msg": f"Invalid id: {cat_id}"}
#         return jsonify(rsp), 400
#     chosen_cat = None
#     for cat in cats:
#         if cat.id == cat_id:
#             chosen_cat = cat
#             break
#     if chosen_cat is None:
#         rsp = {"msg": f"Could not find cat with id {cat_id}"}
#         return jsonify(rsp), 404
#     rsp = {
#         'id': chosen_cat.id,
#         'name': chosen_cat.name,
#         'age': chosen_cat.age,
#         'color': chosen_cat.color
#     }
#     return jsonify(rsp), 200