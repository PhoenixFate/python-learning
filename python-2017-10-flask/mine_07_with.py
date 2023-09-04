# 通常情况，打开文件操作比较复杂，需要捕获异常，并且最终关闭文件
# 可以简化成with open 会自动关闭文件（即使有异常）
f = open("./1.txt", "w")
try:
    f.write("hello china")
except Exception as e:
    print(e)
finally:
    f.close()

with open("./1.txt", "w") as f:
    f.write("hello trump")


class Foo(object):
    def __enter__(self):
        """进入with语句的时候会被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exc_type: %s" % exc_type)
        print("exc_val: %s" % exc_val)
        print("exc_tb: %s" % exc_tb)


with Foo() as foo:
    print("learn 'with' language")
    a = 1 / 0
    print("hello end")
