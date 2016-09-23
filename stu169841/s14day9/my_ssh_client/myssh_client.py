import os

import paramiko


class MyLogingClient(object):
    def __init__(self,host,port):
        self.host = host
        self.port = int(port)

    def myssh(self,username,keypath=None ,passportd = None):
        paramiko.util.log_to_file('paramiko_ssh.log')
        ssh = paramiko.SSHClient()
        if keypath != None and passportd ==None:
            key = paramiko.RSAKey.from_private_key_file(keypath)
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, self.port,username,pkey=key)
        else:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, self.port,username,passportd)
        self.ssh = ssh

    def mytranslate(self,username,keypath=None ,passportd = None):
        paramiko.util.log_to_file('paramiko_translate.log')
        t = paramiko.Transport((self.host, self.port))
        if keypath != None and passportd ==None:
            key = paramiko.RSAKey.from_private_key_file(keypath)
            t.connect(username,pkey=key)
            sftp = paramiko.SFTPClient.from_transport(t)
        else:
            t.connect(username, passportd)
            sftp = paramiko.SFTPClient.from_transport(t)
        self.sftp = sftp

    def mycmd(self,cmd):
        # while True:
        #     cmd = input("input a cmd：")
        if cmd.startswith("exit"):
            exit("logout login...")
        cmd_first = cmd.split()[0]
        if hasattr(self,"my_%s" % cmd_first):
            func = getattr(self,"my_%s" % cmd_first)
            func(cmd)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        print(stdout.read().decode())
        if stdout.read().decode():
            print(stderr.read().decode())


    def myget(self,*args):
        """ remote , source file"""
        print("remote , source file")
        self.sftp.get(args[1],args[2])

    def myput(self,*args):
        """source , remote file"""
        print("source , remote file")
        self.sftp.put(args[1],args[2])
if __name__ =="__main__":
    mysep = os.path.sep
    key_path = os.path.dirname(os.path.abspath(__file__)) + mysep + "id_rsaold"
    crete_first = MyLogingClient("192.168.1.102",22)
    crete_first.myssh("lize",passportd="123456")
    crete_first.mycmd("ls")
