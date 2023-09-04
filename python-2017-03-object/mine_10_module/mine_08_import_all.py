# 1.4 原则 —— 每一个文件都应该是可以被导入的
# 一个 独立的 Python 文件 就是一个 模块
# 在导入文件时，文件中 所有没有任何缩进的代码 都会被执行一遍！

import mine_08_temp

print(mine_08_temp.say_hello())
print("-" * 50)
