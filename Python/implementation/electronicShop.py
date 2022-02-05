def getMoneySpent(keyboards, drives, b):
    keyboards = sorted(keyboards, reverse=True)
    drives = sorted(drives, reverse=True)
    res = -1
    for i in drives:
        for j in keyboards:
            if ((i+j) < b) & ((i+j) > res):
                res = i+j
    return res

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)
