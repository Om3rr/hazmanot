from app import db
from models import Product
import gzip
import xml.etree.ElementTree as ET
import requests

tarraw = requests.get("http://pricesprodpublic.blob.core.windows.net/pricefull/PriceFull7290027600007-011-201912220330.gz?sv=2014-02-14&sr=b&sig=gdnM8k9eAn9CCEqIgsJSQbxnXn741M5%2FZO4nTksyU6o%3D&se=2019-12-22T09%3A19%3A57Z&sp=r").content
root = ET.fromstring(gzip.decompress(tarraw).decode("utf-8"))
atts = ["ItemName", "ItemCode", "ItemPrice"]
items = []
for item in root.find("Items"):
    i = {}
    for a in atts:
        i[a] = item.find(a).text
    items.append(Product(**i))

[db.session.add(p) for p in items]

db.session.commit()



