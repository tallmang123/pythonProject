from flask import redirect, request, url_for
from app import app
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user
)
from oauthlib.oauth2 import WebApplicationClient
from project.common.RedisLibrary import RedisLibrary
from project.vo.GoogleUser import GoogleUser

import requests
import json

login_manager = LoginManager()
login_manager.init_app(app)

# OAuth2 client setup
client = WebApplicationClient(app.config['GOOGLE_CLIENT_ID'])


@app.route("/index")
def index():
    print(current_user)
    if current_user.is_authenticated:
        return (
            "<p>{}님 어서오세요!! 로그인 되었습니다.! 당신의 이메일 : {}</p>"
            "<div><p>당신의 구글 프로필 사진 : </p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">로그아웃하기</a>'.format(
                current_user.name, current_user.email, current_user.picture
            )
        )
    else:
        return '<a class="button" href="/login">클릭해서 구글 로그인하기</a>'


@app.route("/login")
def googleLogin():
    # Google 로그인 url 가져옴
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # 위의 로그인 url에 oauth 인증시 필요한 scope, redirect_uri 를 추가하여 oauth 요청 url 정의함.
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )

    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    # 구글 oauth 인증 성공하여 code값 가져옴
    code = request.args.get("code")

    # 토큰 발급 url 가져옴
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # code값을 통한 access_token 발급
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(app.config['GOOGLE_CLIENT_ID'], app.config['GOOGLE_CLIENT_SECRET']),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    # 발급된 토큰을 이용해서 구글 유저 정보를 가져옴
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    googleId = userinfo_response.json().get("sub")
    name = userinfo_response.json().get("name")
    email = userinfo_response.json().get("email")
    picture = userinfo_response.json().get("picture")

    googleUser = GoogleUser(googleId, name, email, picture)
    RedisLibrary().set(googleId, json.dumps(googleUser, default=lambda x: x.__dict__))

    login_user(googleUser)
    # 페이지 리다이렉트
    #return redirect(url_for("index"))
    return redirect("http://localhost:3000/member")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


# 로그인했던 유저 정보를 가져옴
# 기본 정보는 레디스에 저장했지만 UserMixin 자체는 Flask를 통해 메모리레 로드되어있는 상태이므로 Flask가 구동되는한 계속해서 유지됨.
# Todo Flask가 종료되면 정보가 사라지기 때문에 처리 방식에 대한 다른 고민이 필요함
@login_manager.user_loader
def load_user(googleId):
    print('*************user_loader' + googleId)
    jsonData = RedisLibrary().get(googleId)
    if jsonData is not None:
        jsonData = json.loads(jsonData)
    return GoogleUser.as_payload(jsonData)


def get_google_provider_cfg():
    # google에서 제공하는 기본 openid 설정값들 (endpoint url) 가져옴
    return requests.get(app.config['GOOGLE_DISCOVERY_URL']).json()
