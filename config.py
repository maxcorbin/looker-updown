import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') || 'its-a-secret-to-everyone'
    DATASTORE_PATH = os.environ.get('DATASTORE_PATH') || \
        os.path.join(basedir, 'updates.json')
