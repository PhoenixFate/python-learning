def sum_2_num(num1, num2) -> float:
    return num1 + num2
    # print("aaa")


result = sum_2_num(10, 20)
print("计算的结果: %s" % result)
# 万能的%r
print("计算的结果: %r" % result)


# 限定参数和返回值类型
def test(a: int, b: str) -> str:
    print(a, b)
    return b + str(a)


result2 = test(10, "hello")
print("result2: %s" % result2)
