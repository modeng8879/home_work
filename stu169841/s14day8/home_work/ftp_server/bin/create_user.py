import os
import json
from ftp_server.conf.setting import Storage_path,UserJson,mysep


class CreateUesr(object):
    def __init__(self,user,pwd,homedir,totaldisk=128*1024):
        self.user = user
        self.pwd = pwd
        self.homedir = homedir
        self.totaldisk = totaldisk
        self.data = {"homedir" : self.homedir, "totaldisk" : self.totaldisk, "diskuserd" : 0, "filetell" : 0}
        self.userinfo = {"user" : self.user, "pwd" : self.pwd, "data" : self.data}

    def userjson(self):
        if not os.path.exists(self.homedir):
            os.mkdir(self.homedir)
        return (self.userinfo)


init = CreateUesr('lize2','123',Storage_path)
userjsondir = mysep.join([UserJson,'users.json'])
userjson = init.userjson()
user_check = []

with open(mysep.join([UserJson,'users.json']), 'r+') as f:
    for line in f.readlines():
        line = json.loads(line)
        user_check.append(line["user"])
    if userjson["user"] in user_check:
        print("Add false %s is exists" % userjson["user"])
    else:
        f.writelines(json.dumps(userjson) + '\r')
        print("%s is writed succussful" % userjson["user"])
