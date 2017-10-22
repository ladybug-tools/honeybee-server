import os
import logging
from logging.config import dictConfig

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

LOGGER_CONFIG = {
      "version": 1,
      "disable_existing_loggers": False,
      "handlers":
      {"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
      "formatters": {
          "simple": {
              "format": "[%(levelname)s] %(message)s [%(filename)s](%(lineno)d)[%(asctime)s]",
              "datefmt": "%I:%M:%S"}},
      "loggers": {"honeybee": {"handlers": ["console"], "level": LOG_LEVEL}}}

log_levels = {50: 'CRITICAL',
              40: 'ERROR',
              30: 'WARNING',
              20: 'INFO',
              10: 'DEBUG',
              0: 'NOTSET'}

dictConfig(LOGGER_CONFIG)

log = logging.getLogger("honeybee")  # Sets Root Logger
log.info('** LOG LEVEL: {}'.format(log_levels[log.getEffectiveLevel()]))
