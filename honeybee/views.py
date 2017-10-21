from flask import render_template, redirect, request, url_for
from honeybee import app

@app.route('/job/create')
def new_job():
    return 'Hello World'
    return render_template('index.html')


