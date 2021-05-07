from flask_cors import cross_origin

from app import api
from flask_restx import fields, Resource, reqparse

from project.common.ErrorCode import ErrorCode
from project.service.AccountService import AccountService

# request body를 파싱하여 type 및 해당 name에 맞는 값을 자동으로 변환하여 추가함.
requestParser = reqparse.RequestParser()
requestParser.add_argument('User-Agent', type=str, location='header')  # get request header
requestParser.add_argument('id', type=str, location='json')  # get request body ( Content-type = application/json 일때만)
requestParser.add_argument('uid', type=int, location='json')
requestParser.add_argument('status', type=str, location='json')

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
    'data': fields.List(fields.Nested(reponseModel)), #data 안에 json list 형식으로 설정
})


# 아래와 같이 하나의 클래스(url)에서 전송타입(get,post,delete ... ) 등으로 기능을 구분할 경우 각 타입에 맞는 기능 정의를 명확하게 하는것이 안전함
# get은 단순 조회 , post는 데이터 업데이트 전용 용도로 보통 사용
@api.route('/auth/info')
class Auth(Resource):
    @api.marshal_with(responseBody)  # response model set
    def get(self, **kwargs):
        accountInfo = AccountService().getAccountInfo()
        print(accountInfo)
        res = {'code': ErrorCode.SUCCESS.errorCode, 'msg': ErrorCode.SUCCESS.errorMsg, 'data': accountInfo}
        print(res)
        return res

    @api.expect(requestParser)  # request body parsing
    @api.marshal_with(responseBody)  # response model set
    def post(self):
        args = requestParser.parse_args()
        userId = args['id']
        accountInfo = AccountService().getAccountInfoById(userId)
        res = {'code': ErrorCode.SUCCESS.errorCode, 'msg': ErrorCode.SUCCESS.errorMsg, 'data': accountInfo}
        return res
