from flask import request
from flask_restx import abort, Namespace, Resource,reqparse
from project.tools.security import auth_required
from project.services import UsersService
from project.setup_db import db
from project.exceptions import ItemNotFound

users_ns = Namespace('users')
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)

@users_ns.route("/")
class UsersView(Resource):
    @users_ns.expect(parser)
    @auth_required
    @users_ns.response(200, "OK")
    def get(self):
        """Get all users"""
        page = parser.parse_args().get("page")
        if page:
            return UsersService(db.session).get_limit_users(page)
        return UsersService(db.session).get_all_users()

@users_ns.route("/<int:movie_id>")
class UsersView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Users not found")
    def get(self, user_id: int):
        """Get users by id"""
        try:
            return UsersService(db.session).get_item_by_id(user_id)
        except ItemNotFound:
            abort(404, message="User not found")

    def patch(self, user_id: int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = user_id
        if not req_json:
            abort(400, message="Bad request")
        try:
            return UsersService(db.session).update(req_json)
        except ItemNotFound:
            abort(401, message="Authorization Error")


@users_ns.route("password/<int:user_id>")
class GenreView(Resource):
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Genre not found")
    def put(self, user_id: int):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        if not req_json.get('password_1') or not req_json.get('password_2'):
            abort(400, message="Bad request")
        if not req_json.get('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update_pass(req_json)

        except ItemNotFound:
            abort(404, message="User not found")
