import shutil
import socketserver
import json,os
import zipfile
from ftp_server.conf.setting import Storage_path,Storage_bak_path,mysep,UserJson
class MyTCPHandler(socketserver.BaseRequestHandler):

    def auth(self,*args):
        auth_dic =  args[0]
        name = auth_dic["user"]
        pwd = auth_dic["pwd"]
        user_list = []
        UserJsonfile = mysep.join([UserJson, 'users.json'])
        with open(UserJsonfile, 'r') as f:
            for line in f:
                line = json.loads(line)
                user_list.append(line["user"])
                if name == line["user"]:
                    user_info = line

            if name == user_list:
                if pwd == user_info["pwd"]:
                    print("auth successful !!")
                    info = """
        totaldisk     {totaldisk}
        homedir       {homedir}
        diskuserd     {diskuserd}
                           """
                    result = (0, info.format_map(user_info["data"]))
                else:
                    result = (2, "password erorr")

            else:
                result = (1, user_list)

        self.request.send(json.dumps(result).encode("utf-8"))

    def get(self,*args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        clientttell = cmd_dic["filetell"]
        size = os.stat(mysep.join([Storage_path,filename])).st_size
        with open(mysep.join([Storage_path,filename]), "rb") as t:
            t.read()
            servertell = t.tell()

        msg_dic1 = {
            "size" : size,
            "filetell" : servertell
        }
        self.request.send(json.dumps(msg_dic1).encode("utf-8"))
        print("send :",json.dumps(msg_dic1).encode("utf-8"))
        start = self.request.recv(1024)
        f = open(mysep.join([Storage_path,filename]), "rb")

        if 0< clientttell < servertell:
            #jump seek
            f.seek(clientttell,0)
            print('jump seek',clientttell)
            print('start please go on !!!')

        for line in f:
            print(f.tell(),'start .....')
            self.request.send(line)
            count = f.tell()
        else:
            print("file download success...")
            f.close()

    def put(self,*args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(mysep.join([Storage_path,filename]),"wb")

        else:
            f = open(mysep.join([Storage_path,filename]) , "wb")

        self.request.send(b"200 ok")
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded..." % filename)
            zipping = zipfile.ZipFile(mysep.join([Storage_bak_path,filename.split(".")[-2]])+".zip",'w',zipfile.ZIP_DEFLATED)
            zipping.write(mysep.join([Storage_path,filename]))
            zipping.close()
            print("file [%s] zipfile ... " % mysep.join([Storage_path,filename]))

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)

            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()