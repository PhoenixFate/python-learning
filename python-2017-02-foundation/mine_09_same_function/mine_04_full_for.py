num1 = [1, 2, 3]
for a in num1:
    print(a)
else:
    print("如果循环遍历完，没有用break跳出循环，则else后面到语句会执行; 没有break")

for a in num1:
    print(a)
    if a == 3:
        break
else:
    print("如果循环遍历完，没有用break跳出循环，则else后面到语句会执行; 有break")
