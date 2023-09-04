def say_hello():
    print("hello")
    return __name__


# 如果直接执行模块，__name__就是固定值 __main__
# 如果被导入，__name__就是模块名
print(__name__)
# 测试代码 ，被导入的时候不需要被执行
if __name__ == "__main__":
    print("小明开发的模块")
    say_hello()
