import os
from honeybee import app


class Config(object):
    MODE = 'Config'
    DEBUG = False
    TESTING = False
    STAGING = False
    PRODUCTION = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY', str(os.urandom(10)))
    # ASSETS_DEBUG = True if os.getenv('ASSETS_DEBUG') == '1' else False


class Development(Config):
    MODE = 'Development'
    DEBUG = True


class Production(Config):
    MODE = 'Production'

flask_config = os.environ.get('FLASK_CONFIG', 'Development')
app.config.from_object('honeybee.config.{}'.format(flask_config))
