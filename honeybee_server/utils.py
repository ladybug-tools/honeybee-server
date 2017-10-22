import os
import uuid
import zipfile
import subprocess
import json
from flask.json import jsonify
from celery import Celery
from bson import ObjectId

from . import flask_app
from .logger import log

def make_celery(app):
    # create context tasks in celery
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

def new_uuid():
    return str(uuid.uuid4())

def unzip_file(filepath):
    filename = os.path.basename(filepath)
    folder_name = filename.split('.')[0]

    job_folderpath = os.path.dirname(filepath)
    folder_path = os.path.join(job_folderpath, folder_name)
    with zipfile.ZipFile(filepath,"r") as zip_ref:
        zip_ref.extractall(folder_path)
    return folder_path

def respond(code, message):
    response = jsonify({'message': message})
    response.status_code = code
    return response


def subprocess_cmd(command, cwd=None):
    """ Helper function to call subprocess.Popen consistently without having
    to repeat keyword settings"""
    print('CMD: ' + command)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True,
                               cwd=cwd)
    proc_stdout, errmsg = process.communicate()
    print(proc_stdout)
    if errmsg:
        print(errmsg)
    return process, proc_stdout, errmsg

def run_cmd(cmd_sh, job_folder):
    cmd_filepath = os.path.join(job_folder, cmd_sh)
    cmd_folder = os.path.dirname(cmd_filepath)

    log.info('** Cmd: {}'.format(cmd_sh))
    log.info('** Cwd: {}'.format(cmd_folder))
    process, out, errmsg = subprocess_cmd(cmd_filepath, cwd=cmd_folder)
    failed = process.returncode
    log.info('OUT: {}'.format(out))
    log.info('Failed: {}'.format(failed))
    return process

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
