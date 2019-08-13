# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 17:41
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : fakertest.py
# @Software: PyCharm
from faker import Faker
from faker.providers import internet
from faker.providers import bank


if __name__ == "__main__":
    fake = Faker('zh_CN')

    print(fake.name())
    print(fake.address())
    print(fake.text())

    for _ in range(10):
        print(fake.name())

    fake.add_provider(internet)
    print(fake.ipv4_private())

    fake.add_provider(bank)
    print(fake.bank_country())

    print(fake.random)
    print(fake.random.getstate())

    fake.seed(1)
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.ipv4_private())
    fake.seed(5555)
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.ipv4_private())
    fake.seed(1)
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.ipv4_private())
    fake.seed_instance(5555)
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.ipv4_private())

    my_word_list = [
        'danish', 'cheesecake', 'sugar',
        'Lollipop', 'wafer', 'Gummies',
        'sesame', 'Jelly', 'beans',
        'pie', 'bar', 'Ice', 'oat']

    fake.sentence()
    # 'Expedita at beatae voluptatibus nulla omnis.'

    fake.sentence(ext_word_list=my_word_list)
    # 'Oat beans oat Lollipop bar cheesecake.'