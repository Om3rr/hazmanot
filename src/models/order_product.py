from app import db
class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    amount = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    order = db.relationship("Order", back_populates="order_products")

    @property
    def total_price(self):
        return self.amount * self.unit_price

    def jsonify(self):
        return {
            "product": "...",
            "order_id": self.order_id,
            "amount": self.amount,
            "unit_price": self.unit_price,
            "total_price": self.total_price
        }
