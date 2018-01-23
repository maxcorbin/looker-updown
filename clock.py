from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore
from urllib.parse import urlparse
from app import app, models

redis_jobstore = urlparse(app.config['REDIS_URL'])

scheduler = BackgroundScheduler(jobstores = {
    'default': RedisJobStore(
        host=r.hostname,
        port=r.port,
        password=r.password
    )
})

@scheduler.scheduled_job('interval', seconds = 5, id = 'testservice.job')
def start_zendesk():
    Zendesk().check(post_to = slack)

@scheduler.scheduled_job('interval', seconds = 5, id = 'zendesk.job')
def start_testservice():
    TestService().check(post_to = slack)

scheduler.start()
