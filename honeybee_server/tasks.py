from . import celery, flask_app

@celery.task()
def process_job(filepath):
    import time
    time.sleep(10)
    print('Done Processing')


class Job():

    def __init__(self, job_filepath):
        self.job_filepath = job_filepath

    def run(self):
        process_job(self.job_filepath)


@flask_app.route('/long')
def long():
    process_job.delay('asdasd')
    return 'Response'
