from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv
from config.google import GOOGLE_CLIENT_ID
import os
load_dotenv()
# app = Flask(__name__,
#             static_folder = "./dist/static",
#             template_folder = "./dist")
app = Flask(__name__, static_folder = "../hazil_ui/dist/static", template_folder = "../hazil_ui/dist")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.environ.get("MYSQL_USERNAME")}:{os.environ.get("MYSQL_PASSWORD")}@{os.environ.get("MYSQL_HOST")}/hazmanot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
client = WebApplicationClient(GOOGLE_CLIENT_ID)
