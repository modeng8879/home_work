import random
import threading
import time
result = []
from s14day9.MyThread.myttt import MyThread
# class MyThread(threading.Thread):
#     def __init__(self,name,mysleep):
#         super(MyThread, self).__init__()
#         self.name = name
#         self.mysleep = mysleep

def run(name,mysleep):
    semaphore.acquire()
    time.sleep(mysleep)
    # print("你好 %s" % name)
    semaphore.release()
    return {"name":name,"time":mysleep}

    # def getresult(self):
    #     return self.result
if __name__ == "__main__":
    semaphore = threading.BoundedSemaphore(160)
    start_time = time.time()
    t = MyThread()
    myt_list = []

    for num in range(160):
        myt_list.append({"func": run, "args": ("lize%s" % num,random.randint(1,3))})

    t.set_thread_func_list(myt_list)
    t.start()
    print(t.ret_flag)
    print(time.time()-start_time)
