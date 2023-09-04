# 类属性
class Tool(object):
    # 使用赋值语句定义类属性 记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        # 在类方法内部 可以使用cls 访问类属性或者类方法
        # cls.test()
        print("工具类 创建的对象 数量：%d" % cls.count)

    @classmethod
    def test(cls):
        print("类方法测试")
        print(cls)


tool1 = Tool("榔头")

Tool.show_tool_count()
Tool.test()
