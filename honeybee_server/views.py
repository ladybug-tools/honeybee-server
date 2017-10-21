import os
from flask import render_template, redirect, request, url_for
from werkzeug.utils import secure_filename

from . import flask_app

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in flask_app.config['ALLOWED_EXTENSIONS']

@flask_app.route('/job/create', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files.get('file', None)
        if not file:
            return 'No file sent with request'

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], filename))
            return str(filename) + " uploaded."
    return
def new_job():
    return 'Hello World'
    return render_template('index.html')
