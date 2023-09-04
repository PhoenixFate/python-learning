def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    """
    打印多行函数
    :rtype: object
    :param char:
    :param times:
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines('-', 50)
