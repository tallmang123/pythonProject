from app import api
from flask_restx import fields, Resource, reqparse
from project.service.accountService import AccountService

#response 형태 정의하여 marshal_with에 실어 보내면 자동으로 해당 정의 형태로 가공됨.
model = api.model('Model', {
    'uri': fields.Url('block'),
    'Seq': fields.Integer,
    'Id': fields.String,
    'Status': fields.String
})


@api.route('/block')
class Block(Resource):
    @api.marshal_with(model)  # response
    def get(self, **kwargs):
        return AccountService().getAccountInfo()

    # @api.expext(model) # request
    @api.marshal_with(model)  # response
    def post(self):
        pass
