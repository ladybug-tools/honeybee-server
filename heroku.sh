#!/bin/bash
celery worker -A honeybee_server.celery --purge
gunicorn honeybee_server:flask_app
