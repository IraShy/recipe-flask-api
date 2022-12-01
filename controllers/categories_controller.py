from flask import Blueprint, request
from init import db, bcrypt
from models.category import Category, CategorySchema
from marshmallow import ValidationError

categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


@categories_bp.route("/")
def get_categories():
    # stmt = db.select(Category).order_by(Category.title.asc())
    stmt = db.select(Category)
    categories = db.session.scalars(stmt)
    return CategorySchema(many=True).dump(categories)


@categories_bp.route("/<int:id>/")
def get_one_category(id):
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    return CategorySchema().dump(category)


@categories_bp.route("/", methods=["POST"])
def register():
    try:
        category = Category(
            title=request.json["title"],
        )

        db.session.add(category)
        db.session.commit()
        return CategorySchema().dump(category), 201

    except Exception as err:
        return {"error": f"Validation Error: {err}"}, 400
