import os

imports = ('updown.tasks.checks')
result_expires = os.environ.get('CELERY_RESULT_EXPIRES')
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

redis_max_connections = os.environ.get('CELERY_REDIS_MAX_CONNECTIONS')

beat_schedule = {
    'zendesk.checks': {
        'task': 'updown.tasks.checks.check_zendesk',
        'schedule': 5.0
    },
    'testservice.checks': {
        'task': 'updown.tasks.checks.check_testservice',
        'schedule': 5.0
    }
}
