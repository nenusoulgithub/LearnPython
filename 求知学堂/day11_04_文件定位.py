# 文件定位
# tell() 文件指针位置
with open("111.txt", "r", encoding="utf8") as fo:
    # 一个中文占用3个字节，一个英文字符占用一个字节
    print(fo.read(3))
    print(fo.tell())
    print(fo.read(2))
    print(fo.tell())

# truncate() 删除文件内容
# with open("111.txt", "w", encoding="utf8") as fo:
#     fo.truncate(5)

print("----------------------------------------")
# seek() 指定光标位置
# 对于用r模式打开文件的情况，由于文本文件中没有使用rb模式打开文件，只允许从文件的开头计算位置。
with open("111.txt", "rb") as fo:
    print(fo.read(3).decode("utf8"))
    print(fo.tell())
    # 从当前位置往左移动3个字节
    fo.seek(-3, 1)
    print(fo.tell())
    print(fo.read(3).decode("utf8"))
    # 从当前位置往右移动3个字节
    fo.seek(3, 1)
    print(fo.read(3).decode("utf8"))
    # 从文件开始位置向右移动3个字节
    fo.seek(3, 0)
    print(fo.read(3).decode("utf8"))
    # 从文件结束位置向左移动3个字节
    fo.seek(-4, 2)
    print(fo.read(3).decode("utf8"))