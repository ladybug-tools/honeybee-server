from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

flask_app = Flask(__name__,
                  static_folder="./dist/static",
                  template_folder="./dist")

cors = CORS(flask_app, resources={r"/api/*": {"origins": "*"}})

mongo = PyMongo(flask_app)

from . import config
from .logger import log
log.info('>>> {}'.format(flask_app.config['MODE']))

from .utils import make_celery
celery = make_celery(flask_app)

from . import views

flask_app.logger.info('>>> {}'.format(flask_app.config['MODE']))

# Add logger
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.INFO)
# app.logger.addHandler(stream_handler)

@celery.task()
def add_together(a, b):
    return a + b

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0')
