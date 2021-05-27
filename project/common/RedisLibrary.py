from redis import Redis
from app import app


class RedisLibrary:
    prefix = app.config['REDIS_PREFIX_KEY']  # Redis key 앞에 넣을 값
    server_ip = app.config['REDIS_SERVER_IP']  # Redis ip
    port = app.config['REDIS_SERVER_PORT']

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RedisLibrary, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.db = Redis(self.server_ip, self.port)

    def get(self, key):
        return self.db.get(self.prefix + key)

    def set(self, key, data, expire=3600):
        return self.db.set(self.prefix + key, data, expire)

    def delete(self, key):
        return self.db.delete(self.prefix, key)
