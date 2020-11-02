import time
import threading


def sing(num, name):
    for i in range(num):
        print("{}唱歌...".format(name))
        time.sleep(0.5)


def dance(num, name):
    for i in range(num):
        print("{}跳舞...".format(name))
        time.sleep(0.5)


if __name__ == '__main__':
    sing_process = threading.Thread(target=sing, args=(3, "小明"))
    dance_process = threading.Thread(target=dance, kwargs={"num": 3, "name": "小红"})

    sing_process.start()
    dance_process.start()
