# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 16:28
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : redis_test.py
# @Software: PyCharm
import redis

class RedisUtil:
    def __init__(self, host='localhost', port=6379, db=0,password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.__initredis()


    def __initredis(self):
        self.redis = redis.Redis(self.host, self.port, self.db,self.password)


    def getdata(self,key):
        return self.redis.get(key)

    def getkeys(self,pattern):
        return self.redis.keys(pattern=pattern)


rt=RedisUtil(host='172.20.0.98', port=6379, db=4,password='Hy77499981')
keys=rt.getkeys(pattern='*merchantVerifyCode_19999999990')
print(keys)

for key in keys:
    print(rt.getdata(key))


