import temp_function

a = 1
print(id(a))
print(id(1))
b = 1
print(id(b))

temp_function.temp_fun(a)
print(a)
print(id(a))
