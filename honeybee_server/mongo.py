import os
from flask import render_template, redirect, request, url_for
from honeybee_server import flask_app
from werkzeug.utils import secure_filename
from honeybee import mongo

UPLOAD_FOLDER = '../../jobs'
ALLOWED_EXTENSIONS = set(['zip'])

flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def new_job():
    return 'Hello World'
    return render_template('index.html')

@flask_app.route('/job', methods=['GET'])
def get_all_jobs():
    jobs = mongo.db.jobs.find({})
    return render_template('jobs.html', jobs=jobs)

@flask_app.route('/job', methods=['GET'])
def get_one_job(id):
    job = mongo.db.jobs.find({'_id': id})
    if job:
        return
