# -*- coding: cp1251 -*-

import codecs
import json

# with codecs.open('newit.xml', encoding="cp1251") as news:
#     print(news.read())

a = 'Привет'
b = 'Ну, здравствуй'
c = [a, b]
print(c)

# print(ord('э')) # принимает букву возращает код
# print(chr(1101)) # принимает число, получает букву


for x in range(ord('а'), ord('я') + 1):
    print(x, chr(x))