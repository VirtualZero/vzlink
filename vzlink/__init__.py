from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from hashids import Hashids
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
hashids_ = Hashids(
    salt=os.environ['HASHIDS_SALT'],
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789-_.~'
)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQL_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Models
from vzlink.models.user import User
from vzlink.models.link import Link


# Routes
from vzlink.routes.api import api_routes
from vzlink.routes.main import main_routes
from vzlink.errors import errors
