from app import db

class Cat(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String)
  personality = db.Column(db.String)
  breed = db.Column(db.String)
  age = db.Column(db.Integer)
  toe_beans = db.Column(db.Integer, default=16)

  def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "personality": self.personality,
            "breed": self.breed,
            "age": self.age,
            "toe_beans": self.toe_beans
        }
  
  def update(self,req_body):
    self.name = req_body["name"]
    self.personality = req_body["personality"]
    self.breed = req_body["breed"]
    self.age = req_body["age"]
    self.toe_beans = req_body["toe_beans"]

  @classmethod
  def create(cls,req_body):
    new_cat = cls(
        name=req_body['name'],
        personality=req_body['personality'],
        age=req_body['age'],
        breed=req_body['breed']
    )
    return new_cat