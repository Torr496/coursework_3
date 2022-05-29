

from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import DirectorsService
from project.setup_db import db

directors_ns = Namespace("directors")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Get all directors"""
        page = parser.parse_args().get("page")
        if page:
            return DirectorsService(db.session).get_limit_directors(page)
        return DirectorsService(db.session).get_all_directors()


@directors_ns.route("/<int:genre_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def get(self, genre_id: int):
        """Get director by id"""
        try:
            return DirectorsService(db.session).get_item_by_id(genre_id)
        except ItemNotFound:
            abort(404, message="Director not found")
