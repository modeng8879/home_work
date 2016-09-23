import queue
q = queue.Queue()
q.put('d1')
q.put("d2")
q.put("d3")
def qu():

    while True:
        for i in range(4):
            print(q.get(timeout=10))