from flask import Blueprint, jsonify, request

from app import db
from app.models.cars import Car

cars_bp = Blueprint("cars", __name__, url_prefix="/cars")

@cars_bp.route("", methods=["POST"])
def create_car():
    request_body = request.get_json()

    new_car = Car(
        driver=request_body["driver"],
        team=request_body["team"],
        mass_kg=request_body["mass_kg"]
    )

    db.session.add(new_car)
    db.session.commit()

    return {
        "id": new_car.id
    }, 201

@cars_bp.route("", methods=["GET"])
def get_all_cars():
    response = []
    cars = Car.query.all()
    for car in cars:
        response.append(
            {
                "id": car.id,
                "driver": car.driver,
                "team": car.team,
                "mass_kg": car.mass_kg
            }
        )
    return jsonify(response)

# @cars_bp.route("/<car_id>", methods=["GET"])
# def get_one_car(car_id):
#     try:
#         car_id = int(car_id)
#     except ValueError:
#         return jsonify({'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}), 400

#     chosen_car = None
#     for car in cars:
#         if car.id == car_id:
#             chosen_car = {
#                 "id": car.id,
#                 "driver": car.driver,
#                 "team": car.team,
#                 "mass_kg": car.mass_kg
#             }

#     if chosen_car is None:
#         return jsonify({'msg': f'Could not find car with id {car_id}'}), 404

#     return jsonify(chosen_car)
    

