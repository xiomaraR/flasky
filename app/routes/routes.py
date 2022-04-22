from flask import Blueprint, jsonify

class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality

cats = [
    Cat(1, "Muna", "black", "mischevious"),
    Cat(2, "Matthew", "spotted", "cuddly"),
    Cat(3, "George", "Gray","Sassy")
]

bp = Blueprint("cats", __name__, url_prefix="/cats")

# GET /cats
# GET /cats/id

@bp.route("", methods=("GET",))
def index_cats():
    result_list = [dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality,
        ) for cat in cats]

    return jsonify(result_list)