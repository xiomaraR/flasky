from flask import make_response, abort
from app.models.cat import Cat

def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"cat {id} is invalid"}, 400))

    cat = Cat.query.get(id)

    if not cat:
        abort(make_response({"message":f"cat {id} not found"}, 404))
    
    return cat