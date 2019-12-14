from flask import Blueprint, jsonify, request, g, abort
from models import Product
from app import db, app
import uuid

products = Blueprint("products", __name__)


@products.route("suggest/", methods=["GET"], defaults={'query': ''})
@products.route("suggest/<query>", methods=["GET"])
def suggest(query):
    prods = Product.q(query)
    prods = [p.to_dict() for p in prods]
    return jsonify({"products": prods})


@products.route("", methods=["POST"])
def create():
    product_raw = request.get_json()
    product = Product(ItemName=product_raw.get("title"), ItemCode=str(uuid.uuid4().int))
    print(product)
    product.save()
    return jsonify({"product": product.to_dict()})
