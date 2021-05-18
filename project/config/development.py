# MYSQL
ACCOUNT_DB_HOST = '127.0.0.1'
ACCOUNT_DB_PORT = '3306'
ACCOUNT_DB_DATABASE = 'test'
ACCOUNT_DB_USER = 'root'
ACCOUNT_DB_PASSWORD = 'flsnrtm@1234'

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + ACCOUNT_DB_USER + ':' + ACCOUNT_DB_PASSWORD + '@' + ACCOUNT_DB_HOST + ':' + ACCOUNT_DB_PORT + '/' + ACCOUNT_DB_DATABASE
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# 수정사항에 대한 TRACK
SQLALCHEMY_TRACK_MODIFICATIONS = True

# GOOGLE OAUTH2
GOOGLE_CLIENT_ID = "445186266606-8jhc86j9jor6f9igmsvvq0gda6vv9qol.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "foxWN5U-CIMlGEzkTBI4bqKX"
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
# GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")


# REDIS
REDIS_SERVER_IP = '127.0.0.1'
REDIS_SERVER_PORT = '6379'
REDIS_PREFIX_KEY = 'auth:development:'
