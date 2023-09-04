# *-* coding:utf8 *-8
# 在第一行 增加如上的话，python2.x解释器
# 或者：
# coding=utf8

# 在字符串前面添加u ,告诉解释器这是一个utf8编码的字符串
# python3 默认所有字符串都是utf8
hello_str = u"hello 中国"
# 在python下面 依然是按照单个字节解析的
for c in hello_str:
    print(c)
print("*" * 10)
# 字符串前面加个b 代表byte数组  type:bytes
# string 通过encode方法转为bytes
# bytes 通过decode转为string

str1 = "中文"
print("str1.encode('unicode_escape') 将中文转为unicode编码的bytes数组:%s" % str1.encode("unicode_escape"))

str2 = b'\\u4f60\\u597d'
print("str2.decode('unicode_escape') 将bytes数组以unicode编码的转为字符串:%s" % str2.decode('unicode_escape'))

str3 = "中文"
print("str3.encode('utf-8') 将中文转为utf8编码的bytes数组:%s" % str3.encode('utf-8'))

str4 = b'\xe4\xb8\xad\xe6\x96\x87'
print("将utf-8编码的bytes数组转成字符串: %s " % str4.decode("utf-8"))
