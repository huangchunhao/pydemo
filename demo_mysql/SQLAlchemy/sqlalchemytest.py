# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 19:52
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : sqlalchemytest.py
# @Software: PyCharm

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://autotest:autotest@192.168.1.3:3306/testdb')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()


sessionquery = DBSession()
user = sessionquery.query(User).filter(User.id=='5').one()
print(type(user))
print(user.name)
sessionquery.close()
