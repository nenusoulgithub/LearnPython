# 进程间通信
import time
import multiprocessing
from multiprocessing import Queue
from multiprocessing import Process

# q = Queue(10)
# q.qsize()
# q.empty()
# q.full()
# q.get([block][timeout])
# q.get_nowait() = q.get(False)
# q.put(item[block][timeout])
# q.put_nowait() = q.put(False)


def produce(q):
    for i in range(10):
        q.put(i)
        time.sleep(0.5)


def consume(q):
    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    q = Queue(10)

    multiprocessing.JoinableQueue
