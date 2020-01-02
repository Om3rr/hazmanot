import json
from app import db
from models.product import Product

data = []
with open('c:/users/omer/scrapytut/art/items.jl') as f:
    for line in f:
        data.append(json.loads(line))

datap = {l.get("makat"): l for l in data}
datap = datap.values()
datap = [Product(ItemName=l.get("title"), ItemCode=l.get("makat"), ItemPrice=0.0, picture=l.get("img")) for l in data]
db.session.execute('''DELETE From product;''')
db.session.commit()
[db.session.add(p) for p in datap]
db.session.commit()
