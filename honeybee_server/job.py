import os
import sys
import json
import logging

from .logger import log
# from celery import signals
# from celery.utils.log import get_task_logger

from . import celery
from .utils import unzip_file, run_cmd


# @signals.setup_logging.connect
# def on_celery_setup_logging(**kwargs):
    # pass

# @celery.task()
def process_job(filepath):
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


class Job():

    def __init__(self, job_filepath):
        self.job_filepath = job_filepath

    def run(self):
        process_job(self.job_filepath)
        # process_job.calling(self.job_filepath)

