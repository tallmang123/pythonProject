# 비즈니스 로직

from project.vo.Account import Account


class AccountService:
    def __init(self):
        pass

    def getAccountInfo(self):
        # return Account.query.first()
        return Account.query.all()

    def getAccountInfoById(self, userId):
        return Account.query.filter(Account.Id == userId).all()
