def print_line():
    print("*" * 50)


def print_line2(char: str) -> None:
    print(char * 50)


def print_line3(char, times):
    print(char * times)


print_line()
print_line2('s')
print_line3('a', 20)
print(type('a'))
