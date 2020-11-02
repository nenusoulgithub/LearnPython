import os
import threading


# 实现文件拷贝方法
def copy_file(filename, source_dir, desc_dir):
    print("--------------------------------")
    print("copy {} from {} to {}".format(filename, source_dir, source_dir))
    print("--------------------------------")

    source_path = os.path.join(source_dir, filename)
    dest_path = os.path.join(desc_dir, filename)

    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                content = source_file.read(1024)
                if content:
                    dest_file.write(content)
                else:
                    break


if __name__ == '__main__':
    source_dir = "D:\BaiduNetdiskDownload\视频-2小时玩转python多线程编程"
    dest_dir = "D:\视频-2小时玩转python多线程编程"

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    else:
        for file_name in os.listdir(dest_dir):
            if os.path.isfile(os.path.join(dest_dir, file_name)):
                os.remove(os.path.join(dest_dir, file_name))

    file_list = os.listdir(source_dir)

    for file in file_list:
        print(file)
        copy_process = threading.Thread(target=copy_file, args=(file, source_dir, dest_dir))
        copy_process.start()
