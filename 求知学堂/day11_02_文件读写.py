import codecs

# 写入文件
fw = codecs.open("111.txt", mode="w", encoding="utf8")
fw.write("写入第一行数据\n")
fw.write("写入第二行数据\n")
fw.close()

# 追加吸入文件
fw = codecs.open("111.txt", mode="a", encoding="utf8")
fw.write("写入第三行数据\n")
fw.close()

# 以二进制写入文件
fw = open("111.txt", "ab")
fw.write("写入第四行数据\n".encode("utf8"))
fw.close()

# 读取文件
fo = open("111.txt", "r", encoding="utf8")
print(fo.read())
fo.close()

# 按行读取
fo = open("111.txt", "r", encoding="utf8")
print(fo.readline().strip("\n"))
fo.close()

# 按行读取
fo = open("111.txt", "r", encoding="utf8")
for line in fo.readlines():
    print(line.strip("\n"))
fo.close()

# 二进制读取数据
fo = open("111.txt", "rb")
for line in fo.readlines():
    print(line.decode("utf8").strip("\n"))
fo.close()
