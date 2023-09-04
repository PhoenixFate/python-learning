# 类属性
class Tool(object):
    # 使用赋值语句定义类属性 记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("大刀")
tool3 = Tool("小刀")

# 访问类属性的两种方式
# 1.类名.类属性
# 2.对象.类属性（不推荐）

print("工具类创建对象的总数： %d" % Tool.count)
# 属性获取机制：向上查找机制
# 可以通过对象.属性 访问 类属性 （不推荐）
print(tool1.count)

# 注意：使用对象.属性名=值 赋值语句，只会给对象添加一个属性，而不会影响到 类属性到值
tool1.count = 99
print(tool1.count)
print(Tool.count)
