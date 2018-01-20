import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret-to-everyone'
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
    # TWITTER_CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
    # TWITTER_CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]
    # TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
    # TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
