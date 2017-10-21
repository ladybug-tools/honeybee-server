import os
from flask import render_template, redirect, request, url_for, abort
from werkzeug.utils import secure_filename
from flask.json import jsonify

from . import flask_app
from .utils import new_uuid, unzip_file, respond
from .logger import log

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in flask_app.config['ALLOWED_EXTENSIONS']

# create a job
@flask_app.route('/job/create', methods=['POST'])
def upload_file():

    job_id = new_uuid()
    log.debug('Job Received: {}'.format(job_id))

    file = request.files.get('file', None)
    if not file:
    	return respond(400, 'No file sent with request')

    if not allowed_file(file.filename):
        return respond(400, 'Invalid file type: {}'.format(filename))

    jobs_folder = flask_app.config['JOBS_FOLDER']

    filename = secure_filename(file.filename)
    folder_path = os.path.join(jobs_folder, job_id)
    os.mkdir(folder_path)
    filepath = os.path.join(folder_path,'job.zip')
    file.save(filepath)

    # TODO: create a new record in the DB with UUID
    msg = "{} uploaded. job_id is {}".format(filename, job_id)
    return respond(201, msg)

# get job data or delete a job
@flask_app.route('/job/<uuid:job_id>', methods=['GET','DELETE'])
def job(job_id):
    if request.method == 'DELETE':
        #logic to halt radiance running this job and delete it from server
        return job_id + " has been deleted"

    if requets.method == 'GET':
        #log to send back completed job data
        return job_id + "'s data goes here"

# get a job's status
@flask_app.route('/job/<uuid:job_id>/status')
def job_status(job_id):
    return jsonify(
        #placeholder info for Mingbo
		{
			"JobId": str(job_id),
			"Simulations": [
				{
					"childId":"pkkrjle",
					"Status":"running",
					"isDone":False
				},
				{
					"childId":"udfgdfe",
					"Status":"done",
					"isDone":True
				},

			]
		})

# get a task's data
@flask_app.route('/job/<uuid:job_id>/<taskId>')
def get_task(taskId):
    #logic to send back task data
    return taskId

# delete a task
@flask_app.route('/job/<uuid:job_id>/<taskId>', methods=['DELETE'])
def delete_task(taskId):
    #logic to halt radiance running this task
    return taskId + " has been deleted"

@flask_app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
