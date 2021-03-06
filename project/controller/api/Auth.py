import hashlib
import json
import requests
from http import cookies

from flask import make_response

from app import api
from flask_restx import fields, Resource, reqparse

from project.common.AuthException import AuthException
from project.common.ErrorCode import ErrorCode
from project.common.RedisLibrary import RedisLibrary
from project.service.AccountService import AccountService

requestPostParser = reqparse.RequestParser()
requestPostParser.add_argument('User-Agent', type=str, location='header')  # get request header
requestPostParser.add_argument('id', type=str, location='json')  # get request param ( get -> query string)
requestPostParser.add_argument('password', type=str, location='json')

reponseModel = api.model('ResponseModel', {
    'Seq': fields.Integer,
    'Id': fields.String,
    'Password': fields.String,
    'Salt': fields.String,
    'Status': fields.String,
    'AddTime': fields.String
})

responseBody = api.model('ResponseBody', {
    'uri': fields.Url(),
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(reponseModel)),  # data 안에 json list 형식으로 설정
})


# 아래와 같이 하나의 클래스(url)에서 전송타입(get,post,delete ... ) 등으로 기능을 구분할 경우 각 타입에 맞는 기능 정의를 명확하게 하는것이 안전함
# get =  조회 , post = 데이터 insert , put = 데이터 update , delete = 데이터 삭제
@api.route('/auth/login')
class Auth(Resource):

    @api.expect(requestPostParser)  # request body parsing
    #cookie 저장을 위해 make_response사용하게 되면 model set 이 적용되지 않아 주석처리
    #@api.marshal_with(responseBody)  # response model set
    def post(self):  # 수동 로그인
        args = requestPostParser.parse_args()
        userId = args['id']
        password = args['password']

        if not userId or not password:
            raise AuthException(ErrorCode.INVALID_PARAMETER.errorCode, ErrorCode.INVALID_PARAMETER.errorMsg)

        accountInfo = AccountService().validateAccount(userId, password)
        userSessionKey = AccountService().setAccountSession(accountInfo['Id'], accountInfo)

        res = {'code': ErrorCode.SUCCESS.errorCode, 'msg': ErrorCode.SUCCESS.errorMsg, 'data': accountInfo.as_dict()}

        # set cookie
        resp = make_response(res)
        resp.set_cookie('userID', userSessionKey)

        return resp
