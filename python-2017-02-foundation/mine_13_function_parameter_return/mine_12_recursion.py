def sum_number(num):
    print(num)
    # 递归的出口
    # 当满足某个条件时，不再执行
    if num == 1:
        return
    sum_number(num - 1)


sum_number(10)
