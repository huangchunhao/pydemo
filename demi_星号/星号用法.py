# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 18:06
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 星号用法.py
# @Software: PyCharm



# 1、算术运算：
#
# * 表示乘积运算。
#
# **表示乘方运算。

print(2 * 5)

print(2 ** 5)
# 2、*号常用在list变量前。表示解析出list中可迭代的元素，传递到函数中。
fruits = ['lemon', 'pear', 'watermelon', 'tomato']

print(fruits[0], fruits[1], fruits[2], fruits[3])

print(*fruits)
# *号的这种用法使得程序变得简便。

fruits = ['lemon', 'pear', 'watermelon', 'tomato']

print(*fruits[1:], fruits[0])

# 3、*号常用在dict变量前。表示解析出dict中可迭代的values，传递到函数中。

date_info = {'year': "2020", 'month': "01", 'day': "01"}

track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}

filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(

     **date_info,

     **track_info)

print(filename)

#4、*号用在函数中接收 keyword-only的参数


def get_multiple(*keys, dictionary, default=None):

    return [

        dictionary.get(key, default)

        for key in keys

    ]

fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}

get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown')

# 5、**用在函数中将参数打包成字典

def tag(tag_name, **attributes):

    attribute_list = [

        f'{name}="{value}"'

        for name, value in attributes.items()

    ]

    return f"<{tag_name} {' '.join(attribute_list)}>"

print(tag('a', href="http://treyhunner.com"))

print(tag('img', height=20, width=40, src="face.jpg"))



def tag2(tag_name, attributes):

    attribute_list = [

        f'{name}="{value}"'

        for name, value in attributes.items()

    ]

    return f"<{tag_name} {' '.join(attribute_list)}>"


print(tag2('img', {"height":"20", "width":"40", "src":"face.jpg"}))