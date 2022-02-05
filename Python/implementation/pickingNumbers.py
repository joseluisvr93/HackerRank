def pickingNumbers(a):
    a.sort()
    print(a)
    res = 0
    resmax = 0
    for i in range(len(a)-1):
        res = len([j for j in a if j==a[i]])
        res += len([j for j in a if j==(a[i]+1)])
        if res > resmax:
            resmax = res
    return resmax
    # Write your code here

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)

print(result)
