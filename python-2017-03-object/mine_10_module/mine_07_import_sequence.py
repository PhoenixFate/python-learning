# 模块导入的顺序
# 首先导入当前文件下的模块
# 然后在搜索系统文件
import random

# python每一个模块都有一个内置属性 __file__ 可以查看模块的 完整路径
print(random.__file__)

# [0,10]闭区间
rand_int = random.randint(0, 10)
print(rand_int)
