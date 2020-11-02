# 主进程会等待所有的子进程结束后才会结束
import multiprocessing
import time


def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # 设置daemon = True则主进程结束，子进程直接结束
    work_process.daemon = True
    work_process.start()

    time.sleep(1)
    print("主进程执行结束")
