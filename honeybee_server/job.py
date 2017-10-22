from .logger import log
from celery.utils.log import get_task_logger

from . import celery
from .utils import unzip_file

task_log = get_task_logger('process_job')

@celery.task()
def process_job(filepath):
    print('Started')
    task_log.debug('Job START: {}'.format(filepath))


    task_log.debug('Unzipping...')
    unzip_file(filepath)

    task_log.debug('Job END: {}'.format(filepath))
    print('Ended')


class Job():

    def __init__(self, job_filepath):
        self.job_filepath = job_filepath

    def run(self):
        process_job.delay(self.job_filepath)

