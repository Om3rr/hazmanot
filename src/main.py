import os
from app import app, db
from flask_login import current_user
import controllers


@app.route("/", methods=["GET"])
def hello():
    return "Hello {}".format(current_user.username)

if __name__ == "__main__":
    app.run("0.0.0.0", os.environ.get("APP_PORT") or 5000)