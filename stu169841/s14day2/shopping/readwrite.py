from env import *
# print(buypath)
class ReadWrite(object):

    def read(self,file_path):
        with open(file_path, 'r')as f:
           return f.readlines()

    def write(self,file_path, file_content):
        with open(file_path, 'a+')as f:
             f.writelines(file_content)

    def onewrite(self,file_path,file_content):
        with open(file_path,'w') as f:
            f.writelines(file_content)

    def oneread(self,file_path):
        with open(file_path,'r') as f:
            return f.read()
# wr = ReadWrite()
# print([i.strip() for i in wr.read(buypath)])
# wr.write(goodspath,)
