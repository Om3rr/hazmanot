from flask import Blueprint, jsonify, request, redirect
from app import app, db, client
from helpers.google_auth import get_google_provider_cfg, get_google_user, validate_with_token
from flask_login import login_user, logout_user, login_required, current_user
from models import User
import os

auth = Blueprint('auth', __name__)

@auth.route("/token", methods=["POST"])
def token():
    token = request.get_json().get("token")
    g_user = validate_with_token(token)
    user = User.query.filter_by(email=g_user.get("email")).first()
    user = user or User()
    user.email = g_user.get("email")
    user.profile_pic = g_user.get("picture")
    user.google_token = token
    user.username = g_user.get("name")
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    login_user(user, remember=True)
    return jsonify(user.jsonify())


@auth.route('/logout')
def logout():
    logout_user()
    return redirect("/")