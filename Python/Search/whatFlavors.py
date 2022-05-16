def whatFlavors(cost, money):
    result = []
    for sunny in cost:
        johnny = money - sunny
        if sunny != johnny:
            if johnny in cost:
                j = cost.index(johnny)
                r1 =cost.index(sunny) + 1
                r2 = j + 1
                result.append(r1)
                result.append(r2)
                print(r1,r2)
                return result
        else:
            if cost.count(sunny) > 1:
                j = cost[cost.index(sunny) + 1:].index(johnny)
                r1 = cost.index(sunny) + 1
                r2 = j + 2 + cost.index(sunny)
                result.append(r1)
                result.append(r2)
                print(r1,r2)
                return result

t = int(input())
for t_itr in range(t):
    money = int(input().strip())
    n = int(input().strip())
    cost = list(map(int, input().rstrip().split()))
    result = whatFlavors(cost, money)
    print(result)

