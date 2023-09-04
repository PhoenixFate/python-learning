def test(num):
    print("test方法中num的地址：%d" % id(num))
    # 1.定义一个字符串变量
    result = "hello"
    print("函数要返回的数据的内存地址：%s" % id(result))
    # 2.将字符串变量返回
    return result


# 1.定义一个数字的变量
a = 10
print("a变量保存的内存地址是:%d" % id(a))
# 2.调用test，参数传递，本质上是传递实参保存数据的引用，而不是实参保存的数据
result_test = test(a)
print("接受到的参数返回值的内存地址：%s" % id(result_test))
