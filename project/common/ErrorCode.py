from enum import Enum


# ErrorCode : Enum으로 정의하여 해당 클래스 import 하여 공통으로 사용
class ErrorCode(Enum):
    SUCCESS = (200, "Success")
    INVALID_PARAMETER = (400, "Invalid Parameter")
    SERVER_ERROR = (500, "Server Error")
    SERVICE_ERROR = (700, "Service Error")
    NO_ACCOUNT = (701, "No Account")
    DUPLICATED_ACCOUNT = (702, "Duplicated Account")
    BLOCKED_ACCOUNT = (703, "Blocked Account")
    PASSWORD_MISMATCH = (704, "Password Mismatch")
    INVALID_CODE = (999, "Invalid Error Code")

    def __init__(self, errorCode, errorMsg):
        self.errorCode = errorCode
        self.errorMsg = errorMsg
