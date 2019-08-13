# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 17:02
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : requeststest.py
# @Software: PyCharm
import requests

class HTTPUtil:

    def __init__(self):
        pass

    def post_form(self,url,data=None,**kwargs):
        response = requests.post(url=url,data=data,**kwargs)
        return response

    def post_json(self,url,json=None,**kwargs):
        response = requests.post(url=url,json=json,**kwargs)
        return response

    def get(self,url,params=None, **kwargs):
        response = requests.get(url, params, **kwargs)
        return response