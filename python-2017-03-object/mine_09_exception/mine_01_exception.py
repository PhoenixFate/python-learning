try:
    num = int(input("请输入一个整数"))
    # 被除数/除数
    result = 20 / num
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("除数不能为0")
except ValueError as e:
    print(e)
    print("输入的值不能转换为数字")

# 捕获未知错误
except Exception as e:
    print("发生了异常")
    print(e)

print("-" * 50)
