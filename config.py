import os


class Config(dict):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret-to-everyone'
    REDIS_URL = os.environ.get('REDIS_URL')
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
