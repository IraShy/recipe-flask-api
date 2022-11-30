from init import db, ma
from marshmallow import fields, ValidationError
from sqlalchemy.orm import validates
import re


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )
    password = db.Column(
        db.String,
        nullable=False,
    )
    is_admin = db.Column(db.Boolean, default=False)

    @validates("email")
    def validate_email(self, key, email):
        regex = r"\b[A-Za-z0-9.!#$%&'*+-/=?^_`{|}~]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if re.fullmatch(regex, email):
            return email
        else:
            raise ValidationError("Invalid Email")


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password", "is_admin")
