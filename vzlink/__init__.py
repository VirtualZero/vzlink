from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from hashids import Hashids
from flask_migrate import Migrate
from flask_cdn import CDN
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
hashids_ = Hashids(
    salt=os.environ['HASHIDS_SALT'],
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789-_.~'
)


# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQL_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# CDN
app.config['CDN_HTTPS'] = True
app.config['CDN_DOMAIN'] = os.environ['CDN_DOMAIN']
app.config['CDN_HTTPS_ROOT'] = f'https://{app.config["CDN_DOMAIN"]}'
CDN(app)


# Assets
#app.config['FLASK_ASSETS_USE_CDN'] = True
assets = Environment(app)

js = Bundle(
    'js/materialize.min.js',
    'fontawesome/fontawesome-all.min.js',
    output='assets/vzlink.js',
    filters='jsmin'
)

css = Bundle(
    'css/style.css',
    output='assets/vzlink.css',
    filters='cssmin'
)

assets.register('vzlink_js', js)
assets.register('vzlink_css', css)


# Models
from vzlink.models.user import User
from vzlink.models.link import Link


# Routes
from vzlink.routes.api import api_routes
from vzlink.routes.main import main_routes
from vzlink.errors import errors
