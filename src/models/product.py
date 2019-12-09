from elasticsearch_dsl import Document, Date, Keyword, Text, Search, Completion, Float
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Q
import random
import string

connections.create_connection(hosts=['localhost'])


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class Product(Document):
    ItemName = Text()
    ItemCode = Text()
    ItemPrice = Float()
    title = Text()
    title_suggest = Completion()
    description = Text(analyzer='snowball')
    tags = Keyword()
    created_at = Date()

    class Index:
        name = "products"
        settings = {
            "number_of_shards": 2,
        }

    @staticmethod
    def generate_new():
        for i in range(1, 1000):
            p = Product(meta={"id": i}, title=randomString(10), tags=[randomString(3) for i in range(4)])
            p.save()

    @staticmethod
    def q(query):
        s = Product.search()
        q = Q()
        for w in query.split(" "):
            q = q & (Q("wildcard", ItemCode="{}*".format(w)) | Q("wildcard", ItemName="*{}*".format(w)))
        return s.query(q).execute()

    @staticmethod
    def newProduct(title):
        p = Product(ItemName=title).save()
        print(p)
        return p

    def jsonify(self):
        return {
            "title": self.ItemName,
            "id": self.ItemCode,
            "price": self.ItemPrice,
            "created_at": self.created_at
        }
