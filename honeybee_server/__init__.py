import os
from flask import Flask, session

from .tasks import make_celery

flask_app = Flask(__name__)

from . import views
from . import config

celery = make_celery(flask_app)

flask_app.logger.info('>>> {}'.format(flask_app.config['MODE']))

# Add logger
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.INFO)
# app.logger.addHandler(stream_handler)

# @celery.task()
# def add_together(a, b):
    # return a + b
