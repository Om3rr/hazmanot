import json
from app import db
from models.product import Product

data = []
with open('c:/users/omer/scrapytut/art/items.jl') as f:
    for line in f:
        data.append(json.loads(line))

datap = {l.get("makat"): l for l in data}
datap = datap.values()
datap = [Product(ItemName=l.get("title"), ItemCode=l.get("makat"), ItemPrice=0.0, picture=l.get("img")) for l in datap]
db.session.execute('''DELETE From product;''')
db.session.commit()
for k in range(0, len(datap), 100):
    print("k is ", k)
    [db.session.add(p) for p in datap[k:k+100]]
    db.session.commit()
