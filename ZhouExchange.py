import random

question = input("请输入所求问题：")
choose1 = input("请输入解决方案1：")
choose2 = input("请输入解决方案2：")

choose1Num = random.randint(1, 99)
choose2Num = 100 - choose1Num

randomSwitch = random.randint(1, 999)
if randomSwitch > 888:
    if choose1Num < choose2Num:
        tempNum = choose1Num
        choose1Num = choose2Num
        choose2Num = tempNum

print(choose1 + ": " + str(choose1Num) + "%")
print(choose2 + ": " + str(choose2Num) + "%")

