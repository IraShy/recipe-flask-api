from flask import Flask
import os
from init import db, ma
from commands import db_commands
from controllers.users_controller import user_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(user_bp)

    return app
