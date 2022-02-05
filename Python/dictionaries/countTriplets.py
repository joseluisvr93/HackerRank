
def countTriplets(arr, r):
    res = 0
    bef={}
    aft={}
    for i in arr:
        if i in aft:
            aft[i]+=1
        else:
            aft[i]=1
    for i in arr:
        aft[i]-=1
        if i//r in bef and i %r ==0 and i*r in aft:
            res += bef[i//r]*aft[i*r]
        if i in bef:
            bef[i]+=1
        else:
            bef[i]=1
    print(res)
    return res

nr = input().rstrip().split()

n = int(nr[0])

r = int(nr[1])

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

