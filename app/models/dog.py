from app import db

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    chip = db.Column(db.String, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            breed=self.breed,
            chip=self.chip,
        )

    # See cat.py for more about why this method is here
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            breed=data_dict["breed"],
            chip=data_dict["chip"],
        )
