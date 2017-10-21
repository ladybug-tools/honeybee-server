from flask import render_template, redirect, request, url_for
from honeybee import app

@app.route('/job/create', methods=['GET', 'PUT'])
def new_job():
    if request.method
    return 'Hello World'
    return render_template('index.html')


