from project import db, app
import re
from sqlalchemy.orm import validates


# Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer)
    book_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"

    @validates('name')
    def validate_name(self, _, value):
        if not re.match(r'^[a-zA-Z0-9\s]*$', value):
            raise ValueError("Only alphanumeric characters and spaces are allowed in the name field.")
        return value

    @validates('author')
    def validate_author(self, _, value):
        if not re.match(r'^[a-zA-Z\s]*$', value):
            raise ValueError("Only alphabetic characters and spaces are allowed in the author field.")
        return value


with app.app_context():
    db.create_all()
