from enum import Enum

# ErrorCode : Enum으로 정의하여 해당 클래스 import 하여 공통으로 사용
class ErrorCode(Enum):
    SUCCESS = (200, "Success")
    SERVER_ERROR = (500, "Server Error")
    INVALID_CODE = (999, "Invalid Error Code")

    def __init__(self, errorCode, errorMsg):
        self.errorCode = errorCode
        self.errorMsg = errorMsg
