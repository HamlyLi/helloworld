import random

def randGen():
    numList = []
    for i in range(1,2000):
        numList.append(random.randint(1,2000))
    return numList


def nonRepeat(numList):
    uniqueNums = set()
    for n in numList:
        uniqueNums.add(n)
    print(uniqueNums)

def repNums(numList):
    uniqueNums = set()
    for n in numList:
        uniqueNums.add(n)

    numHash = {}
    for n in uniqueNums:
        numHash[n] = 0

    for n in numList:
        numHash[n] += 1

    res = {}
    for n in numHash:
        if numHash[n] > 1:
            res[n] = numHash[n]

    print(res)



numList = randGen()

print(numList)

nonRepeat(numList)

repNums(numList)
