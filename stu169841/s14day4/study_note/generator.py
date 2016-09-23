#_*_coding:utf-8_*_
# __author__ = 'Alex Li'
#
# import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        baozi = yield
#
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
#
# def producer():
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("第%s个包子做好了!"%i)
#         c.send(i)
#         c2.send(i)
#
# producer()

# b = bytearray('abcde',encoding='utf-8')
# print(b[:])
#
# res = filter(lambda n:n!=2, range(10))
# for i in res:
#     print(i)

# a = [4,3,2,1]
# b = ['a','b','c','d']
# for i in zip(a,b):
#     print(i)
import os
print(__file__)

print(os.path.split(__file__)[0] + "/../")