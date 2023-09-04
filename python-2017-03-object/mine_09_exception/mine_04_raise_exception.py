def input_password():
    # 1.提示用户输入密码
    password = input("请输入密码: ")
    # 2.判断密码长度>=8, 返回用户输入的密码
    if len(password) >= 8:
        return password
    # 3.如果密码长度<8，主动抛出异常
    print("主动抛出异常")
    raise Exception("密码错误")


try:
    print(input_password())
except Exception as result:
    print("捕获的异常:%s" % result)
