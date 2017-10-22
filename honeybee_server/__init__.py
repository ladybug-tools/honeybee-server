from flask import Flask
from flask_pymongo import PyMongo

flask_app = Flask(__name__)
mongo = PyMongo(flask_app)

from . import config
from .logger import log
# Add logger
# flask_app.logger.addHandler(log)
log.info('>>> {}'.format(flask_app.config['MODE']))

from .utils import make_celery
celery = make_celery(flask_app)
from . import views
