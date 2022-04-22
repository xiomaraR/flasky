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

