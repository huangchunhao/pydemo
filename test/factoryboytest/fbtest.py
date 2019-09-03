# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 16:51
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : fbtest.py
# @Software: PyCharm
import factory
import pprint
from demo_factory_boy.fbfactory.userfc import UserFactory



# def todict(obj):
#     data = {}
#     for key, value in obj.__dict__.items():
#         try:
#             if isinstance(value, dict):
#                 for k, v in value.items():
#                     if isinstance(value, (str,int)):
#                         data[k]=(value)
#                     else:
#                         data[key] = todict(value)
#             elif isinstance(value, tuple):
#                 for i in range(len(value)):
#                     if isinstance(value[i], (str, int)):
#
#                     todict(value[i])
#         except AttributeError:
#             data[key] = value
#     return data

def objecttodict(obj):
    dict_o=obj.__dict__
    for key, value in dict_o.items():
        print(key,type(value))
        if isinstance(value, (str,int)):#不处理str,int的情况
            pass
        elif value is None:
            pass
        elif isinstance(value, list):#处理list的情况
            valuelist=[]
            for l in value:
                if isinstance(l, (str,int)):
                    valuelist.append(l)
                else:
                    valuelist.append(objecttodict(l))
            dict_o[key] = valuelist
        elif isinstance(value, dict):
            pass#不处理dict的情况
        else:#处理普通对象
            dict_o[key]=objecttodict(value)
    return dict_o




if __name__ == "__main__":
    # 单个生成
    seq = []
    uf = UserFactory()
    print(uf.__dict__)
    seq.append(uf.__dict__)
    seq.append(UserFactory().__dict__)
    print(seq)

    ##批量生成
    listf = []
    fss = factory.build_batch(UserFactory, 4)
    for fs in fss:
        listf.append(fs.__dict__)
    print(listf)
    ##部分字段修改
    uff = UserFactory(shipped=True)

    print(uff.school.__dict__)
    print(uff.__dict__)
    print(uff.__dir__())
    #print(pprint.pprint(uff.__dict__))


    print(objecttodict(UserFactory(name='')))


#https://www.jb51.net/article/116869.htm
#https://blog.csdn.net/tz_zs/article/details/100044487

