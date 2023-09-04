a = 1
b = 1
while a <= 9:
    b = 1
    while b <= a:
        print("%d * %d = %d" % (a, b, a * b), end="\t")
        b += 1
    print()
    a += 1
print("end")
