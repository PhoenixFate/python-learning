# 代码结构:
# shebang （用哪一个解释器解释该代码）
# import模块
# 全局变量
# 函数定义
# 执行代码


# 开发的时候应该在函数开头定义所有的全局变量
# 为了避免全局变量和局部变量混淆，建议在全局变量前面添加前缀 g_ or gl_
gl_num = 10


def demo():
    # 如果局部变量和全局变量一样，pycharm会在局部变量下面添加一条灰色线
    num = 100
    print("%d" % num)
    print("%s" % gl_title)
    # 执行的时候这里会报错
    # print("%s" % name)


# 程序不会有问题
gl_title = "my title"
demo()

#
name = "tom"
