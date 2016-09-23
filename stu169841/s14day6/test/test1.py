# class Role(object):
#
#     def __init__(self,name,role,weapon):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         # self.__life_value = life_value
#         # self.money = money
#
#     def shot(self):
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self,gun_name):
#         print("just bought %s" %gun_name)
# #
# # r1 = Role('Alex','police','AK47') #生成一个角色
# #
# # r2 = Role('Jack','terrorist','B22')  #生成一个角色
#
#
# class aa(Role):
#     def __init__(self,name, role, weapon,shen):
#         Role.__init__(self, name, role, weapon)
#         self.shen = "ye"
#
#     def show(self):
#         self.got_shot()
#         print("111111111")
# print(aa('Jack','terrorist','B22','a').name)

#
# Role.num="Role"
# r1.num=111111
# r1.num_list.append("1")
# print(r1.num,r1.num_list)
# r2.num_list.append("2")
# print(r2.num,r2.num_list)

#
# class Peoper(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.friends = []
#
#     def eat(self):
#         print("%s eating...." % self.name)
#
#     def sleep(self):
#         print("%s sleeping....." % self.name)
#
#
# class zhong(object):
#     def make_friends(self,obj):
#         print("%s and %s making friend" %(self.name,obj.name))
#         self.friends.append(obj)
# class Man(zhong,Peoper):
#     # def __init__(self,name, age, manoy):
#     #     super(Man,self).__init__(name, age)
#     #     self.manoy = manoy
#     def pay(self):
#         print("pay.....")
#
# class Woman(zhong,Peoper):
#     def cry(self):
#         print("wa wa wa .......")
#
# m1 = Man("ze",22)
#
# w1 = Woman("li",22)
#
# m1.make_friends(w1)
# w1.name = "chensanpao"
# print(m1.friends[0].name)

