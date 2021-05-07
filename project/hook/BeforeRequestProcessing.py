from flask import request

from app import app


# application 기동 이후 맨 처음 들어오는 HTTP 요청에서만 실행
@app.before_first_request
def before_first_request():
    pass


# HTTP요청이 들어올때마다 실행
@app.before_request
def before_request():
    pass
