import os
import sys
import json
import logging

from .logger import log
# from celery import signals
# from celery.utils.log import get_task_logger

from . import celery, mongo
from .utils import unzip_file, run_cmd


# @signals.setup_logging.connect
# def on_celery_setup_logging(**kwargs):
    # pass

# @celery.task()
def process_job(job):
    filepath = job.job_filepath
    log.info('Job START: {}'.format(filepath))

    log.info('Unzipping...')
    job_folder = unzip_file(filepath)
    job_file = os.path.join(job_folder, 'honeybee_run.json')
    with open(job_file) as fp:
        data = json.load(fp)

    log.info('Opening Job: {}'.format(filepath))
    # TODO: Running only first task for now
    job = data[0]
    init_cmd = job['init'][0]
    main_cmd = job['init'][0]

    log.info('Running Init: {}'.format(init_cmd))
    result = run_cmd(init_cmd, job_folder=job_folder)
    log.info(str(result))

    log.debug('Job END: {}'.format(filepath))
    print('Print: Ended')
    return result


def process_json(job):
    filepath, job_id = job.job_filepath, job.job_id
    log.debug('Job JSON: {}'.format(filepath))
    from .from_json import run_from_json
    with open(filepath, 'rb') as fp:
        recipe = json.load(fp)
    success, results = run_from_json(recipe, 'jobs', job_id)
    log.debug('Status: {}'.format(success))
    log.debug('Job JSON DONE')

    updated_job = mongo.db.jobs.update_one(
       {"job_id": job_id},
       {
        "$set": {"status": 1, "data": json.dumps(results)}
       }
    )

    return results



class Job():

    def __init__(self, job_filepath, job_id):
        self.job_filepath = job_filepath
        self.job_id = job_id

    def run(self):
        if self.job_filepath.lower().endswith('json'):
            return process_json(self)
        elif self.job_filepath.lower().endswith('zip'):
            return process_job(self)
        # process_job.calling(self.job_filepath)

