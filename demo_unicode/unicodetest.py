# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 10:17
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : unicodetest.py
# @Software: PyCharm
import re
content = "reason\u9ed1\u540d\u5355\u6765\u6e90\u7c7b\u578b:\u5176\u4ed6None"
remark=re.sub(r'(\\u[\s\S]{4})',lambda x:x.group(1).encode("utf-8").decode("unicode-escape"),content)
print(remark)

