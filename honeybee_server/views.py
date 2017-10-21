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
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            #return redirect(request.url)
            return 'No file sent with request'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return
def new_job():
    return 'Hello World'
    return render_template('index.html')
