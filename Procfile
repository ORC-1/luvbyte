web: gunicorn luvbyte.wsgi --log-file -
worker: celery -A luvbyte worker -l info  --pool=solo
beat: celery -A luvbte beat -l info
