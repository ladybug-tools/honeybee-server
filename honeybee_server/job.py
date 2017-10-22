import os
import sys
import json
import logging

from .logger import log
from celery.utils.log import get_task_logger
from celery import signals

from . import celery
from .utils import unzip_file, run_cmd

task_log = get_task_logger(__name__)

@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    pass

@celery.task()
def process_job(filepath):
    # sys.stdout.write('TEST!')
    # sys.stdout.flush()
    log.critical('test')
    print('Print: Job Started')
    task_log.critical('Job START: {}'.format(filepath))
    task_log.info('Unzipping...')
    job_folder = unzip_file(filepath)
    job_file = os.path.join(job_folder, 'honeybee_run.json')
    with open(job_file) as fp:
        data = json.load(fp)

    task_log.info('Opening Job: {}'.format(filepath))
    # TODO: Running only first task for now
    job = data[0]
    init_cmd = job['init'][0]
    main_cmd = job['init'][0]

    task_log.info('Running Init: {}'.format(init_cmd))
    result = run_cmd(init_cmd, job_folder=job_folder)
    task_log.info(str(result))

    task_log.debug('Job END: {}'.format(filepath))
    print('Print: Ended')


class Job():

    def __init__(self, job_filepath):
        self.job_filepath = job_filepath

    def run(self):
        process_job.delay(self.job_filepath)

