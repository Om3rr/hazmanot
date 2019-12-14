import os
from app import app, db
from flask_login import current_user
from flask_login import login_required
import controllers
import requests
from flask import request, jsonify, render_template

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(ex)
    else:
        return ex

if __name__ == "__main__":
    app.run("0.0.0.0", os.environ.get("APP_PORT") or 5000)