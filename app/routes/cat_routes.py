from tkinter import N
from flask import Blueprint, jsonify

class Cat:
    def __init__(self, name, personality, breed, age, tricks):
        self.name = name
        self.personality = personality
        self.breed = breed
        self.age = age
        self.tricks = tricks
        self.toe_beans = 16

    def to_json(self): #this method can be used across any route/function
        return {
            "name": self.name,
            "personality": self.personality,
            "breed": self.breed,
            "age": self.age,
            "tricks": self.tricks,
            "toe_beans": self.toe_beans
        }

cats = [
    Cat("hamburger", "sassy", "tabby", 4, ["loves Philomena"]),
    Cat("Scully", "grumpy", "tuxdedo", 4, []),
    Cat("Leonardo Dicatrio", "cuddly", "tuxdedo", 4, []),
    Cat("Luna", "pragmatic", 100, ["magic"])
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