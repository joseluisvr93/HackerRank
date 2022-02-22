def whatFlavors(cost, money):
    result = []
    for i in range(len(cost)):
        c2 = cost[i+1:len(cost)]
        if money - cost[i] in c2:
            j = c2.index(money - cost[i]) + i + 1
            result.append(i+1)
            result.append(j+1)
            print(i+1, j+1)
            return result

t = int(input())
for t_itr in range(t):
    money = int(input().strip())
    n = int(input().strip())
    cost = list(map(int, input().rstrip().split()))
    result = whatFlavors(cost, money)
    print(result)

