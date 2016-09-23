from BS import BaseSelect as s

one = [1,2,3]

two = [4,5,6]

three = [7,8,9]
def sb1(select):
    num=0
    for i in select.get_one():
        num +=1
        print "%d  %s" %(num,i)
    select_result = raw_input('\033[1;34mplease input num :  \033[0m').strip()
    one = list(select.get_one())[int(select_result)]
    return one

def sb2(select):
    num=0
    for i in select.get_two():
        num +=1
        print "%d  %s" %(num,i)
    select_result = raw_input('\033[1;34mplease input num :  \033[0m').strip()
    one = list(select.get_one())[int(select_result)]
    return one

def sb3(select):
    num=0
    for i in select.get_three():
        num +=1
        print "%d  %s" %(num,i)
    select_result = raw_input('\033[1;34mplease input num :  \033[0m').strip()
    one = list(select.get_one())[int(select_result)]
    return one


for i in one:
    sb = sb2(i)
    if i == 1:
        two[i]
select = s(one, two, three)

