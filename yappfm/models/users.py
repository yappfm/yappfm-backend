from yappfm.models import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger(), primary_key=True)
    email = db.Column(db.String(), unique=True)
