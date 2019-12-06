from app import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String)
    user = db.relationship("User", back_populates="orders")




    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name
        }