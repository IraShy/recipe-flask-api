from init import db, ma
from marshmallow import fields


class Occasion(db.Model):
    __tablename__ = "occasions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)


class OccasionSchema(ma.Schema):
    class Meta:
        fields = ["id", "title"]
