from project.config import BaseConfig
from project.dao.models import Genre, User, Movie, Director
from project.server import create_app, db

app = create_app(BaseConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User
    }
