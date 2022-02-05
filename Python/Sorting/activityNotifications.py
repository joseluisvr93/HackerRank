import bisect
def activityNotifications(expenditure, d, n):
    a = sorted(expenditure[:d])
    res = 0
    m=d//2
    for i in range(d,n):
        if (med(a,d,m)*2) <= expenditure[i]:
            res += 1
        del a[bisect.bisect_left(a,expenditure[i-d])]
        bisect.insort(a,expenditure[i])
    return res
def med(arr,d,m):
    if d%2==0:
        return sum(arr[m-1:m+1])/2
    else:
        return arr[int(m)]

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
expenditure = list(map(int, input().rstrip().split()))
result = activityNotifications(expenditure, d, n)

print(result)
