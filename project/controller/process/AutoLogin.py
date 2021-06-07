import json

import requests
from flask import request, redirect, make_response
from app import app

from project.common.RedisLibrary import RedisLibrary


# 자동 로그인
@app.route('/autoLogin')
def autoLogin():

    userSessionKey = request.cookies.get('userID')
    print(userSessionKey)
    if userSessionKey is None:
        return redirect("/login")

    userSession = RedisLibrary().get(userSessionKey)
    if userSession is None:
        return redirect("/login")
    ###################################
    #Todo : 유저 검증 방식이 대한 로직 점검 필요
    ###################################
    data = json.loads(userSession.decode('utf8'))

    # set cookie
    resp = make_response(redirect("/member"))
    #resp.set_cookie('userID222', userSessionKey)

    return resp
