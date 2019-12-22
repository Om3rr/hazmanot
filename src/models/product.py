from app import db, login_manager
from sqlalchemy import or_
import random
import string
from typing import List


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ItemCode = db.Column(db.Text)
    ItemPrice = db.Column(db.Float)
    ItemName = db.Column(db.Text)

    @staticmethod
    def q(query) -> List['Product']:
        qq = [Product.ItemName.like("%{q}%".format(q=q)) for q in query.split(" ")]
        return db.session.query(Product).filter(db.and_(*qq)).limit(20).all()

    @staticmethod
    def newProduct(title):
        p = Product(ItemName=title).save()
        print(p)
        return p

    def jsonify(self):
        return {
            "ItemName": self.ItemName,
            "ItemCode": self.ItemCode,
            "ItemPrice": self.ItemPrice,
        }
