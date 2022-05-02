from flask import Blueprint, jsonify, request, make_response, abort

from app import db
from app.models.dogs import Dog

def get_dog_or_abort(dog_id):
    try:
        dog_id = int(dog_id)
    except ValueError:
        return abort(make_response({"msg": "Invalid dog id!"}, 400))

    dog = Dog.query.get(dog_id)

    if dog is None:
        return abort(make_response({"msg": f"Could not find dog with id {dog_id}!"}, 404))
    
    return dog


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

@dogs_bp.route('/<dog_id>', methods=['GET'])
def get_one_dog(dog_id):
    dog = get_dog_or_abort(dog_id)
    return {
            'id': dog.id,
            'name': dog.name, 
            'age': dog.age
        }, 200


@dogs_bp.route('/<dog_id>', methods=['PUT'])
def update_one_dog(dog_id):
    request_body = request.get_json()
    if "name" not in request_body or \
       "age" not in request_body:
        return {"msg": "Request must include name and age"}, 400

    dog = get_dog_or_abort(dog_id)

    dog.name = request_body["name"]
    dog.age = request_body["age"]

    db.session.commit()
    
    return {
            'id': dog.id,
            'name': dog.name, 
            'age': dog.age
        }, 200

@dogs_bp.route('/<dog_id>', methods=['DELETE'])
def delete_one_dog(dog_id):
    dog = get_dog_or_abort(dog_id)

    db.session.delete(dog)
    db.session.commit() 

    return {"msg": f"Doggo with id {dog_id} deleted"}, 200
