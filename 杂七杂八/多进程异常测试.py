from multiprocessing import Pool, Manager


def run(name, queue):
    print("进程%d开始执行..." % name)
    try:
        if name % 2 != 0:
            raise Exception("%d不能被2整除" % i)
    except Exception:
        queue.put("进程%d开始执行失败..." % name)
        raise Exception("%d不能被2整除" % i)
    finally:
        queue.put("进程%d开始执行结束..." % name)


if __name__ == '__main__':
    queue = Manager().Queue()
    pool = Pool(3)

    for i in range(0, 10):
        pool.apply_async(run, args=[i, queue])

    pool.close()
    pool.join()

    while not queue.empty():
        print(queue.get())
