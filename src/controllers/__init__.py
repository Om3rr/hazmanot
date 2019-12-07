from app import app
from controllers.users import users
from controllers.auth import auth
from controllers.orders import orders
from controllers.products import products


app.register_blueprint(products, url_prefix="/api/products")
app.register_blueprint(users, url_prefix="/api/users")
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(orders, url_prefix="/api/orders")