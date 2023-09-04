def sum_numbers(*args):
    num = 0
    for n in args:
        num += n

    return num


result = sum_numbers(1, 2, 23, 7, 45)
print("累加之和：%d" % result)
