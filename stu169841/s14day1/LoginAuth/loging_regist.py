#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wr import NamePool
class LoginAuth(object):
   '所有员工的基类'
   empCount = 0
   np = NamePool()
   up_dic = {}
   def __init__(self, name, passport):
      self.name = name
      self.passport = passport
      LoginAuth.empCount += 1

   def Count(self):
     return LoginAuth.empCount

   def displayLoginRegist(self):
      print "Name : ", self.name,  ", passport: ", self.passport

   def Auth(self):
       if self.name+"\n" in LoginAuth.np.read():
           print "%s locked" % self.name
           exit()
       for i in LoginAuth.np.registread():
           up = i.split(":")
           LoginAuth.up_dic[up[0]] = up[1]

       if  self.name not in LoginAuth.up_dic.keys():

           print "Username not exist"
           exit()
       if self.passport+"\n" not in LoginAuth.up_dic.values():

           print "Uassport error"
       if self.name in  LoginAuth.up_dic.keys() and self.passport+"\n" ==  LoginAuth.up_dic.get(self.name):
           print "Regist Success Welcome",self.name
           exit()

if __name__ == "__main__":

    name = raw_input("Username:")
    while True:
        pwd = raw_input("Passport:")
        login = LoginAuth(name, pwd)
        if login.Count() == 3:
            print "%s locked" % name
            LoginAuth.np.write(name + "\n")
            exit()
        login.Auth()
        a = 3-int(login.Count())

        print "还有%d次账户将被锁定！！！" % a
