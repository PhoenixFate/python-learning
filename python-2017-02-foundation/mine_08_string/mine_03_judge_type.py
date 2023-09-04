hello = "hello python"

# 类型判断
# 1.string.isspace()如果strin中只包含空格，返回True
# \t \n \r 空格 都属于空白字符
space_str = " \t\n\r"
print("如果string中只包含空格，返回True: %s" % space_str.isspace())
print(hello.isspace())

# 2.string.isalnum()如果string至少有一个字符，并且所有字符串都是字母或数字，返回True
alnum_str = "abc123"
print("如果string至少有一个字符，并且所有字符串都是字母或数字，返回True: %s" % alnum_str.isalnum())
print(hello.isalnum())

# 3.string.isalpha()如果string至少有一个字符，并且所有字符串都是字母，返回True
alpha_str = "abc"
print("如果string至少有一个字符，并且所有字符串都是字母，返回True%s" % alpha_str.isalpha())

# 4.isdecimal （重要）
# isdigit
# isnumeric
# 都不能判断小数
# num_str = "123"
# num_str = "\u00b2"
num_str = "一千零一"
print("isdecimal:%s" % num_str.isdecimal())
print("isdigit:%s" % num_str.isdigit())
print("isnumeric:%s" % num_str.isnumeric())

# 5.islower
# isupper
lower_str = "abc"
upper_str = "ABC"
print("islower:%s" % lower_str.islower())
print("islower:%s" % lower_str.isupper())
print("isupper:%s" % upper_str.islower())
print("isupper:%s" % upper_str.isupper())
