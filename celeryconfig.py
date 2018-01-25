from os.environ import get
from datetime import timedelta

FIVE_MIN = timedelta(minutes=5)
FIVE_SEC = timedelta(seconds=5)

imports = ('updown.tasks.checks')
timezone = 'UTC'
accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

result_expires = int(get('CELERY_RESULT_EXPIRES').strip() or FIVE_MIN)
redis_max_connections = int(get('CELERY_REDIS_MAX_CONNECTIONS').strip() or 20)
broker_pool_limit = int(get('CELERY_BROKER_POOL_LIMIT').strip() or 10)
worker_concurrency = int(get('CELERY_WORKER_CONCURRENCY').strip() or 6)

beat_schedule = {
    'zendesk.checks': {
        'task': 'updown.tasks.checks.check_zendesk',
        'schedule': FIVE_SEC
    },
    'testservice.checks': {
        'task': 'updown.tasks.checks.check_testservice',
        'schedule': FIVE_SEC
    }
}
