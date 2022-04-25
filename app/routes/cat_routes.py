from flask import Blueprint, jsonify, make_response, abort 

class Cat:
    def __init__(self, id, name, personality, breed, age, tricks=None):
        self.id = id
        self.name = name
        self.personality = personality
        self.breed = breed
        self.age = age
        self.tricks = tricks or []
        self.toe_beans = 16

    def to_json(self): #this method can be used across any route/function
        return {
            "id": self.id,
            "name": self.name,
            "personality": self.personality,
            "breed": self.breed,
            "age": self.age,
            "tricks": self.tricks,
            "toe_beans": self.toe_beans
        }

cats = [
    Cat(1, "hamburger", "sassy", "tabby", 4, ["loves Philomena"]),
    Cat(2, "Scully", "grumpy", "tuxdedo", 4, []),
    Cat(3, "Leonardo Dicatrio", "cuddly", "tuxdedo", 4, []),
    Cat(4, "Luna", "pragmatic", "scottish fold", 100, ["magic"])
]

cat_bp = Blueprint("cat", __name__, url_prefix="/cats")

# GET ALL
@cat_bp.route("", methods=["GET"])
def read_all_cats():
    cats_response = []
    for cat in cats:
        # Note: to_json is the helper method in the class
        cats_response.append(cat.to_json())
        
        # Note: Older way, much longer
        # cats_response.append({
        #     "name": cat.name,
        #     "personality": cat.personality,
        #     "breed": cat.breed,
        #     "age": cat.age,
        #     "tricks": cat.tricks,
        #     "toe_beans": cat.toe_beans
        # })

    return jsonify(cats_response)

def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"cat {id} is invalid"}, 400))

    for cat in cats:
        if cat.id == id:
            return cat

    return abort(make_response({"message":f"cat {id} not found"}, 404))

# GET one cat
@cat_bp.route("/<id>", methods = ["GET"])
def read_one_cat(id):
    cat = validate_cat(id)
    return jsonify(cat.to_json(), 200)