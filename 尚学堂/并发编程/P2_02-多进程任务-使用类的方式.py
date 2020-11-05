# 多进程任务
# 继承进程对象来实现并发
from multiprocessing import Process
import time
import os


class Sing(Process):
    def run(self) -> None:
        for i in range(10):
            print("进程{}：在唱歌...".format(os.getpid()))
            time.sleep(1)


class Dance(Process):
    def run(self) -> None:
        for i in range(10):
            print("进程{}：在跳舞...".format(os.getpid()))
            time.sleep(1)


if __name__ == '__main__':
    sing_process = Sing()
    dance_process = Dance()

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