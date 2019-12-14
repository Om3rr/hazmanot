from app import app
from controllers.auth import auth
from controllers.orders import orders
from controllers.products import products
from controllers.users import users
from controllers.home import homes

app.register_blueprint(homes, url_prefix="/")
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(products, url_prefix="/api/products")
app.register_blueprint(orders, url_prefix="/api/orders")
