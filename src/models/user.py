from app import db, login_manager
import uuid
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    token = db.Column(db.String, unique=True, nullable=False, default=lambda: str(uuid.uuid1()))
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
