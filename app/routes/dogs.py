from flask import Blueprint, jsonify, request

from app import db
from app.models.dogs import Dog

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@dogs_bp.route('', methods=['GET'])
def get_all_dogs():
    dogs = Dog.query.all()
    dog_response = []
    for dog in dogs:
        dog_response.append({
            'id': dog.id,
            'name': dog.name, 
            'age': dog.age
        })
    return jsonify(dog_response)

@dogs_bp.route('', methods=['POST'])
def create_one_dog():
    request_body = request.get_json()

    new_dog = Dog(name= request_body["name"],
                  age=request_body["age"])

    db.session.add(new_dog)
    db.session.commit()

    return {
        "id": new_dog.id, 
        "msg": f'Successfully created dog with id: {new_dog.id}'
        }, 201

# To be fixed to use the Dog model in the following livecode
# @dogs_bp.route('/<dog_id>', methods=['GET'])
# def get_one_dog(dog_id):
#     try:
#         dog_id = int(dog_id)
#     except ValueError:
#         return {"msg": "Invalid dog id"}, 400

#     chosen_dog = None
#     for dog in dogs:
#         if dog.id == dog_id:
#             chosen_dog = dog
#             break
#     if chosen_dog is None:
#         return {"msg": f"Could not find dog with id {dog_id}"}, 404
#     return {
#             'id': chosen_dog.id,
#             'name': chosen_dog.name, 
#             'age': chosen_dog.age
#         }, 200

