# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 0013 12:28
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : blend.py
# @Software: PyCharm

#透明度

from PIL import Image

img1=Image.open('11.pmg').cpnvert(mode='RGB')
img2=Image.new('RGB',img1.size,'red')

Image.blend(img1,img2,alpha=0.5).show()