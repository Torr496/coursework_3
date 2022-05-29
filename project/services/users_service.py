from flask import current_app

from project.dao import UserDAO
from project.exceptions import ItemNotFound
from project.schemas.users import UserSchema
from project.services.base import BaseService
from project.tools.security import generate_password_digest, compare_passwords


class UsersService(BaseService):
    def get_item_by_email(self, email):
        user = UserDAO(self._db_session).get_by_email(email)
        if not user:
            raise ItemNotFound
        print(user)
        return user

    def get_item_by_id(self, pk):
        user = UserDAO(self._db_session).get_by_email(pk)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_all_users(self):
        users = UserDAO(self._db_session).get_all()
        return UserSchema(many=True).dump(users)

    def get_limit_users(self, page):
        limit = current_app.config["ITEMS_PER_PAGE"]
        offset = (page - 1)*limit
        users = UserDAO(self._db_session).get_limit(limit=limit, offset=offset)
        return UserSchema(many=True).dump(users)

    def create(self, data_in):
        user_pass = data_in.get("password")
        if user_pass:
            data_in["password"] = generate_password_digest(user_pass)
        user = UserDAO(self._db_session).create(data_in)
        return "Пользователь создан"

    def update(self, data_in):
        user = UserDAO(self._db_session).update(data_in)
        return UserSchema().dump(user)

    def update_password(self, email: str, old_password: str, new_password: str) -> None:
        user = self.get_item_by_email(email)
        if not compare_passwords(password_hash=user.password, other_password=old_password):
            raise ItemNotFound
        user.password = generate_password_digest(new_password)
        UserDAO(self._db_session).update(user)








