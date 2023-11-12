from project import db, app
import re
from sqlalchemy.orm import validates


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"

    @validates('name')
    def validate_name(self, _, value):
        if not re.match(r'^[a-zA-Z\s]*$', value):
            raise ValueError("Only alphabetic characters and spaces are allowed in the name field.")
        return value

    @validates('author')
    def validate_city(self, _, value):
        if not re.match(r'^[a-zA-Z\s]*$', value):
            raise ValueError("Only alphabetic characters and spaces are allowed in the city field.")
        return value


with app.app_context():
    db.create_all()
