from flask import Flask
from init import db, ma
import os


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    @app.route("/")
    def index():
        return "Recipes"

    db.init_app(app)
    ma.init_app(app)

    return app
