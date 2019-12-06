from flask import Blueprint, jsonify, request, g, abort
from models import Product
from app import db, app

orders = Blueprint("products", __name__)


@orders.route("suggest/<query>", methods=["GET"])
def suggest(query):
    products = Product.q(query)
    products = [p.to_dict() for p in products]
    return jsonify({"products": products})


app.register_blueprint(orders, url_prefix="/products")
