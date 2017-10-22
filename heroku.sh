#!/bin/bash
celery worker -A honeybee_server.celery
gunicorn honeybee_server:flask_app
