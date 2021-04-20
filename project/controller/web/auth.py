from app import app, render_template
from project.service.accountService import AccountService


class Auth:
    def __init__():
        pass

    @app.route('/first')
    def first():
        print('test')
        print(AccountService().getAccountInfo().__dict__)
        return render_template("index.html")

    @app.route('/second')
    def second(self):
        print('')
        print(AccountService().getAccountInfo().__dict__)
        return render_template("index.html")

    @app.route('/app')
    def app():
        print('test')
        print(AccountService().getAccountInfo().__dict__)
        return render_template("index.html")
