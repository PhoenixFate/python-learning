# 格式化后面的 '()' 本质上就是元组
print("%s 的年龄是: %d, 身高是: %.2f" % ('carry', 18, 1.754))
# 万能的%r
print("%r 的年龄是: %r, 身高是: %r" % ('carry', 18, 1.754))
print("%d" % True)
print("%d" % False)
info = ("carry", 18, 1.75)

print("%s 的年龄是: %d, 身高是: %.2f" % info)
