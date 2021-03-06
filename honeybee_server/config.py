import os
from . import flask_app


class Config(object):
    MODE = 'Config'
    DEBUG = False
    TESTING = False
    STAGING = False
    PRODUCTION = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY', str(os.urandom(10)))
    # ASSETS_DEBUG = True if os.getenv('ASSETS_DEBUG') == '1' else False

    JOBS_FOLDER = os.path.join(os.path.dirname(BASEDIR),'jobs')
    ALLOWED_EXTENSIONS = set(['zip', 'json'])

class Development(Config):
    MODE = 'Development'
    DEBUG = True
    REDIS_URL = 'redis://localhost:6379'
    CELERY_BROKER_URL = CELERY_RESULT_BACKEND = REDIS_URL

class Production(Config):
    MODE = 'Production'
    DEBUG = True
    REDIS_URL = os.environ.get('REDIS_URL')
    CELERY_BROKER_URL = CELERY_RESULT_BACKEND = REDIS_URL
    # MONGO_PORT = 29315
    MONGO_URI = os.environ.get('MONGODB_URI')


flask_config = os.environ.get('FLASK_CONFIG', 'Development')
flask_app.config.from_object('honeybee_server.config.{}'.format(flask_config))
