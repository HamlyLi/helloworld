import random

a = input("please input:")
print(a)
print(type(a))

num = random.randint(1, int(a))
print(num)

numList = []
numList.append(1)
numList.append(2)
print(numList)

fileName = "/Users/hans/PycharmProjects/helloworld/test.txt"
f = open(fileName, 'w+')
f.writelines(a)
f.close()

f1 = open(fileName)
content = f1.read()
f1.close()
print(content)
print(content.count("0"))

