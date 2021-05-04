from project.vo.Account import Account

class AccountService:
    def __init(self):
        pass

    def getAccountInfo(self):
        return Account.query.first().as_dict()
