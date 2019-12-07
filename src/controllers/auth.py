from flask import Blueprint, jsonify, request, redirect
from app import app, db, client
from helpers.google_auth import get_google_provider_cfg, get_google_user
from flask_login import login_user
from models import User
import os

auth = Blueprint('auth', __name__)

@auth.route("/test")
def test():
    return jsonify(os.environ.get("GOOGLE_CLIENT_ID", None))
@auth.route('/login')
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg.get("authorization_endpoint")
    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@auth.route("/login/callback")
def callback():
    g_user = get_google_user(request)
    if not g_user: return jsonify({"error": "Unauthorized"})
    user = User.query.filter_by(id_=g_user.get("id_")).first() or User(id_=g_user.get("id_"))
    user.profile_pic = g_user.get("profile_pic")
    user.google_token = g_user.get("google_token")
    user.username = g_user.get("username")
    db.session.add(user)
    db.session.flush()
    login_user(user, remember=True)
    return redirect("/")


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
