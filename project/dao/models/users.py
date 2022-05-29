
from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(155), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(155), nullable=True)
    surname = db.Column(db.String(155), nullable=True)
    favorite_genre = db.Column(db.String(155), nullable=True)

    def __repr__(self):
        return f"<User '{self.title.title()}'>"

