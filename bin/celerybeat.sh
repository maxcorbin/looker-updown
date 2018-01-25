celery -A updown.celery beat \
--schedule=/tmp/celery-schedule \
--pidfile=/tmp/celerybeat.pid \
--loglevel=$CELERY_BEAT_LOGLEVEL
