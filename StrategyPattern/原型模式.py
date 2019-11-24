# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 0024 11:14
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 原型模式.py
# @Software: PyCharm

# 用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
# 原型模式本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能，因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。
#
# 浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
# 深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。

import copy
from collections import OrderedDict

class Student():
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job

    def __str__(self):
        return "name:{},age:{},job:{}".format(self.name,self.age,self.job)

class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, key, obj):
        self.objects[key] = obj

    def unregister(self, key):
        del self.objects[key]

    def clone(self, key, **attr):
        found = self.objects.get(key)
        if not found:
            raise ValueError('Incorrect object key: {}'.format(key))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    s1=Student("tom",18,"Student")
    prototype = Prototype()
    key="clone1"
    prototype.register(key, s1)

    s2=prototype.clone(key,name="tom2",age=20,job="Student2")
    s3 = prototype.clone(key, name="tom3")
    for s in (s1,s2,s3):
        print(s)
    print("ID s1 : {} != ID s2 : {}".format(id(s1), id(s2)))
    print("ID s1 : {} != ID s3 : {}".format(id(s1), id(s3)))



if __name__ == '__main__':
    main()


# name:tom,age:18,job:Student
# name:tom2,age:20,job:Student2
# name:tom3,age:18,job:Student
# ID s1 : 2376008359816 != ID s2 : 2376008388744
# ID s1 : 2376008359816 != ID s3 : 2376008388872

