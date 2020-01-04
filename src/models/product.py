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
    ItemCode = db.Column(db.String(16))
    ItemPrice = db.Column(db.Float(16))
    ItemName = db.Column(db.String(32))
    picture = db.Column(db.Text)

    @staticmethod
    def q(query, user=None) -> List['Product']:
        qq = [Product.ItemName.like("%{q}%".format(q=q)) for q in query.split(" ")]
        return sorted(db.session.query(Product).filter(db.and_(*qq)).all(), key=lambda p: Product.score_result(p, query, user), reverse=True)[0:50]

    @staticmethod
    def score_result(product, query, user=None):
        if len(query) < 1: return 0
        score = 0
        splitted_item_name = product.ItemName.split(" ")
        for w in query.split(" "):
            if w in splitted_item_name: score += len(w)
            for ww in splitted_item_name:
                if ww.startswith(w): score += len(w)
        #print(product.ItemName, query, score)
        return score




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
            "ItemImage": self.picture,
            "id": self.id
        }
