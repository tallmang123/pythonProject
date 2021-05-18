from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_cors import CORS
import os
import pymysql
import os
# SQLAlchemy사용하여 mysql 사용하는 경우 mysqldb형태만 인식하므로 pymysql은 해당 형태로 변환
pymysql.install_as_MySQLdb()

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# 서버 내 환경변수값을 통해 config파일 읽어들여서 설정
env = os.environ.get('SERVICE_ENV')
if env is None:
    env = 'development'
configPath = 'project/config/' + env + '.py'

# Make Flask Object
app = Flask(__name__)
app.config.from_pyfile(configPath)  # Set Config
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
# cors 이슈 해결
# 현재 뷰 내 데이터 통신시 host가 아닌 다른 url로 호출하면 브라우저에서 이를 정책상 차단하여 정상적인 통신이 이루어지지 않아 해당 모듈 사용
CORS(app)

# use flask_restx
api = Api(app)

# use SQLAlchemy
db = SQLAlchemy(app)

# project import
from project.common import *
from project.hook import *
from project.controller.api import *
