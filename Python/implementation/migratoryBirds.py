import math
from collections import Counter

def migratoryBirds(arr):
    arr = sorted(arr)
    ar = Counter(arr)
    maximo = 0
    res = 0
    print(ar)
    for key in ar.keys():
        if ar[key] > maximo:
            maximo = ar[key]
            res = key
    return res


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratoryBirds(arr)

print(result)
