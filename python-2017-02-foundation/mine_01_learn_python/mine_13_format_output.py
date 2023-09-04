# %s 字符串
# %d 整型，%06d，不足6位补0
# %f 浮点型 %.2f 表示小数点后面只显示2位小数
# %% 输出%
name = "王小虎"
print("我的名字叫 %s,请多关照" % name)
studentNo = 12345677
print("我的学号%06d" % studentNo)
price = 112.5564
print("价格：%.2f" % price)

price = 5.6
weight = 7.8

money = price * weight
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))
# 输出10%
scale = 0.1
# %% 转义%
print("数据比例：%.2f%%" % (scale * 100))

# python 中的bool跟c很相似
b = True
print("bool: %d" % b)
print("bool: %s" % b)
# %r 万能打印；类似于go中的%v
print("bool: %r" % b)
a = 100
print("a: %x" % a)
print("a address: %x" % id(a))
# print("a address: %p" % id(a))
