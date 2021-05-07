from flask import request

from app import app
from project.common.LoggingData import LoggingData


# HTTP 요청이 끝나고 브라우저에 응답하기 전에 실행
# @TODO : 특정 path를 지정할수 있는지 확인 필요.
@app.after_request
def after_request(response):
    if request.method == 'GET':
        requestData = request.query_string
    else:
        requestData = request.json
    print(requestData)
    # CORS 정책으로 인해 options 타입으로 들어오는 경우가 있어 예외처리
    # @todo : option으로 처리할수 있는지 확인 필요
    if request.method != 'OPTIONS':
        # 요청 처리 이후 데이터 로깅 일괄 처리
        LoggingData().writeApiSuccessLog(requestData, response.get_json())
    return response


# HTTP 요청 결과가 브라우저에 응답한 다음 실행
@app.teardown_request
def teardown_request(response):
    pass
