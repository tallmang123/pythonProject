from app import app


@app.before_first_request
def before_first_request():
    pass


@app.before_request
def before_request():
    pass
