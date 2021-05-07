import os

from project.common.ErrorCode import ErrorCode
from project.vo.LogData import LogData
from datetime import datetime
from flask import request

import logging
import json


# 데이터 로깅
class LoggingData:

    # new : 객체가 최초 생성되어 메모리에 할당되는 시점에 실행
    # 공통 사용이므로 singleton 이용하여 할당된 메모리 공간만 사용하도록 함
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggingData, cls).__new__(cls)
        return cls.instance

    # init : 소스상에서 원하는대로 객체 생성요청하여 커스터마이징하는 경우에 실행
    # init , new 중 new가 먼저 실행되어 객체를 메모리에 할당한 후에 init 진입
    def __init__(self):
        # logging에서 기본 에러레벨은 WARNING
        # DEBUG < INFO < WARNING < ERROR < CRITICAL 순에서 WARNING 하위는 출력되지 않아서 기본 INFO로 설정
        logging.getLogger().setLevel(logging.INFO)

        log_path = '/Users/tallmang/Desktop/HIVE/pythonProject/logs'
        if not os.path.exists(log_path):
            print('*******************path error')
            os.mkdir(log_path)

    def writeApiSuccessLog(self, requestData, responseJson):

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
            logging.info(logData.__dict__)
        else:
            logging.error(logData.__dict__)

        return
