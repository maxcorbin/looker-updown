from celery import Celery
import celeryconfig


def make_celery(app):

    celery = Celery(
        app.import_name,
        broker = app.config['REDIS_URL'],
        backend = app.config['REDIS_URL'],
        include=['updown.tasks']
    )
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery
