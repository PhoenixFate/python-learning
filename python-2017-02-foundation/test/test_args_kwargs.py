import string


def test(*args):
    print(type(args), args)


test()
test(1)
test(1, 2)
test(1, 2, 3, 'a', [1, 2, 3])
a: int = 10
print(a)
name: string = "abc"
print(name)
print(type(name))
name2 = "bcd"
print(type(name2))
