import os
from datetime import timedelta

imports = ('updown.tasks.checks')
result_expires = int(os.environ.get('CELERY_RESULT_EXPIRES')) or 15
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

redis_max_connections = int(os.environ.get('CELERY_REDIS_MAX_CONNECTIONS')) or 20
broker_pool_limit = int(os.environ.get('CELERY_BROKER_POOL_LIMIT')) or 10

beat_schedule = {
    'zendesk.checks': {
        'task': 'updown.tasks.checks.check_zendesk',
        'schedule': timedelta(seconds = 5.0)
    },
    'testservice.checks': {
        'task': 'updown.tasks.checks.check_testservice',
        'schedule': timedelta(seconds = 5.0)
    }
}
