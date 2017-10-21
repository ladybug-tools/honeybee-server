bash run-redis.sh &  # to run redis
celery worker -A honeybee_server.celery &  # to run celery workers
python run.py
