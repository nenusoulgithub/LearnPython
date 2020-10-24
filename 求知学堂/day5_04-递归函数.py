# 递归调用
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 递归文件
import os
def listFiles(filePath):
    for path in os.listdir(filePath):
        fullPath = os.path.join(filePath, path)
        if os.path.isdir(fullPath):
            listFiles(fullPath)
        else:
            print(fullPath)

listFiles("../")
