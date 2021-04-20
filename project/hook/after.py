from app import app


@app.after_request
def after_request():
    pass


@app.teardown_request
def teardown_request():
    pass
