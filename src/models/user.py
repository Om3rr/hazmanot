from app import db, login_manager
import uuid
from flask_login import UserMixin
from flask import jsonify
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    token = db.Column(db.String, unique=True, nullable=False, default=lambda: str(uuid.uuid1()))
    google_token = db.Column(db.String)
    profile_pic = db.Column(db.String)
    id_ = db.Column(db.String)
    orders = db.relationship("Order", back_populates="user")




    def jsonify(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "token": self.token,
        }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return jsonify({"error": "Unauthorized request"})
