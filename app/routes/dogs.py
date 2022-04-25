from flask import Blueprint, jsonify

class Dog:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

dogs = [
    Dog(1, 'Roscoe', 7),
    Dog(2, 'Toto', 2),
    Dog(3, 'Snowpuff', 13)
]

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@dogs_bp.route('', methods=['GET'])
def get_all_dogs():
    dog_response = []
    for dog in dogs:
        dog_response.append({
            'id': dog.id,
            'name': dog.name, 
            'age': dog.age
        })
    return jsonify(dog_response)

@dogs_bp.route('/<dog_id>', methods=['GET'])
def get_one_dog(dog_id):
    try:
        dog_id = int(dog_id)
    except ValueError:
        return {"msg": "Invalid dog id"}, 400

    chosen_dog = None
    for dog in dogs:
        if dog.id == dog_id:
            chosen_dog = dog
            break
    if chosen_dog is None:
        return {"msg": f"Could not find dog with id {dog_id}"}, 404
    return {
            'id': chosen_dog.id,
            'name': chosen_dog.name, 
            'age': chosen_dog.age
        }, 200

