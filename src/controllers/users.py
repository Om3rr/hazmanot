from flask import Blueprint, jsonify, request
from app import app, db

from models import User

users_controller = Blueprint("users", __name__)



@users_controller.route("/", methods=["GET"])
def index():
    return jsonify(list(map(lambda x: x.jsonify(), User.query.all())))


@users_controller.route("/", methods=["POST"])
def create():
    user = request.get_json()["user"]
    print("Hey")
    print(user["username"])
    u = User(username=user["username"], email=user["email"])
    db.session.add(u)
    db.session.commit()
    return jsonify(u.jsonify())

app.register_blueprint(users_controller, url_prefix='/users')