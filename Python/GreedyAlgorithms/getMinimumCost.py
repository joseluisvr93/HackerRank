def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    cp = 0
    pp = 1
    j = 0
    for i in range(len(c)):
        if j >= k:
            cp += 1
            j = 0
        cost += (cp+pp)*c[i]
        print("(",cp,"+",pp,")*",c[i],"=",(cp+pp)*c[i])
        j += 1
    return cost

nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
minimumCost = getMinimumCost(k, c)
print(minimumCost)

