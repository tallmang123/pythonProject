# 비즈니스 로직
from project.common.ErrorCode import ErrorCode
from project.common.AuthException import AuthException
from project.vo.Account import Account
import uuid
import datetime
import hashlib


class AccountService:
    def __init(self):
        pass

    def getAccountInfo(self):
        # return Account.query.first()
        return Account.query.all()

    def getAccountInfoById(self, userId):
        return Account.query.filter(Account.Id == userId).first()

    def addAccount(self, userId, password):
        salt = uuid.uuid4().hex[:3]
        status = 'N'
        createDate = datetime.datetime.now()
        encPassword = hashlib.md5((password + salt).encode('utf-8')).hexdigest()
        Account(userId, encPassword, salt, status, createDate).insert()
        pass

    # get account info
    def validateAccount(self, userId, password):
        accountInfo = AccountService().getAccountInfoById(userId)
        if not accountInfo:
            raise AuthException(ErrorCode.NO_ACCOUNT.errorCode, ErrorCode.NO_ACCOUNT.errorMsg)

        if accountInfo.Status == 'B':
            raise AuthException(ErrorCode.BLOCKED_ACCOUNT.errorCode, ErrorCode.BLOCKED_ACCOUNT.errorMsg)

        encPassword = hashlib.md5((password + accountInfo.Salt).encode('utf-8')).hexdigest()

        if encPassword != accountInfo.Password:
            raise AuthException(ErrorCode.PASSWORD_MISMATCH.errorCode, ErrorCode.PASSWORD_MISMATCH.errorMsg)

        return accountInfo
