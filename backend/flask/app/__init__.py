from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .config import Config

# import logging
# logging.basicConfig(level=logging.DEBUG)

app = Flask(
    __name__,
    # static_folder='/frontend/dist/static',
    # template_folder='/frontend/dist',
)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)
cors = CORS(app)

from . import models
from . import apis
from . import oauth
