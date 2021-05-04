class LogData:
    logDate = None
    url = None
    errorCode = None
    request = None
    response = None

    def __init__(self, logDate, url, errorCode, request, response):
        self.logDate = logDate
        self.url = url
        self.errorCode = errorCode
        self.request = request
        self.response = response
