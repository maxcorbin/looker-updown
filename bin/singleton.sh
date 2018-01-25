gunicorn updown:app

celery -A updown.celery beat \
--schedule=/tmp/celery-schedule \
--pidfile=/tmp/celerybeat.pid \
--loglevel=INFO

celery -A updown.celery worker \
--loglevel=INFO
