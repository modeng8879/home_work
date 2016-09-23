
import socket
import json
import os
mysep=os.path.sep


class FtpClient(object):
    def __init__(self,name,pwd):
        self.client = socket.socket()
        self.name = name
        self.pwd = pwd
    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)
    def connect(self,ip,port):
        self.client.connect((ip, port))
    def interactive(self):
        ret,data = self.authenticate()
        if self.auth_check(ret,data):
            while True:
                cmd = input(">>").strip()
                if len(cmd) ==0:continue
                cmd_str = cmd.split()[0]
                if hasattr(self,"cmd_%s" % cmd_str):
                    func = getattr(self,"cmd_%s" % cmd_str)
                    func(cmd)
                else:
                    self.help()

    def cmd_put(self,*args):
        cmd_split =  args[0].split()
        if len(cmd_split) >1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename":filename,
                    "size": filesize,
                    "overridden":True
                }
                self.client.send( json.dumps(msg_dic).encode("utf-8")  )
                print("send",json.dumps(msg_dic).encode("utf-8") )
                #防止粘包，等服务器确认
                server_response = self.client.recv(1024)
                f = open(filename,"rb")
                for line in f:
                    self.client.send(line)
                    count = f.tell()
                    print(count)
                else:
                    print("file upload success...")

                    f.close()

            else:
                print(filename,"is not exist")
    def cmd_get(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
        client_size = os.stat(filename).st_size
        with open(filename, 'r') as f:
            f.read()
            client_tell = f.tell()

        msg_dic1 = {
            "action" : "get",
            "filename" : filename,
            "filetell" : client_tell
        }
        self.client.send(json.dumps(msg_dic1).encode('utf-8'))
        print("send",json.dumps(msg_dic1).encode('utf-8'))
        """
         server_msg1 :   "size" : size,
         server_msg1 :   "filetell" : servertell
        """
        server_msg1 = self.client.recv(1024)
        server_msg1 = json.loads(server_msg1.decode())

        if server_msg1["size"] > client_size and server_msg1["filetell"] >client_tell:
            f = open(filename, "ab+")
            print("rb jump")
        else:
            f = open(filename, "wb")
        self.client.send(b'200')

        received_size = client_tell
        while received_size < server_msg1["size"]:
            line = self.client.recv(1024)
            f.write(line)
            received_size +=len(line)
        else:
            print("file [%s] has download ..." % received_size)

    def authenticate(self):
        sed_info = {"action" : "auth","user" : self.name,"pwd" : self.pwd}
        self.client.send(json.dumps(sed_info).encode("utf-8"))
        sed_info["pwd"] = "*"*len(self.pwd)
        print("send", sed_info)
        user_info = self.client.recv(1024)
        user_info = json.loads(user_info.decode())
        return user_info

    def auth_check(self,ret,data):
        if ret == 0:
            self.data = data
            print(data)
            return True

        elif ret == 1:
            print("Please input anyone user:>>", data)
            return False

        else:
            print(data)
            return False

name = input("input your name: ")
pwd = input("input your passport: ")
ftp = FtpClient(name,pwd)
# ret,data = ftp.authenticate()
# if ret == 0:
#     print(data)
# elif ret == 1:
#     print("Please input anyone user:>>",data)
# else:
#     print(data)

ftp.connect("localhost",9999)
ftp.interactive()