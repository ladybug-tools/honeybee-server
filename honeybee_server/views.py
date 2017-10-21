import os
from flask import render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
from flask.json import jsonify
from . import flask_app
from .utils import new_uuid

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in flask_app.config['ALLOWED_EXTENSIONS']

# create a job
@flask_app.route('/job/create', methods=['POST'])
def upload_file():
	if request.method == 'POST':

		jobId = new_uuid()

		file = request.files.get('file', None)
		if not file:
			return 'No file sent with request'

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			os.mkdir(os.path.join(flask_app.config['UPLOAD_FOLDER'], jobId))
			filepath = os.path.join(flask_app.config['UPLOAD_FOLDER'],jobId)
			file.save(os.path.join(filepath,'job.zip'))
            # TODO: create a new record in the DB with UUID
			return str(filename) + " uploaded. jobId is " +jobId
	return

# get job data or delete a job
@flask_app.route('/job/<uuid:jobId>', methods=['GET','DELETE'])
def job(jobId):
    if request.method == 'DELETE':
        #logic to halt radiance running this job and delete it from server
        return jobId + " has been deleted"

    if requets.method == 'GET':
        #log to send back completed job data
        return jobId + "'s data goes here"

# get a job's status
@flask_app.route('/job/<uuid:jobId>/status')
def job_status(jobId):
    return jsonify(
        #placeholder info for Mingbo
		{
			"JobId": str(jobId),
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
@flask_app.route('/job/<uuid:jobId>/<taskId>')
def get_task(taskId):
    #logic to send back task data
    return taskId

# delete a task
@flask_app.route('/job/<uuid:jobId>/<taskId>', methods=['DELETE'])
def delete_task(taskId):
    #logic to halt radiance running this task
    return taskId + " has been deleted"

