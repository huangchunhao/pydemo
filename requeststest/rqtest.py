# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 17:04
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : rqtest.py
# @Software: PyCharm
from demo_requests.requeststest import HTTPUtil

ip = "172.20.0.84"
port = "13800"
txnReq_name = "/payTrade/huab/txnReq"
txnReq_url = "http://" + ip + ":" + port + txnReq_name
mchQuery_name = "/payTrade/huab/mchQuery"
mchQuery_url = "http://" + ip + ":" + port + mchQuery_name
interface_name = "/payTrade/mchProdOpenBanks"
url = "http://" + ip + ":" + port + interface_name

ht = HTTPUtil()
if __name__ == "__main__":
    # json请求
    dict = {'mchReqNo': '494283689918948192', 'mchReqTime': '2018-09-26', 'money': '2.00', 'storeCode': '006002I01',
            'customerName': 'tst', 'certNo': '158484848840404040', 'mobile': '15248404040', 'brand': '金立',
            'model': 'GN5005L金钢', 'color': 'red', 'imei': '123456789', 'fqNumber': '12', 'payCode': '6933943500082'}
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    r = ht.post_json(url=txnReq_url, json=dict, headers=headers)
    print(r.json())  # {'status': 40, 'respCode': 'PAM_0002', 'respMsg': '重复请求'}
    print(type(r.json()))  # <class 'dict'>
    print(r.headers)
    print(r.status_code)  # 200

    # 表单请求
    data = {"mchCode": "LEHE", "prodCode": "CWH"}
    rf = ht.post_form(url=url, data=data, headers=None)
    print(rf.json())  # {'respCode': '000000', 'respMsg': '请求成功'...
    print(type(rf.json()))  # <class 'dict'>
    print(rf.headers)
    print(rf.status_code)  # 200
