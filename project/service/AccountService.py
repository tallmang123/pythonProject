# 비즈니스 로직
import json

from project.vo.Account import Account
import uuid
import datetime


class AccountService:
    def __init(self):
        pass

    def getAccountInfo(self):
        # return Account.query.first()
        return Account.query.all()

    def getAccountInfoById(self, userId):
        return Account.query.filter(Account.Id == userId).all()

    def addAccount(self, userId, password):
        salt = uuid.uuid4().hex[:3]
        status = 'N'
        createDate = datetime.datetime.now()

        Account(userId, password, salt, status, createDate).insert()
        pass
