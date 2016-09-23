# coding=utf-8
import sys, os
import time
for i in range(10):
    time.sleep(0.5)
    sys.stdout.write("File transfer progress :[%3d%s] percent complete!\n" % (i,'%'))
    sys.stdout.flush()