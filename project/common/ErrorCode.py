from enum import Enum

# ErrorCode : Enum으로 정의하여 해당 클래스 import 하여 공통으로 사용
# @todo : import하는 시점 고려해봐야함. 매 소스마다 import하는건 일단 비효율적인듯..
class ErrorCode(Enum):
    SUCCESS = (200, "Success")
    SERVER_ERROR = (500, "Server Error")

    def __init__(self, errorCode, errorMsg):
        self.errorCode = errorCode
        self.errorMsg = errorMsg
