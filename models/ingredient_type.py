from init import db, ma
from marshmallow import fields


class IngredientType(db.Model):
    __tablename__ = "ingredient_types"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)


class IngredientTypeSchema(ma.Schema):
    class Meta:
        fields = ["id", "title"]
