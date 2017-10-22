#!/bin/bash
celery worker -A honeybee_server.celery -Q random-tasks --concurrency=4 --loglevel=debug &
gunicorn honeybee_server:flask_app --log-file -
