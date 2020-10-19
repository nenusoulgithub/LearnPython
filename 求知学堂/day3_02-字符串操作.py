# Python的序列 字符串 列表 元组
# 优点：通过下标访问元素
# 共同点：支持切片
python = "Python"

print("字符串的第一个字符%s" % python[0])
print("字符串的第二个字符%s" % python[1])

for c in python:
    print(c, end=" ")

print("\n--------------------------------------")

# 大小写转换
python = "python"
print("将单词的首字母变为大写%s" % python.capitalize())
print("将单词所有字母变为大写%s" % python.upper())
print("将单词所有字母变为小写%s" % python.lower())
s = "I like Python."
print("把每个单词的首字符变大写%s" % s.title())
print("大小写逆转%s" % s.swapcase())
print("判断字符串是否大写%s" % python.upper().isupper())
print("判断字符串是否小写%s" % python.lower().islower())
print("--------------------------------------")

# 去掉空格
python = " P y t h o n "
print("去掉字符串中的空格%s。" % python.strip())
print("去掉字符串中的左边空格%s。" % python.lstrip())
print("去掉字符串中的右边空格%s。" % python.rstrip())

print("--------------------------------------")

# 复制字符串：内存地址的复制，是同一个内存地址的引用
_python = python
print("python的内存地址%d" % id(python))
print("python的内存地址%d" % id(_python))

print("--------------------------------------")

# 字符串查找
s = "I like Python."
print("使用find查找字符串o的位置%d" % python.find("o"))
print("使用find查找字符串o的位置%d" % python.index("o"))
print("字符串是否以I开头%s" % s.startswith("I"))
print("字符串是否以.结尾%s" % s.endswith("."))

print("--------------------------------------")

# 其他操作
print("判断是否字母和数字%s" % python.isalnum())
print("判断是否字母和数字%s" % s.isalnum())
print("判断是否字母%s" % python.isalnum())
print("判断是否数字%s" % "123".isdigit())
print("字符串连接%s" % "_".join(s))
print("替换字符串中的字母%s" % s.replace("I", "You", 1))
print("切分字符串%s" % s.split(" "))
print("字符串计数%d" % "aaabbcccc".count("c"))

print("--------------------------------------")
# 字符串切片(开始:结尾:步进)
print("Hello World!"[2:10])
print("Hello World!"[:10])
print("Hello World!"[2:])
print("Hello World!"[:-5])
print("Hello World!"[2:10:2])
print("Hello World!"[2:10:1])
print("Hello World!"[9:1:-1])
print("Hello World!"[-3:1:-1])
print("Hello World!"[-3:-11:-1])
print("Hello World!"[9:-11:-1])
