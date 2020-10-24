# 匿名杉树
# 语法
# lambda 参数1,参数2...:表达式


func1 = lambda x, y: x + y
print(func1(1, 2))
print((lambda x, y: x + y)(1, 2))


func2 = lambda x: "可以参军" if x > 25 else "不可以擦参军"
print(func2(26))
