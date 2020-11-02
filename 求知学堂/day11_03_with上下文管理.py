# 按行读取
# with管理的对象会自动释放
with open("111.txt", "r", encoding="utf8") as fo:
    for line in fo.readlines():
        print(line.strip("\n"))

# 小结
# 文件写入模式：w w+ wb wb+
# 普通文件使用：w w+
# 音频，视频文件使用：wb wb+
# 文件读取模式：r r+ rb rb+
# 读取普通文件：r r+
# 读取图片，视频文件：rb rb+

# 使用with进行文件拷贝
with open("111.txt", "r", encoding="utf8") as old_file, open("111.txt.bak", "w", encoding="utf8") as new_file:
    while True:
        content = old_file.read(3)
        new_file.write(content)
        if len(content) < 3:
            break
