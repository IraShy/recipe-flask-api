from flask import Blueprint, request
from init import db, bcrypt
from sqlalchemy import exc
from models.occasion import Occasion, OccasionSchema

# from marshmallow import ValidationError

occasions_bp = Blueprint("occasions", __name__, url_prefix="/occasions")


@occasions_bp.route("/")
def get_occasions():
    # stmt = db.select(Occasion).order_by(Occasion.title.asc())
    stmt = db.select(Occasion)
    occasions = db.session.scalars(stmt)
    return OccasionSchema(many=True).dump(occasions)


@occasions_bp.route("/<int:id>/")
def get_one_occasion(id):
    stmt = db.select(Occasion).filter_by(id=id)
    occasion = db.session.scalar(stmt)
    return OccasionSchema().dump(occasion)


@occasions_bp.route("/", methods=["POST"])
def register():
    try:
        occasion = Occasion(
            title=request.json["title"],
        )

        db.session.add(get_occasion)
        db.session.commit()
        return OccasionSchema().dump(occasion), 201

    except TypeError as err:
        print(f"TYPE ERROR: {err.detail}")

        return {"error": f"UniqueViolation: {err.detail}"}
    #     return {"error": f"Validation Error: {err}"}, 400
    except exc.DBAPIError as err:
        print(f"------------\nDPAPIERROR: {err.__dict__}\n-----------")
        return {"error": f"Database Error: {err.orig}"}, 400
    except Exception as err:
        print(f"------------\nERROR: {err.__dict__}\n-----------")
        print(err)
        return {"error": f"Validation Error: {err}"}, 400
