from . import app

@app.route('/')
@app.route('/index')
def index():
    return 'Looker UpDown is Up!'
