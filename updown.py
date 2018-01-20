from app import app, scheduler, services

@app.shell_context_processor
def make_shell_context():
    return {
            'app': app,
            'scheduler': scheduler,
            'services': services
            }
