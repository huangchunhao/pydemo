# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 13:51
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : dicttest.py
# @Software: PyCharm

dict={"code":123,"resp":"4565","data":{"id":5689,"io":{"is":"4587"}},"list":[1,2,3,4,5],"listd":[{"id":5689},{"id":4545},{"id":5585}]}
print(dict["code"])
print(dict["resp"])
print(dict["data"])
print(dict["data"]["id"])
print(dict["list"][0])
print(dict["list"][4])
print(dict["listd"][0]["id"])

dict["code"]=5689
print(dict)
dict["code"]="8888"
print(dict)


def getValueInDict(dict, keylist):
    value=dict[keylist[0]]
    print(value)
    keylist.remove(keylist[0])
    print(keylist)
    if keylist.__len__() >= 1 :
        return getValueInDict(value, keylist)
    else:
        print(value)
        return value



s=getValueInDict(dict,['data','io','is'])
print(s)
