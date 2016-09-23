# def log(func):
#     def wrapper(*args, **kw):
#         print( 'call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('2013-12-25')
#
# now()
import time



# import time
# def timer(func):
#
#     def deco():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("The func run time is %s" %(stop_time-start_time))
#     return deco
# deco
# @timer
# def time1():
#     time.sleep(3)
#     print("In the time")
# time1()
# def no_sleep(func):
#     print("sleepping is fuck,fuck")
#     return func
# @no_sleep #time_new = no_sleep(time_new)
# def time_new():
#     # time.sleep(2)
#     print("sleep 2s")
#
# time_new()
# import sys
#
# a = map(lambda x: x*x,[1,2,3,4])
# print(list(a))
# def test():
#     pass
# a = test
#
# print (test)
#
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log #now_time= log(now_time)
# def now_time():
#     print( '2013-12-25')
# now_time()
# print(a)
# print(type(range(5)))
#1.定义log
#2.执行now_time = log(now_time)
#3.返回wrapper   =====>>>  now_time = wrapper
#4.现在执行now_time() 相当于执行wrapper了吧即wrapper()
#5.
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print( '%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2013-12-25')
#
# print(now)
from tkinter import *
import tkMessageBox
def quit():
    if e1.get() == "":
        pass




top = Tk()

top.title('登陆框')

top.geometry('+800+350')  #设置窗口出现的位置
top.resizable(width=False,height=False)
Label(top, text='账号：').grid(row=0,column=0)
Label(top, text='密码：').grid(row=1,column=0)

e1 = Entry(top, fg='black', bg='white') #单行文字输入框
e2 = Entry(top, fg='black', bg='white',show='*') #单行文字输入框

e1.grid(row=0,column=1)
#密码密文
e2.grid(row=1,column=1,)

#按钮
b = Button(top,text='登陆', width='20',height='1',command=quit)
b.grid(row=2,column=1)


mainloop()