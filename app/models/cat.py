from app import db

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality,
        )

    # This method "knows" how to build a Cat from a dictionary. It maps the
    # appropriate keys to the fields in our Cat. Notice, this can still result
    # in a KeyError if the dictionary is missing keys (or had typos). The Cat
    # model itself doesn't know the best way to handle these errors, so it lets
    # them escape the function (no try/except) and leaves it to the caller to
    # deal with. See make_cat_safe in cat_routes.py for one way of handling 
    # this. Further refactors are possible!

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            color=data_dict["color"],
            personality=data_dict["personality"],
        )
