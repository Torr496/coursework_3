
from project.dao.models.base import BaseMixin
from project.setup_db import db


class FavoriteMovie(BaseMixin, db.Model):
    __tablename__ = 'favorite_movies'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    movie = db.relationship("Movie")

    def __repr__(self):
        return "<FavoriteMovie>"