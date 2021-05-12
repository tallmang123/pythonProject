from app import api
from flask_restx import fields, Resource, reqparse

from project.common.AuthException import AuthException
from project.common.ErrorCode import ErrorCode
from project.service.AccountService import AccountService

# request query string 파싱하여 type 및 해당 name에 맞는 값을 자동으로 변환하여 추가함. ( GET )
requestGetParser = reqparse.RequestParser()
requestGetParser.add_argument('User-Agent', type=str, location='header')  # get request header
requestGetParser.add_argument('id', type=str, location='args')  # get request body ( Content-type = application/json 일때)

# request body 파싱하여 type 및 해당 name에 맞는 값을 자동으로 변환하여 추가함. ( POST )
requestPostParser = reqparse.RequestParser()
requestPostParser.add_argument('User-Agent', type=str, location='header')  # get request header
requestPostParser.add_argument('id', type=str, location='json')  # get request param ( get -> query string)
requestPostParser.add_argument('password', type=str, location='json')

# argument명이 동일하고 location만 달라 중복으로 사용하는 경우에 마지막 설정값으로 덮어씌워져서 이름을 다르게하거나 별도로 만들어야함.

# response 형태 정의하여 marshal_with에 실어 보내면 자동으로 해당 정의 형태로 가공됨.
# responseModel : 실제 사용하고자 하는 데이터 가공 객체
# responseBody : 실제 응답에 필요한 데이터 가공 객체
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
@api.route('/auth/info')
class Auth(Resource):
    @api.expect(requestGetParser)  # request body parsing
    @api.marshal_with(responseBody)  # response model set
    def get(self, **kwargs):
        args = requestGetParser.parse_args()
        userId = args['id']
        if not userId:
            accountInfo = AccountService().getAccountInfo()
        else:
            accountInfo = AccountService().getAccountInfoById(userId)

        res = {'code': ErrorCode.SUCCESS.errorCode, 'msg': ErrorCode.SUCCESS.errorMsg, 'data': accountInfo}

        return res

    @api.expect(requestPostParser)  # request body parsing
    @api.marshal_with(responseBody)  # response model set
    def post(self):
        args = requestPostParser.parse_args()
        userId = args['id']
        password = args['password']

        if not userId or not password:
            raise AuthException(ErrorCode.INVALID_PARAMETER.errorCode, ErrorCode.INVALID_PARAMETER.errorMsg)

        accountInfo = AccountService().getAccountInfoById(userId)
        if accountInfo:
            raise AuthException(ErrorCode.DUPLICATED_ACCOUNT.errorCode, ErrorCode.DUPLICATED_ACCOUNT.errorMsg)

        accountInfo = AccountService().addAccount(userId, password)
        res = {'code': ErrorCode.SUCCESS.errorCode, 'msg': ErrorCode.SUCCESS.errorMsg, 'data': accountInfo}
        return res
