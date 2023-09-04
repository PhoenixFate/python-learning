# 不推荐使用 会替换掉某个东西
# 默认以最后导入的为最新的
# 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
from mine_01_module1 import *
from mine_02_module2 import *

print(title)
say_hello()
dog = Dog
print(dog)
