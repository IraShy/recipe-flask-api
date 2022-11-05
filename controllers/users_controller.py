from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from init import db, bcrypt
from models.user import User, UserSchema

user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("/register", methods=["POST"])
def register():
    try:
        user = User(
            email=request.json["email"],
            password=bcrypt.generate_password_hash(request.json["password"]).decode(
                "utf8"
            ),
            username=request.json.get("username"),
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=["password"]).dump(user), 201
    except IntegrityError as err:
        print(f"ERROR:\n{err}")
        return {"error": f"{err.orig}"}, 409
    except KeyError as err:
        print(f"ERROR:\n{err}")
        return {"error": f"KeyError: missing {err}"}, 400
