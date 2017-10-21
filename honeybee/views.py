import os
from flask import render_template, redirect, request, url_for
from honeybee import app
from werkzeug.utils import secure_filename
from honeybee import mongo

base = app.config['BASEDIR']
UPLOAD_FOLDER = os.path.join(os.path.dirname(base),'jobs')
ALLOWED_EXTENSIONS = set(['zip'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/job/create', methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File uploaded"
def new_job():
    return 'Hello World'
    return render_template('index.html')

@app.route('/job', methods=['GET'])
def get_all_jobs():
    jobs = mongo.db.jobs.find({})
    return render_template('jobs.html', jobs=jobs)

@app.route('/job', methods=['GET'])
def get_one_job(id):
    job = mongo.db.jobs.find({'_id': id})
    if job:
        return
