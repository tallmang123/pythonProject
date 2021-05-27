from flask import request

from app import app
from project.common.LoggingData import LoggingData


# HTTP 요청이 끝나고 브라우저에 응답하기 전에 실행
@app.after_request
def after_request(response):

    # api일 때만 로깅 작업 ( response-json )
    if response.get_json() is None:
        return response

    if request.method == 'GET':
        requestData = request.query_string
    else:
        requestData = request.json

    # 요청 처리 이후 데이터 로깅 일괄 처리
    LoggingData().writeApiLog(requestData, response.get_json())

    return response


# HTTP 요청 결과가 브라우저에 응답한 다음 실행
@app.teardown_request
def teardown_request(response):
    pass
