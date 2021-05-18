from flask import request
from flask_restx import fields
from app import api
from project.common.AuthException import AuthException
from project.common.ErrorCode import ErrorCode
from project.common.LoggingData import LoggingData

##Exception 발생시 api는 정상 응답처리 해야하므로 uri, code는 포맷에 맞게 고정
responseBody = api.model('ResponseBody', {
    'uri': fields.Url(),
    'code': fields.Integer,
    'message': fields.String  # python error message는 핸들러단에서 무조건 노출하는것으로 가공하려면 응답 필드 고정해야함
})


## ExceptionHandler : Exception발생시 해당 에러 핸들러를 통해 일괄 처리할수 있음.
@api.errorhandler(AuthException)
@api.marshal_with(responseBody)  # response model set
def serverErrorHandler(exception):
    errorCode = exception.errorCode
    errorMsg = exception.errorMsg

    if errorCode is None:
        errorCode = ErrorCode.SERVER_ERROR.errorCode

    if errorMsg is None:
        errorMsg = ErrorCode.SERVER_ERROR.errorMsg

    responseData = {'code': errorCode, 'message': errorMsg}

    # request get,post일때 body를 가져오는 함수가 달라서 분기처리
    if request.method == 'GET':
        requestData = request.param
    else:
        requestData = request.json

    LoggingData().writeApiLog(requestData, responseData)

    return responseData
