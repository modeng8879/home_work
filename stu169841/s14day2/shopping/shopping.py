import time
from stu169841.s14day2.shopping.readwrite import ReadWrite
from stu169841.s14day2.shopping.env import *
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
wr = ReadWrite()
product_list = [i.strip() for i in wr.read(goodspath)]
shopping_list = []

if wr.oneread(salarypath):
    salary = wr.oneread(salarypath)
    print("Your current balance:", salary)
else:
    salary = input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice].split(':')
                if int(p_item[1]) <= salary: #买的起
                    shopping_list.append("%s buy %s %s" % (GetNowTime(),p_item,'\n'))
                    salary -= int(p_item[1])
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary) )
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                print("product code [%s] is not exist!"% user_choice)
        elif user_choice == 'q':
            print("--------shopping list-------")
            a =[]
            for i in shopping_list:
                a.append(i)
                print(i)

            wr.write(buypath, a)
            print("Your current balance:",salary)
            if salary > 0:
                wr.onewrite(salarypath,str(salary))
            else:
                wr.onewrite(salarypath, str(''))
            print('history goods'.center(50,'-'))
            print(wr.oneread(buypath))
            exit()
        elif user_choice == 'cz': #充值
            salary = int(input("Input your salary:"))

        else:
            print("invalid option")