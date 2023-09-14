from typing import Dict, Union

from db import db

UserJSON = Dict[str, Union[int, str]]

class UserModel(db.Model):
    __tablename__ = "Details"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    occupation = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)


    def __init__(self, name: str, occupation: str, location: str):
        self.name = name
        self.occupation = occupation
        self.location = location

    def json(self) -> UserJSON:
        return {"id": self.id,
                "name": self.name,
                "occupation": self.occupation,
                "location": self.location
                }

    