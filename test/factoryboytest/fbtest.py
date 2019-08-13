# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 16:51
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : fbtest.py
# @Software: PyCharm
import factory
from demo_factory_boy.fbfactory.userfc import UserFactory

if __name__ == "__main__":
    #单个生成
    seq = []
    uf = UserFactory()
    print(uf.__dict__)
    seq.append(uf.__dict__)
    seq.append(UserFactory().__dict__)
    print(seq)

##批量生成
    list = []
    fss = factory.build_batch(UserFactory, 4)
    for fs in fss:
        list.append(fs.__dict__)
    print(list)
##部分字段修改
    uff = UserFactory(shipped=True)
    print(uff.school.__dict__)
    print(uff.__dict__)
    print(uff.__dir__())