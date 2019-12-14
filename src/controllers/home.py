from flask import Blueprint, jsonify, redirect
from app import login_manager
from flask_login import login_required
from models import User


homes = Blueprint("home", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect("home")
