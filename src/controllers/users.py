from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app import app
users = Blueprint("users", __name__)


@users.route("/me", methods=["GET"])
@login_required
def me():
    return jsonify({"me": current_user.jsonify()})


app.register_blueprint(users, url_prefix="/api")