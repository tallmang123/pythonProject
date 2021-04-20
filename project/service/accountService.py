from project.vo.Account import Account


class AccountService:
    def __init(self):
        pass

    def getAccountInfo(self):
        print('getAccountInfo')
        return Account.query.first()
