from flask import Blueprint, jsonify, request, g, abort
from models import Product
from app import db, app
import uuid

products = Blueprint("products", __name__)


@products.route("suggest/", methods=["GET"], defaults={'query': ''})
@products.route("suggest/<query>", methods=["GET"])
def suggest(query):
    products = Product.q(query)
    products = [p.to_dict() for p in products]
    return jsonify({"products": products})

@products.route("", methods=["POST"])
def create():
    product_raw = request.get_json()
    product = Product(ItemName=product_raw.get("title"), ItemCode=uuid.uuid4().int)
    print(product)
    product.save()
    return jsonify({"product": product.to_dict()})
