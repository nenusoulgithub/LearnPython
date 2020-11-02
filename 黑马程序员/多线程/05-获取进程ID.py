import time
import multiprocessing
import os


def sing(num, name):
    print("唱歌进程编号:{}，父进程编号:{}".format(os.getpid(), os.getppid()))
    for i in range(num):
        print("{}唱歌...".format(name))
        time.sleep(0.5)


def dance(num, name):
    print("跳舞进程编号:{}，父进程编号:{}".format(os.getpid(), os.getppid()))
    for i in range(num):
        print("{}跳舞...".format(name))
        time.sleep(0.5)


if __name__ == '__main__':
    sing_process = multiprocessing.Process(target=sing, args=(3, "小明"))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 3, "name": "小红"})
    print("主进程编号{}，主进程的父进程编号：{}".format(os.getpid(), os.getppid()))
    sing_process.start()
    dance_process.start()
