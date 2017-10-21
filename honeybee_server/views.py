import os
from flask import render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
from flask.json import jsonify
from . import flask_app
from .utils import new_uuid, unzip_file

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in flask_app.config['ALLOWED_EXTENSIONS']

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
			# create a new record in the DB with UUID
			return str(filename) + " uploaded. jobId is " +jobId
	return

@flask_app.route('/job/<uuid:jobId>')
def send_response(jobId):
	return jsonify(
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
		#return str(jobId)
