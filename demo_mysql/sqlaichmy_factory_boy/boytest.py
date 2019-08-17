# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 20:01
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : boytest.py
# @Software: PyCharm

from sqlalchemy import Column,String, Integer, Unicode, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://autotest:autotest@192.168.1.3:3306/testdb')
DBSession = scoped_session(sessionmaker(bind=engine))#这里需要使用scoped_session

#Base.metadata.create_all(engine) #创建表

import factory

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = DBSession   # the SQLAlchemy session object
        sqlalchemy_session_persistence="commit" #"commit"--perform a session commit() #'flush'-- perform a session flush()

    id = factory.Sequence(lambda n: n)
    #id = 9
    name = factory.Sequence(lambda n: u'User %d' % n)

#清除表内容
DBSession.query(User).delete()
#DBSession.query(User).filter(User.id==0).delete()
DBSession.commit()


# users=DBSession.query(User).all()
# for usr in users:
#     print(usr.__dict__)

#创建一条记录
UserFactory()
# UserFactory()
#创建100条记录
factory.build_batch(UserFactory, 100)
#DBSession.commit()
users=DBSession.query(User).all()
for usr in users:
    print(usr.__dict__)
print(len(users))
DBSession.remove()