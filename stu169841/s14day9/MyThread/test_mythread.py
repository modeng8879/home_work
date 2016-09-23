import threading,time
def run(n):
    semaphore.acquire()

    time.sleep(1)
    print("run the thread: ")
    semaphore.release()

if __name__ == "__main__":
    semaphore = threading.BoundedSemaphore(5)
    for i in range(22):
        t = threading.Thread(target=run, args=("lize",))
        t.start()