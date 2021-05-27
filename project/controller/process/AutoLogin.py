import requests
from flask import request, redirect
from app import app

from project.common.RedisLibrary import RedisLibrary


# 자동 로그인
@app.route('/autoLogin')
def autoLogin():
    s = requests.session()
    userSessionKey = s.cookies.get("SID")
    print(userSessionKey)
    if userSessionKey is None:
        return redirect("/login")

    userSession = RedisLibrary().get(userSessionKey)
    if userSession:
        return redirect("/member")
    return redirect("/login")
