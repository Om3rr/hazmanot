from app import db, login_manager
import uuid
from flask_login import UserMixin
import operator
from functools import reduce

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    token = db.Column(db.String, unique=True, nullable=False, default=lambda: str(uuid.uuid1()))
    google_token = db.Column(db.String)
    profile_pic = db.Column(db.String)
    id_ = db.Column(db.String)
    orders = db.relationship("Order", back_populates="user", lazy='dynamic')




    def jsonify(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "token": self.token,
            "google_token": self.google_token,
            "profile_pic": self.profile_pic,
            "products": "",
        }