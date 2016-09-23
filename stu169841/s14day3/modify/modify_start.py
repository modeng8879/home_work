import os
import sys
#print(conf_path)

# input_result = input('input a FQDN: ')
import time
conf_path = os.path.dirname(os.path.realpath(__file__))+"\conf\haproxy.conf"
class Haproxy_RW(object):

    """
    1、查
        输入：www.oldboy.org
        获取当前backend下的所有记录

    2、新建
    输入：
    arg = {
        'bakend': 'www.oldboy.org',
        'record':{
            'server': '100.1.7.9',
            'weight': 20,
            'maxconn': 30
        }
    }
    3. add
    4.delete
    """

    def search(self):

        # 1、查
        #     输入：www.oldboy.org
        #     获取当前backend下的所有记录
        # input_result = "www.lize.org"

        input_result = input('input a FQDN: ')
        if "." in input_result:
            jishu = 0
            with open(conf_path,'r') as f:
                f_list = f.readlines()
            for line in f_list:
                if input_result in line and line.startswith('backend'):
                    jishu +=1
                    print(input_result.center(50,"-"))
                    continue

                if jishu==1:
                    if line.startswith('backend') or jishu!=1:
                        jishu = 0
                        continue
                    # file_args = f_list[count].strip()1
                    if line.strip() != '':
                        file_args = line.strip()
                        print(file_args)


        else:
            print("input error!!!")

    def addbackend(self,a):
        """
        # for k,v in dict(backend_args).items():
        #     print(backend_templates[i].format_map({k:v}))
        #     i+=1
        """
        ###add
        b = a.split("\n")[1]+"\n"
        with open(conf_path,'r') as  f:
            f_list = f.readlines()
        if b in f_list:
            print("%s 已 经 存 在" % a)
        else:
            print(a)
            with open(conf_path, 'a+') as  f:
                f.writelines(a)
                asd = "%s Add Success" % a.split("\n")[1].split()[1]
                print(asd.center(80,'=') )

#删除
    def delbackend(self,a):
        def writeoldfile(newfile_list):
            f = open(conf_path, 'w')

            for i in newfile_list:
                i = '%s%s'%(i,'\n')
                f.writelines(i)
            print("del %s success writting old file " % a.split("\n")[1].split()[1])
            f.close()

        newfile_list = list()
        with open(conf_path,'r') as f:
            f_list = f.readlines()
        for index,line in enumerate(f_list):
            line = line.strip('\n')
            # print(index,"line",line)
            if line in a:
                line = line.replace(line,'')
            if line != '':
                newfile_list.append(line.strip())

        return writeoldfile(newfile_list)


if __name__ == "__main__":
    # backend_args = eval("""{
    # 'bakend': 'www.lize.org',
    #     'record':{
    #         'server': '100.110.110.110',
    #         'weight': 20,
    #         'maxconn': 30
    #     }
    # }""")
    # backend_templates = ["backend {bakend}" ,"server {record[server]} weight {record[weight]} maxconn {record[maxconn]}"]
    backend_templates = """
backend {bakend}
        server {record[server]} weight {record[weight]} maxconn{record[maxconn]}
   """
    # a = backend_templates.format_map(backend_args)
    #构造界面
    graph = """
###########################################################################################
#                         ##############################                                  #
#                         Wlcome use proxy modify system                                  #
#                            请选择你所要使用的功能序号                                   #
#                                                                                         #
#     0 添加                        1 查询                               2 删除           #
###########################################################################################\n"""

    function_list = ['添加',"查询","删除"]
    for i in graph:

        sys.stdout.write(i)
        sys.stdout.flush()
    PC = Haproxy_RW()
    while True:
        for index,function in enumerate(function_list):
                time.sleep(0.3)
                sys.stdout.write("  %s %s  "%(index,function))
                sys.stdout.flush()
        print()
        input_num  = input("[root@Proxy]# ")
        if input_num.isdigit():
            input_num=int(input_num)

            if input_num == 0:
                backend_args = eval(input("input a dict example ({'record': {'server': '100.110.110.110', 'maxconn': 30, 'weight': 20}, 'bakend': 'www.lize.org'}):"))
                a = backend_templates.format_map(backend_args)
                PC.addbackend(a) #add
            elif input_num == 1:
                PC.search()  #search
            elif input_num == 2:
                backend_args = eval(input("input a dict example ({'record': {'server': '100.110.110.110', 'maxconn': 30, 'weight': 20}, 'bakend': 'www.lize.org'}):"))

                a = backend_templates.format_map(backend_args)
                PC.delbackend(a) #del
            elif input_num == "q":
                exit()
            else:
                print("你输入的参数不对")
                exit()
    # PC.delbackend(a) #del
    # PC.addbackend(a) #add
    # PC.search()  #search
