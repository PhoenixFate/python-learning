def demo1():
    return int(input("请输入一个整数"))


def demo2():
    return demo1()


try:
    print(demo2())

except ValueError as e:
    print("异常 %s ;请输入正确的数字" % e)

except Exception as e:
    print("未知异常：%s" % e)
