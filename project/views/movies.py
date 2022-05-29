
from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import MoviesService
from project.setup_db import db
from project.tools.security import auth_required

movie_ns = Namespace("movies")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('page', type=str)


@movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.expect(parser)
    @auth_required
    @movie_ns.response(200, "OK")
    def get(self):
        """Get all movies"""
        req_args = parser.parse_args()
        if any(req_args.values()):
            return MoviesService(db.session).get_filter_movies(req_args)
        else:
            return MoviesService(db.session).get_all_movies()


@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @auth_required
    @movie_ns.response(200, "OK")
    @movie_ns.response(404, "Genre not found")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
