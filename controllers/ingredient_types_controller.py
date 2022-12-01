from flask import Blueprint, request
from init import db, bcrypt
from sqlalchemy import exc
from models.ingredient_type import IngredientType, IngredientTypeSchema

# from marshmallow import ValidationError

ingr_types_bp = Blueprint("ingr_types", __name__, url_prefix="/ingr_types")


@ingr_types_bp.route("/")
def get_ingredient_types():
    # stmt = db.select(IngredientType).order_by(IngredientType.title.asc())
    stmt = db.select(IngredientType)
    ingr_types = db.session.scalars(stmt)
    return IngredientTypeSchema(many=True).dump(ingr_types)


@ingr_types_bp.route("/<int:id>/")
def get_one_ingredient_type(id):
    stmt = db.select(IngredientType).filter_by(id=id)
    ingr_type = db.session.scalar(stmt)
    return IngredientTypeSchema().dump(ingr_type)


@ingr_types_bp.route("/", methods=["POST"])
def register():
    try:
        ingr_type = IngredientType(
            title=request.json["title"],
        )

        db.session.add(ingr_type)
        db.session.commit()
        return IngredientTypeSchema().dump(ingr_type), 201

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
