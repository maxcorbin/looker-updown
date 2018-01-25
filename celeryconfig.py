

imports = ('updown.tasks.checks')
result_expires = 30
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

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
