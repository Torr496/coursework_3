from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from config import DevelopmentConfig
from setup_db import db
from views import genres_ns
from views import directors_ns
from views import users_ns
from views import auth_ns
from views import movie_ns


api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)

# Нужно для работы с фронтендом
cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)

    return app


app = create_app(DevelopmentConfig())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
