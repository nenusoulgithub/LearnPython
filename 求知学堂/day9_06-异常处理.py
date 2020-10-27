# 异常处理模块
try:
    # print(b)
    # x = 10
    # y = 0
    # print( x / y)
    print("Hello Python Exception!")
except NameError as msg:
    print(msg)
except ZeroDivisionError as msg:
    print(msg)
except Exception as msg:
    print(msg)
else:
    print("没有异常进入代码块")
finally:
    print("不管有没有异常都进入代码快")


# 自定义异常
class MyException(Exception):
    def __str__(self):
        return "MyException"


try:
    a = 5
    if a > 0:
        raise MyException
except MyException as msg:
    print(msg)
else:
    print("没有异常进入代码块")
finally:
    print("不管有没有异常都进入代码快")
