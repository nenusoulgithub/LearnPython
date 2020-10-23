# 函数参数
# 参数分为：【默认参数】，可选参数，关键字参数


# 可变关键字参数
# 使用 ** 来定义
def keyFunc(**kwargs):
    """
    关键字可变参数
    @param kwargs:
    @return:
    """
    print(kwargs)


# 第一种调用方式
keyFunc(name="Peter", age=10)

# 第二种调用方式
dictA = {"name": "Peter", "age": 10}
keyFunc(**dictA)


# 混合参数类型 可变参数和可变关键字参数
def complexFunc(*args, **kwargs):
    """
    可变参数 和 可变关键字参数混用，可变参数要放到可变关键字参数前面
    @param args:
    @param kwargs:
    @return:
    """
    print(args)
    print(kwargs)


# 可变参数 和 可变关键字参数 可以都传递
complexFunc(1, 2, 3, 4, name="Perter", age=10)

# 可变参数 和 可变关键字参数 也可以只传递可变参数
complexFunc(name="Perter", age=10)
