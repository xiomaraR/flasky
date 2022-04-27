from flask import Blueprint, jsonify

class Car:
    def __init__(self, id, driver, team, mass_kg):
        self.id = id
        self.driver = driver
        self.team = team
        self.mass_kg = mass_kg

cars = [
    Car(7, "Sainz", "Ferrari", 795),
    Car(88, "SHARLES", "Ferrari", 800),
    Car(4, "Danny Ric", "McLaren", 1138)
]

cars_bp = Blueprint("cars", __name__, url_prefix="/cars")

@cars_bp.route("", methods=["GET"])
def get_all_cars():
    response = []
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

@cars_bp.route("/<car_id>", methods=["GET"])
def get_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}), 400

    chosen_car = None
    for car in cars:
        if car.id == car_id:
            chosen_car = {
                "id": car.id,
                "driver": car.driver,
                "team": car.team,
                "mass_kg": car.mass_kg
            }

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404

    return jsonify(chosen_car)
    

