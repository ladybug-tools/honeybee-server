bash run-redis.sh &  # to run redis
celery worker -A honeybee_server.celery --purge
python run.py
