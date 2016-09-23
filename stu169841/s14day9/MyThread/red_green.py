import threading,time

event = threading.Event()
def car(name):
    while True:
        if event.is_set():
            print("%s running"%name)
        else:
            print("%s stopping %ss after running"%(name,5))
            event.wait()
        time.sleep(1)


def rglight():
    count = 0
    event.set() #green
    while True:
        if count < 10:
            # print("\033[34;1m green light...car run\033[0m")
            event.set()
        elif 10<=count<=15: #red
            # print("\033[33;1m red light ... car stop\033[0m")
            event.clear()
            if count==15:
                count = 0
        count+=1
        time.sleep(1)


light = threading.Thread(target=rglight,)
light.start()
car1 = threading.Thread(target=car, args=("自行车",))
car1.start()