## Stuff Used
- `virtualenvwrapper` to manage dependencies during development
- `apscheduler` as the in-memory background job scheduler
- `slackclient` to post to Slack
- `flask` as the web application
- `gunicorn` as the WSGI web server

## How to Install

```
git clone git@github.com:maxcorbin/looker-updown.git
cd looker-updown
pip3 install -r requirements.txt
export FLASK_APP=updown.py
```

## How to Run

Option 1: Built-in Flask web server (not scalable)
```
flask run
```

Option 2: `gunicorn`
```
gunicorn updown:app
```

Option 3: If using Heroku to deploy
```
heroku local
```
