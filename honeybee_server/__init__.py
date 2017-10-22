from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

flask_app = Flask(__name__,
                  static_folder="./dist/static",
                  template_folder="./dist")

cors = CORS(flask_app, resources={r"/api/*": {"origins": "*"}})


from . import config
from .logger import log
# Add logger
log.info('>>> {}'.format(flask_app.config['MODE']))

from .utils import make_celery
celery = make_celery(flask_app)

mongo = PyMongo(flask_app)

from . import views

flask_app.logger.info('>>> {}'.format(flask_app.config['MODE']))
