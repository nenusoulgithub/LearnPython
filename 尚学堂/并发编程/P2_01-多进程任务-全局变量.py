# 多进程任务
# 全局变量在多个进程中不共享
from multiprocessing import Process

num = 10


def func1():
    global num
    num += 10
    print("进程1中num的值是{}".format(num))


def func2():
    global num
    num += 20
    print("进程2中num的值是{}".format(num))


if __name__ == '__main__':
    p1 = Process(target=func1)
    p2 = Process(target=func2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # 强制清理，不会清理内存空间
    # sing_process.terminate()

    # 判断进程是否正在运行
    # sing_process.is_alive()

    # 主进程阻塞，等待子进程终止，timeout为等待时间。
    # sing_process.join(timeout=10)
    # dance_process.join()

    print("主进程中num的值是{}".format(num))