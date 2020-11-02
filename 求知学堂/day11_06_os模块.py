import os

# 文件重命名
# os.rename("111.txt", "222.txt")
# 删除文件
# os.remove("111.txt.bak")
# 新建文件夹
# os.mkdir("abc")
# os.mkdir("abc/cde")  # 不能直接创建两级目录
# 创建多级文件夹
# os.makedirs("abc/cde/efg")
# 删除文件夹
# os.rmdir("abc")
# 删除有内容的文件夹
# import shutil
# shutil.rmtree("abc")
# 获取当前目录
print(os.getcwd())
# 拼接目录
print(os.path.join(os.getcwd(), "222.txt"))

print("-------------------------------------------------")
# 获取目录列表
print(os.listdir("D:/"))
for entry in os.listdir("D:/"):
    # 判断是否是文件
    if os.path.isfile(os.path.join("D:/", entry)):
        print(os.path.join("D:/", entry))
    # 判断是否是目录
    if os.path.isdir(os.path.join("D:/", entry)):
        print(os.path.join("D:/", entry))

print("-------------------------------------------------")
# 使用现代版的写法，使用with与迭代器一起使用，会在使用完毕后释放资源
with os.scandir("D:/") as entries:
    for entry in entries:
        print(entry.name)
