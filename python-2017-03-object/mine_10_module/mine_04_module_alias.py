# 模块别名应该满足 大驼峰命名法
# import 模块名1 as 模块别名

import mine_01_module1 as dog_module
import mine_02_module2 as cat_module

dog_module.say_hello()
cat_module.say_hello()

dog = dog_module.Dog()
print(dog)
cat = cat_module.Cat()
print(cat)
