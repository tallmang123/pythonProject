class AuthException(Exception):
    errorCode = None
    errorMsg = None

    def __init__(self, errorCode, errorMsg):
        self.errorCode = errorCode
        self.errorMsg = errorMsg
