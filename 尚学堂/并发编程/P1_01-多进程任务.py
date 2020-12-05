# 多进程任务
from multiprocessing import Process
import time
import os


def sing(name):
    for i in range(10):
        print("进程{}：{}在唱歌...".format(os.getpid(), name))
        time.sleep(1)


def dance(name):
    for i in range(10):
        print("进程{}：{}在跳舞...".format(os.getpid(), name))
        time.sleep(1)


if __name__ == '__main__':
    sing_process = Process(target=sing, args=("志玲姐姐",))
    dance_process = Process(target=dance, kwargs={"name": "志玲姐姐"})

    sing_process.start()
    dance_process.start()

    # 强制清理，不会清理内存空间
    # sing_process.terminate()

    # 判断进程是否正在运行
    # sing_process.is_alive()

    # 主进程阻塞，等待子进程终止，timeout为等待时间。
    # sing_process.join(timeout=10)
    # dance_process.join()

    print("主进程执行完毕")