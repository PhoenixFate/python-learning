import random

player = int(input("请输入您要出到拳，石头（1）/剪刀（2）/不（3）："))
computer = random.randint(1, 3)
print("玩家选择到拳头是 %d - 电脑出到拳头是%d" % (player, computer))
# 比较胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")
