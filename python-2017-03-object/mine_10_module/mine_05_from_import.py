# 2）from...import 导入
# 如果希望 从某一个模块 中，导入 部分 工具，就可以使用 from ... import 的方式
# import 模块名 是 一次性 把模块中 所有工具全部导入，并且通过 模块名/别名 访问

from mine_01_module1 import Dog
from mine_01_module1 import title
# 如果从两个不同的模块，导入同名函数，后导入的会覆盖前导入的
# 使用as，可以解决这种问题
from mine_01_module1 import say_hello as module1_say_hello
from mine_02_module2 import say_hello

print(title)
module1_say_hello()
say_hello()
dog = Dog()

print(dog)
