# 函数参数
# 参数分为：【默认参数】，可选参数，关键字参数


# 1. 必选参数
def f_sum(a, b):  # 行是参数，定义时候的，不占用内存地址
    result = a + b
    print(result)
    return result


print(f_sum(25, 15))  # 实参，必须要传值


# 默认参数，默认参数只出现在参数的尾部
def f_sum1(a, b=20):
    result = a + b
    print(result)
    return result


f_sum1(a=100)


# 可变长参数，当参数个数不确定时使用。
def f_sum2(*args):
    """
    计算累加和
    @param args:
    @return:
    """
    result = 0
    for arg in args:
        result += arg
    print(result)


f_sum2(1)
f_sum2(1, 2)
f_sum2(1, 2, 3)
f_sum2(*(1, 2, 3))
