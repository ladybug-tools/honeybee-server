import os
from flask import Flask, session
from flask_pymongo import PyMongo

# from flask import Flask, session
# import logging
# from flask_restful import Api
app = Flask(__name__)
mongo = PyMongo(app)
# app_api = Api(app)

from honeybee import config
from honeybee import views
# from honeybee import assets

# app.logger.info('>>> {}'.format(app.config['MODE']))

# Add logger
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.INFO)
# app.logger.addHandler(stream_handler)

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/vinceprignano/chatapp
