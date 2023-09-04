# *
# **
# ***
# ****
row = 0
while row <= 5:
    print("*" * row)
    row += 1
print("end")

row = 0
while row <= 5:
    count = 0
    while count < row:
        print("*", end="")
        count += 1
    print("")
    row += 1
print("end")
