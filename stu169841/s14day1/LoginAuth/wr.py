import os
np  = os.path.dirname(os.path.realpath(__file__)) + "\config\NamePool"
rp = os.path.dirname(os.path.realpath(__file__)) + "\config\Regist"
class NamePool(object):
    def write(self,str):
        f = open(np, 'a+')
        f.write(str)
        f.close()

    def read(self):
        with open(np,'r') as f:
            return f.readlines()

    def registread(self):
        with open(rp,'r') as f:
            return f.readlines()
