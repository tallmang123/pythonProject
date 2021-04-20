from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
import os
import pymysql

#SQLAlchemy사용하여 mysql 사용하는 경우 mysqldb형태만 인식하므로 pymysql은 해당 형태로 변환
pymysql.install_as_MySQLdb()

#서버 내 환경을 통해 config파일 읽어들여서 설정
env = os.environ.get('SERVICE_ENV')
if env is None:
    env = 'development'
configPath = 'project/config/'+env+'.py'

app = Flask(__name__)
app.config.from_pyfile(configPath) #Set Config

api = Api(app)
db = SQLAlchemy(app)

from project.controller.api import *
from project.controller.web import *


