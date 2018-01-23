from app import app, redis, slack


@app.shell_context_processor
def make_shell_context():
    return {
            'app': app,
            'redis': redis,
            'slack': slack
            }
