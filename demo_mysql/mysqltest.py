# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 19:31
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : mysqltest.py
# @Software: PyCharm

import mysql.connector

conn = mysql.connector.connect(host='192.168.1.3', port='3306', user='autotest', password='autotest', database='testdb',
                               use_unicode=True)
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values (%s, %s)', ['7', 'Michael'])
print(cursor.rowcount)
conn.commit()
cursor.close()

cursorquery = conn.cursor()
cursorquery.execute('select * from user where id = %s', (7,))
print(cursorquery.fetchall())
cursorquery.close()

conn.close()