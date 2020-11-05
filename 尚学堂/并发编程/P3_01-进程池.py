# 进程池
import os
import time
from multiprocessing import Pool


def work(name):
    for i in range(10):
        print("进程{}：{}开始工作...".format(os.getpid(), name))
        time.sleep(0.5)


if __name__ == '__main__':
    pool = Pool(8)

    for i in range(10):
        pool.apply_async(work, args=("{}号员工".format(i + 1),))

    # 关闭进程池，只是不在接受新的进程，原有的进程继续执行
    pool.close()
    pool.join()