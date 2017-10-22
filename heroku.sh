#!/bin/bash
celery worker -A honeybee_server.celery --loglevel=info
gunicorn honeybee_server:flask_app
