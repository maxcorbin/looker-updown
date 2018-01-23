import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret-to-everyone'
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
    REDIS_URL = os.environ.get('REDIS_URL')
