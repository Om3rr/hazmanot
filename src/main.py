import os
from app import app, db
from flask_login import current_user
from flask_login import login_required
import controllers
from flask import request, jsonify


@app.route("/", methods=["GET"])
@login_required
def hello():
    return "Hello {}".format(current_user.username)


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(ex)
    else:
        return ex

if __name__ == "__main__":
    app.run("0.0.0.0", os.environ.get("APP_PORT") or 5000)