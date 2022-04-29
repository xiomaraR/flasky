from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver = db.Column(db.String)
    team = db.Column(db.String)
    mass_kg = db.Column(db.Integer)

# class Car:
#     def __init__(self, id, driver, team, mass_kg):
#         self.id = id
#         self.driver = driver
#         self.team = team
#         self.mass_kg = mass_kg

# cars = [
#     Car(7, "Sainz", "Ferrari", 795),
#     Car(88, "SHARLES", "Ferrari", 800),
#     Car(4, "Danny Ric", "McLaren", 1138)
# ]