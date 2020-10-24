# 局部变量，函数体内部的变量
# 如果想在函数内部修改全局变量，需要在函数内部使用global关键字声明
pro = "计算机"


def printInfo():
    """
    name 就是局部变量
    pro 就是全局变量
    @return:
    """
    name = "Peter"
    print(name)
    print(pro)


printInfo()


def updatePro():
    """
    函数内部更新全局变量必须添加global关键字
    @return:
    """
    global pro
    pro = "电影"


updatePro()
printInfo()