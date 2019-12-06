from flask import Blueprint, jsonify, request, g, abort
from flask_login import current_user, login_required
from models import Order
from app import db, app
orders = Blueprint("orders", __name__)

@orders.route("/", methods=["GET"])
def index():
    return jsonify(list(map(lambda x: x.jsonify(), current_user.orders)))


@orders.route("/", methods=["POST"])
def create():
    order = request.get_json().get("order")
    order = Order(user_id=current_user.id, name=order.get("name"))
    db.session.add(order)
    db.session.commit()
    return jsonify({"order": order.jsonify()})


@orders.route("/<order_id>", methods=["GET"])
def show(order_id):
    o = Order.query.get(int(order_id))
    return jsonify({"user": o.user.jsonify(), "order": o.jsonify()})


@orders.before_request
@login_required
def requirelogin():
    pass


app.register_blueprint(orders, url_prefix="/orders")