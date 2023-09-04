

def multiple_table():
    for i in range(1, 9):
        for j in range(1, i):
            print("%d * %d = %d" % (i, j, i * j), end="\t")
        print()
    print("end")
