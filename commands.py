from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.category import Category
from models.ingredient_type import IngredientType
from models.occasion import Occasion
from data import data

db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")


@db_commands.cli.command("seed")
def seed_db():
    if len(User.query.all()) == 0:
        users = [
            User(
                username="admin",
                email="admin@email.com",
                password=bcrypt.generate_password_hash("admin").decode("utf-8"),
                is_admin=True,
            ),
            User(
                username="User 1",
                email="user1@email.com",
                password=bcrypt.generate_password_hash("password").decode("utf-8"),
            ),
        ]

        db.session.add_all(users)
        db.session.commit()
        print("Users table seeded")

    # categories_data = ["breakfast", "lunch", "dinner"]

    if len(Category.query.all()) == 0:
        categories = map(lambda cat: Category(title=cat), data.categories)
        db.session.add_all(categories)
        db.session.commit()
        print("Categories table seeded")

    if len(IngredientType.query.all()) == 0:
        ingredient_types = map(
            lambda type: IngredientType(title=type), data.ingredient_types
        )
        db.session.add_all(ingredient_types)
        db.session.commit()
        print("IngredientTypes table seeded")

    if len(Occasion.query.all()) == 0:
        occasions = map(lambda type: Occasion(title=type), data.occasions)
        db.session.add_all(occasions)
        db.session.commit()
        print("Occasions table seeded")
