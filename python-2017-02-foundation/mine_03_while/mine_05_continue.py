i = 0
while i <= 100:
    i += 1
    if i % 3 != 0:
        # 一旦发现continue 会跳到下一次循环判断处
        continue
    print("i: %d" % i)
print("end")
