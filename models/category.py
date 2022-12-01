from init import db, ma
from marshmallow import fields


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)


class CategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "title")
