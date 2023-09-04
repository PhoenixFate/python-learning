# 访问实例属性，封装实例方法
# 访问类属性，封装类方法
# 不访问实例属性，也不访问类属性，封装静态方法


class Dog3(object):

    @staticmethod
    def run():
        print("狗 跑步")


# 调用静态方法：
# 类名.静态方法
Dog3.run()
dog = Dog3()
# 实例.静态方法(不推荐)
dog.run()
