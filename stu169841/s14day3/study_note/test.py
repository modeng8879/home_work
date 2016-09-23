#!/usr/bin/envpython
"""
list_1 = [1,2,3,3,5,5,6,7,8,9]
list_1 = set(list_1)
list_2 = set([2,6,0,66,22,8,4])
list_3 = set([1,3,7])
print(list_1.intersection((list_2)))    #交集
print(list_1 & list_2)
print(list_1.union(list_2))             #并集
print(list_2 | list_1)
print(list_1.difference(list_2))        #差集,list_1 里有的,list_2里面没有的,可以返取
print(list_1 - list_2)
print(list_1.issubset(list_2))          #子集
print(list_1.issuperset(list_2))        #父集
print(list_3.issubset(list_1))          #list_3是list_1的子集
print(list_1.symmetric_difference(list_2))   #对称差集,互相没有的取出来,去掉两个两个集合中重复的
print(list_1 ^ list_2)
print(list_1,type(list_1))

print('-------------')
#list_2.isdisjoint()
list_4 = set([5,6,8])
print(list_2.isdisjoint(list_3))

print('********************')
list_1.add(999)
list_1.update([888,999,777])
print(list_1)


print('======================>')
print (list_1.discard('ddd'))  #discard不存在不会报错
# print(list_1.remove(xe))     #remove不存在,会报错,删掉了也不会返回数据
"""
# import sys,time
# f = open('haha.txt','r',encoding='utf-8')
# print(type(f))
# for i in range(5):
#     time.sleep(1)
#     sys.stdout.flush()
#     sys.stdout.write('#')
#
#
#     # print(f.readline().strip())
# f.close()

# f = open('test','r+')
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# f.writelines('\n1111111111')
# f.tell()
# f.close()
# f_old = open('test','r')
# f_new = open('new_test','w')
# for i in f_old:
#     if "5555555555" in i:
#         print(i)
#         i = i.replace("5555555555","hahahahhhhhhhhhahahaha")
#     f_new.writelines(i)
# f_old.close()
# f_new.close()
# for line in f:
#     print(line)
# import sys
# import chardet
# print (sys.getdefaultencoding())
# a = u"你好"
# # print(a)
# b = a.encode('gbk')
#
# utf8_1 = b.decode('gbk').encode()
# print("utf8_1=======",utf8_1)
# print(type(utf8_1))
# print(chardet.detect(utf8_1))

# def test():
#     "haha"
#     return "hahaaaaaaa"
#
# test = test.__doc__
# print(test)
# http://www.cnblogs.com/alex3714/articles/5740985.html
# import  time
# def log():
#     time_format = "%Y-%m-%d %X"
#     time_current = time.strftime(time_format)
#     with open('function.txt','a+') as f:
#         f.write("time %s end action\n" % time_current)
#
# z=1
# print("aaa",type(z))
# def test1():
#     return 1,'haha',[1,2,3],{"a":"b"}
#
# def test2():
#     return
#
# def test3():
#     log()
#
# a = test1()
# b = test2()
# print("test2:",b)
# print(type(a[0]))

#
# def person(name, age, **kw):
#     print ('name:', name, 'age:', age, 'other:', kw)
#
#
# import chardet
# def test(a,b="a",*args,**kw):
#     print(kw)
#     print(args)
#     print(a)
#     print(b)
#
#
# test(2,1,3,set="aa")

# a = "lize"
# class l(object):
#
#     print("aaaaaaaa",a)
#     a = "niu"
#
#     print(a)
#
#     def d(self):
#         print(a)
# print("ggggg",a)

# print("ll==",l.a)
# print("dd==",l().d())
# print("aaa===",a)

#10的阶乘
#1x2x3x4x5x6x7x8x9x10
def fact(n):
    if n==1:
        return 1
    print( n * fact(n - 1))


print(fact(10))
