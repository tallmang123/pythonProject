import os

from project.common.ErrorCode import ErrorCode
from project.vo.LogData import LogData
from datetime import datetime
from flask import request

import logging
import logging.config
import json
import os


# 데이터 로깅
class LoggingData:

    # new : 객체가 최초 생성되어 메모리에 할당되는 시점에 실행
    # 공통 사용이므로 singleton 이용하여 할당된 메모리 공간만 사용하도록 함
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggingData, cls).__new__(cls)
            # 객체 최초 생성시 log 설정 불러옴
            # logging에서 기본 에러레벨은 WARNING
            # DEBUG < INFO < WARNING < ERROR < CRITICAL 순
            dirPath = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
            config = json.load(open(dirPath + '../config/logConfig.json','r'))
            logging.config.dictConfig(config)
        return cls.instance

    # init : 소스상에서 원하는대로 객체 생성요청하여 커스터마이징하는 경우에 실행
    # init , new 중 new가 먼저 실행되어 객체를 메모리에 할당한 후에 init 진입
    def __init__(self):
        # 객체가 생성될때 log 경로 확인
        self.logger = logging.getLogger('pythonLogger')
        log_path = '/Users/tallmang/Desktop/HIVE/pythonProject/logs'
        if not os.path.exists(log_path):
            os.mkdir(log_path)

    def writeApiLog(self, requestData, responseJson):

        # 날짜 생성
        logDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 요청 url
        url = request.url

        # 응답 에러코드
        try:
            errorCode = responseJson['code']
        except:
            errorCode = ErrorCode.INVALID_CODE.errorCode

        # log data set
        logData = LogData(logDate, url, errorCode, requestData, responseJson)

        # logging
        if errorCode == ErrorCode.SUCCESS.errorCode:
            self.logger.info(logData.__dict__)
        else:
            self.logger.error(logData.__dict__)

        return
