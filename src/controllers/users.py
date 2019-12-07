from flask import Blueprint, jsonify, request
from app import app, db

from models import User

users = Blueprint("users", __name__)



@users.route("/", methods=["GET"])
def index():
    return jsonify(list(map(lambda x: x.jsonify(), User.query.all())))


@users.route("/", methods=["POST"])
def create():
    user = request.get_json()["user"]
    print("Hey")
    print(user["username"])
    u = User(username=user["username"], email=user["email"])
    db.session.add(u)
    db.session.commit()
    return jsonify(u.jsonify())
