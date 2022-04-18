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

