from flask import Blueprint, jsonify
from app import app, db
from flask_login import login_user
from models import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'Login'


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route("/login/<user_id>", methods=["GET"])
def sign_in(user_id):
    u = User.query.get(int(user_id))
    login_user(u, remember=True)
    return jsonify(u.jsonify())


app.register_blueprint(auth, url_prefix="")
