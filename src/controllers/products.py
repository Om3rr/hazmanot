from flask import Blueprint, jsonify, request, g, abort
from models import Product
from app import db, app

products = Blueprint("products", __name__)


@products.route("suggest/<query>", methods=["GET"])
def suggest(query):
    products = Product.q(query)
    products = [p.to_dict() for p in products]
    return jsonify({"products": products})
